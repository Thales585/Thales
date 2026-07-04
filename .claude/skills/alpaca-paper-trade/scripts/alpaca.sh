#!/usr/bin/env bash
# Alpaca paper-trading helper for the Thales ledger.
# PAPER TRADING ONLY. No real money is at stake.
#
# Credentials are read from ~/.config/alpaca/paper-trading.env
# (override with ALPACA_ENV_FILE). Never hard-code keys in a skill or repo.
#
# Usage:
#   alpaca.sh account
#   alpaca.sh clock
#   alpaca.sh positions
#   alpaca.sh orders [status]           # status: open|closed|all (default open)
#   alpaca.sh order <order_id>
#   alpaca.sh buy  <SYMBOL> <QTY> [limit_price]
#   alpaca.sh sell <SYMBOL> <QTY> [limit_price]
#   alpaca.sh cancel <order_id>
#
# Market orders when no limit price is given; limit + GTC when one is.
set -euo pipefail

ENV_FILE="${ALPACA_ENV_FILE:-$HOME/.config/alpaca/paper-trading.env}"
if [[ ! -f "$ENV_FILE" ]]; then
  echo "error: credentials file not found: $ENV_FILE" >&2
  exit 1
fi
# shellcheck disable=SC1090
source "$ENV_FILE"

: "${ALPACA_API_KEY_ID:?missing ALPACA_API_KEY_ID in $ENV_FILE}"
: "${ALPACA_API_SECRET_KEY:?missing ALPACA_API_SECRET_KEY in $ENV_FILE}"
BASE="${ALPACA_API_BASE_URL:-https://paper-api.alpaca.markets/v2}"

# Safety rail: refuse to run against the live trading host.
if [[ "$BASE" != *"paper-api.alpaca.markets"* ]]; then
  echo "error: refusing to run — base URL is not the paper endpoint: $BASE" >&2
  exit 1
fi

api() {
  local method="$1" path="$2" body="${3:-}"
  local args=(-sS -X "$method"
    -H "APCA-API-KEY-ID: $ALPACA_API_KEY_ID"
    -H "APCA-API-SECRET-KEY: $ALPACA_API_SECRET_KEY"
    -w $'\n%{http_code}')
  [[ -n "$body" ]] && args+=(-H "Content-Type: application/json" -d "$body")
  local out code
  out="$(curl "${args[@]}" "$BASE$path")"
  code="${out##*$'\n'}"
  out="${out%$'\n'*}"
  if command -v jq >/dev/null 2>&1; then echo "$out" | jq .; else echo "$out"; fi
  if [[ "$code" -ge 400 ]]; then
    echo "HTTP $code" >&2
    return 1
  fi
}

order() {
  local side="$1" symbol="$2" qty="$3" limit="${4:-}"
  local body
  if [[ -n "$limit" ]]; then
    body=$(printf '{"symbol":"%s","qty":"%s","side":"%s","type":"limit","limit_price":"%s","time_in_force":"gtc"}' \
      "$symbol" "$qty" "$side" "$limit")
  else
    body=$(printf '{"symbol":"%s","qty":"%s","side":"%s","type":"market","time_in_force":"day"}' \
      "$symbol" "$qty" "$side")
  fi
  api POST /orders "$body"
}

cmd="${1:-account}"; shift || true
case "$cmd" in
  account)   api GET /account ;;
  clock)     api GET /clock ;;
  positions) api GET /positions ;;
  orders)    api GET "/orders?status=${1:-open}&limit=100&direction=desc" ;;
  order)     api GET "/orders/${1:?order id required}" ;;
  buy)       order buy  "${1:?symbol}" "${2:?qty}" "${3:-}" ;;
  sell)      order sell "${1:?symbol}" "${2:?qty}" "${3:-}" ;;
  cancel)    api DELETE "/orders/${1:?order id required}" ;;
  *) echo "unknown command: $cmd" >&2; exit 2 ;;
esac

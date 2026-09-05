#!/usr/bin/env bash
#
# Fetches the deployed site and applies the same integrity contract as CI.
#
# A status-code check is not enough: the 2026-09-05 stub answered HTTP 200 for
# three and a half hours, so every uptime probe watching status codes saw a
# healthy site. This one reads the body.
#
# Override the target with SITE_URL (used to point at a local server in tests).

set -uo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$repo_root"

# shellcheck source=scripts/lib-page-checks.sh
. scripts/lib-page-checks.sh

site=${SITE_URL:-https://www.thousandsunnytcg.com}
site=${site%/}

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

# Echoes the HTTP status, or 000 when the request never completed. curl still
# writes 000 via -w on a connection failure, so this must not add its own
# fallback on top of that or the two concatenate.
fetch() {
  local url=$1 dest=$2 code
  code=$(curl -sS -L --max-time 30 -o "$dest" -w '%{http_code}' "$url" 2>/dev/null)
  printf '%s' "${code:-000}"
}

echo "Probing ${site}"

home_status=$(fetch "${site}/" "$tmp/index.html")
echo "  GET /               -> HTTP ${home_status}"
if [ "$home_status" != "200" ]; then
  PAGE_FAILURES=$((PAGE_FAILURES + 1))
fi
check_page '/ (homepage)' "$tmp/index.html" "$INDEX_MIN_BYTES" "${INDEX_MARKERS[@]}"

optcg_status=$(fetch "${site}/one-piece-tcg" "$tmp/optcg.html")
echo "  GET /one-piece-tcg  -> HTTP ${optcg_status}"
if [ "$optcg_status" != "200" ]; then
  PAGE_FAILURES=$((PAGE_FAILURES + 1))
fi
check_page '/one-piece-tcg' "$tmp/optcg.html" "$OPTCG_MIN_BYTES" "${OPTCG_MARKERS[@]}"

if [ "$PAGE_FAILURES" -gt 0 ]; then
  echo
  echo "Live site probe FAILED (${PAGE_FAILURES} problem(s)) against ${site}."
  if [ "$home_status" = "200" ]; then
    echo "The site is answering requests but is not serving the real pages."
  else
    echo "The site did not return a healthy homepage (HTTP ${home_status})."
  fi
  exit 1
fi

echo
echo "Live site probe passed."

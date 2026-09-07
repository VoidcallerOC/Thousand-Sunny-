#!/usr/bin/env bash
# Probe production endpoints that are easy to break while the homepage still returns 200.
set -uo pipefail

site=${SITE_URL:-https://www.thousandsunnytcg.com}
site=${site%/}
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
failures=0

fetch() {
  local url=$1 dest=$2 code
  code=$(curl -sS -L --max-time 30 -o "$dest" -w '%{http_code}' "$url" 2>/dev/null || true)
  printf '%s' "${code:-000}"
}
check_status_and_text() {
  local path=$1 expected=$2 file=$3 status=$4
  printf '  GET %-18s -> HTTP %s\n' "$path" "$status"
  if [ "$status" != "200" ]; then
    echo "    FAIL status is not 200"
    failures=$((failures + 1))
  elif ! grep -qF -- "$expected" "$file"; then
    echo "    FAIL missing expected marker: $expected"
    failures=$((failures + 1))
  else
    echo "    ok   contains $expected"
  fi
}

echo "Probing production endpoints at ${site}"

status=$(fetch "${site}/robots.txt" "$tmp/robots.txt")
check_status_and_text '/robots.txt' 'Sitemap: https://www.thousandsunnytcg.com/sitemap.xml' "$tmp/robots.txt" "$status"

status=$(fetch "${site}/sitemap.xml" "$tmp/sitemap.xml")
check_status_and_text '/sitemap.xml' 'https://www.thousandsunnytcg.com/one-piece-tcg' "$tmp/sitemap.xml" "$status"

status=$(fetch "${site}/google2e7599ccbf2b6cc2.html" "$tmp/verification.html")
check_status_and_text '/google verification' 'google-site-verification' "$tmp/verification.html" "$status"

status=$(fetch "${site}/assets/js/main.js" "$tmp/main.js")
check_status_and_text '/assets/js/main.js' 'function track' "$tmp/main.js" "$status"

if [ "$failures" -gt 0 ]; then
  echo
  echo "Production endpoint probe FAILED ($failures problem(s))."
  exit 1
fi

echo
echo "Production endpoint probe passed."

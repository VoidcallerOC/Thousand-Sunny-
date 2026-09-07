#!/usr/bin/env bash
# Deployment contract for the Vercel ignored-build hook.
# Exit 0 means safe; any failure prevents the build from replacing production.
set -uo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$repo_root"

failures=0
fail() { printf 'FAIL  %s\n' "$*"; failures=$((failures + 1)); }
ok() { printf 'ok    %s\n' "$*"; }

echo "Deployment contract"
if bash scripts/check-page-integrity.sh; then ok "page integrity"; else fail "page integrity"; fi

for required in index.html one-piece-tcg.html robots.txt sitemap.xml vercel.json assets/css/styles.css assets/js/main.js; do
  if [ -s "$required" ]; then ok "required file: $required"; else fail "missing or empty required file: $required"; fi
done

if grep -qF 'Sitemap: https://www.thousandsunnytcg.com/sitemap.xml' robots.txt; then
  ok "robots.txt points to the canonical sitemap"
else
  fail "robots.txt is missing the canonical sitemap declaration"
fi

if grep -qF 'https://www.thousandsunnytcg.com/' sitemap.xml && grep -qF 'https://www.thousandsunnytcg.com/one-piece-tcg' sitemap.xml; then
  ok "sitemap contains the canonical routes"
else
  fail "sitemap is missing canonical routes"
fi

if grep -qF 'ignoreCommand' vercel.json && grep -qF 'scripts/vercel-ignore-build.sh' vercel.json; then
  ok "Vercel is wired to the deployment gate"
else
  fail "Vercel ignoreCommand is not wired to the deployment gate"
fi

if [ "$failures" -gt 0 ]; then
  echo
  echo "Deployment contract FAILED ($failures problem(s))."
  exit 1
fi

echo
echo "Deployment contract passed."

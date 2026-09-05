#!/usr/bin/env bash
#
# Fails when a published page has been replaced by a stub, a placeholder, or a
# truncated file.
#
# On 2026-09-05, f1a1fd7 replaced index.html with an 11-byte "PLACEHOLDER" and
# 9027e09 replaced that with a 141-byte "restore-pending" stub. Both commit
# messages claimed to be restoring the homepage. Both deployed cleanly, and the
# site served a blank page for three and a half hours.
#
# Exit 0 = every page is intact.  Exit 1 = at least one page is broken.

set -uo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$repo_root"

# shellcheck source=scripts/lib-page-checks.sh
. scripts/lib-page-checks.sh

echo "Page integrity check"
check_page 'index.html'         'index.html'         "$INDEX_MIN_BYTES" "${INDEX_MARKERS[@]}"
check_page 'one-piece-tcg.html' 'one-piece-tcg.html' "$OPTCG_MIN_BYTES" "${OPTCG_MARKERS[@]}"

if [ "$PAGE_FAILURES" -gt 0 ]; then
  echo
  echo "Page integrity check FAILED (${PAGE_FAILURES} problem(s))."
  echo
  echo "A page looks stubbed, gutted or truncated. Restore it from the last"
  echo "good commit rather than committing a placeholder:"
  echo
  echo "    git log --oneline -- index.html"
  echo "    git show <good-sha>:index.html > index.html"
  exit 1
fi

echo
echo "Page integrity check passed."

#!/usr/bin/env bash
#
# Vercel "Ignored Build Step", wired up via ignoreCommand in vercel.json.
#
# This is the guard that actually keeps a broken homepage off the live site.
# A failing GitHub Actions run does NOT stop a Vercel deployment: on
# 2026-09-05 the CI runs for f1a1fd7 and 9027e09 both went red, and Vercel
# published both commits to production regardless. Only this hook can refuse
# the deploy.
#
# Vercel's contract is inverted from a normal check:
#
#   exit 0  ->  SKIP the build   (the current production deployment keeps serving)
#   exit 1  ->  PROCEED with the build
#
# So a page that fails the integrity check must exit 0 here. Skipping the build
# leaves the last good deployment live instead of replacing it with a stub.

set -uo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$repo_root"

if bash scripts/check-page-integrity.sh; then
  echo
  echo "Pages intact — continuing with the build."
  exit 1
fi

echo
echo "=============================================================="
echo " DEPLOY REFUSED: page integrity check failed for this commit."
echo " The previous deployment stays live and keeps serving traffic."
echo " Fix the page and push again."
echo "=============================================================="
exit 0

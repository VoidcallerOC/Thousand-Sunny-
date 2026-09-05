# shellcheck shell=bash
#
# Shared page-integrity contract.
#
# Sourced by check-page-integrity.sh (which inspects the files in the repo) and
# by probe-live-site.sh (which inspects what the deployed site actually serves),
# so both enforce exactly the same definition of "this page is intact".
#
# Keep the markers to things whose absence means the page is genuinely broken —
# structure, the shop's address and phone, the stylesheet and script wiring.
# They are deliberately not a style guide: normal copy edits must not trip them.

INDEX_MIN_BYTES=20000
OPTCG_MIN_BYTES=8000

INDEX_MARKERS=(
  'West Hartford'
  '75 Park Rd'
  '7573587643'
  'schema.org'
  '<main'
  '<footer'
  'hero-lead'
  'id="visit"'
  '/assets/css/styles.css'
  '/assets/js/main.js'
)

OPTCG_MARKERS=(
  'One Piece'
  '75 Park Rd'
  'schema.org'
  '<main'
  '<footer'
  '/assets/css/styles.css'
)

# Matched case-sensitively and literally, so the lowercase placeholder="..."
# attribute on the offer form is not mistaken for a stubbed page.
PLACEHOLDER_SENTINELS=(
  'restore-pending'
  'PLACEHOLDER'
  'TODO-RESTORE'
)

PAGE_FAILURES=0

_note() { printf '    %s\n' "$*"; }

# check_page <label> <file> <min_bytes> <marker>...
check_page() {
  local label=$1 file=$2 min_bytes=$3
  shift 3
  local markers=("$@")

  printf '  %s\n' "$label"

  if [ ! -s "$file" ]; then
    _note "FAIL  missing or empty"
    PAGE_FAILURES=$((PAGE_FAILURES + 1))
    return
  fi

  local size
  size=$(wc -c < "$file" | tr -d '[:space:]')
  if [ "$size" -lt "$min_bytes" ]; then
    _note "FAIL  truncated: ${size} bytes, expected at least ${min_bytes}"
    PAGE_FAILURES=$((PAGE_FAILURES + 1))
  else
    _note "ok    ${size} bytes"
  fi

  local marker
  for marker in "${markers[@]}"; do
    if ! grep -qF -- "$marker" "$file"; then
      _note "FAIL  missing content: ${marker}"
      PAGE_FAILURES=$((PAGE_FAILURES + 1))
    fi
  done

  local sentinel
  for sentinel in "${PLACEHOLDER_SENTINELS[@]}"; do
    if grep -qF -- "$sentinel" "$file"; then
      _note "FAIL  placeholder text present: ${sentinel}"
      PAGE_FAILURES=$((PAGE_FAILURES + 1))
    fi
  done
}

#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

ENGINEER_SOURCE="${REPO_ROOT}/runtime/codex/AGENTS.md"
AGY_SOURCE="${REPO_ROOT}/runtime/agy/engineer-specialist/agent.md"

ENGINEER_DEST="${HOME}/.codex/AGENTS.md"
AGY_DEST="${HOME}/.gemini/config/agents/engineer-specialist/agent.md"

MODE="sync"

usage() {
  cat >&2 <<'EOF'
usage:
  sync-codex-runtime.sh [--check]

examples:
  bash scripts/sync-codex-runtime.sh
  bash scripts/sync-codex-runtime.sh --check
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --check)
      MODE="check"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "unknown argument: $1" >&2
      usage
      exit 64
      ;;
  esac
done

for src in "${ENGINEER_SOURCE}" "${AGY_SOURCE}"; do
  if [[ ! -f "${src}" ]]; then
    echo "missing canonical source: ${src}" >&2
    exit 66
  fi
done

status_line() {
  local src="$1"
  local dest="$2"
  local label="$3"

  if [[ -f "${dest}" ]] && cmp -s "${src}" "${dest}"; then
    echo "${label}: current"
  elif [[ -f "${dest}" ]]; then
    echo "${label}: update available"
  else
    echo "${label}: not installed"
  fi
}

if [[ "${MODE}" == "check" ]]; then
  status_line "${ENGINEER_SOURCE}" "${ENGINEER_DEST}" "Engineer AGENTS"
  status_line "${AGY_SOURCE}" "${AGY_DEST}" "agy engineer-specialist"
  exit 0
fi

mkdir -p "$(dirname "${ENGINEER_DEST}")"
mkdir -p "$(dirname "${AGY_DEST}")"

TIMESTAMP="$(date -u +%Y%m%dT%H%M%SZ)"

install_one() {
  local src="$1"
  local dest="$2"
  local label="$3"

  if [[ -f "${dest}" ]] && cmp -s "${src}" "${dest}"; then
    echo "${label}: already current"
    return
  fi

  if [[ -f "${dest}" ]]; then
    local backup="${dest}.bak.${TIMESTAMP}"
    cp "${dest}" "${backup}"
    echo "${label}: backed up previous file to ${backup}"
  fi

  mkdir -p "$(dirname "${dest}")"
  cp "${src}" "${dest}"
  chmod 0644 "${dest}"
  echo "${label}: installed ${dest}"
}

install_one "${ENGINEER_SOURCE}" "${ENGINEER_DEST}" "Engineer AGENTS"
install_one "${AGY_SOURCE}" "${AGY_DEST}" "agy engineer-specialist"

echo "sync complete"
echo "Engineer runtime: ${ENGINEER_DEST}"
echo "agy specialist: ${AGY_DEST}"
echo "WebCodex should reference the same Engineer runtime as a Runner-global instruction source."

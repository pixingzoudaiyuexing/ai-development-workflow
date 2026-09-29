#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

CODEX_SOURCE="${REPO_ROOT}/runtime/codex/AGENTS.md"
AGY_SOURCE="${REPO_ROOT}/runtime/agy/engineer-specialist/agent.md"

CODEX_DEST="${HOME}/.codex/AGENTS.md"
AGY_DEST="${HOME}/.gemini/config/agents/engineer-specialist/agent.md"

MODE="${1:-sync}"

if [[ "${MODE}" != "sync" && "${MODE}" != "--check" ]]; then
  echo "usage: $0 [--check]" >&2
  exit 64
fi

for src in "${CODEX_SOURCE}" "${AGY_SOURCE}"; do
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

if [[ "${MODE}" == "--check" ]]; then
  status_line "${CODEX_SOURCE}" "${CODEX_DEST}" "Codex AGENTS"
  status_line "${AGY_SOURCE}" "${AGY_DEST}" "agy engineer-specialist"
  exit 0
fi

mkdir -p "$(dirname "${CODEX_DEST}")"
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

  cp "${src}" "${dest}"
  chmod 0644 "${dest}"
  echo "${label}: installed ${dest}"
}

install_one "${CODEX_SOURCE}" "${CODEX_DEST}" "Codex AGENTS"
install_one "${AGY_SOURCE}" "${AGY_DEST}" "agy engineer-specialist"

echo "sync complete"
echo "Codex runtime: ${CODEX_DEST}"
echo "agy specialist: ${AGY_DEST}"
echo "WebCodex runtime was not modified."

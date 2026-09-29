#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

CODEX_SOURCE="${REPO_ROOT}/runtime/codex/AGENTS.md"
AGY_SOURCE="${REPO_ROOT}/runtime/agy/engineer-specialist/agent.md"

CODEX_DEST="${HOME}/.codex/AGENTS.md"
AGY_DEST="${HOME}/.gemini/config/agents/engineer-specialist/agent.md"

MODE="sync"
WEB_PROJECTS=()

usage() {
  cat >&2 <<'EOF'
usage:
  sync-codex-runtime.sh [--check] [--webcodex-project <project-root>]...

examples:
  bash scripts/sync-codex-runtime.sh
  bash scripts/sync-codex-runtime.sh --check
  bash scripts/sync-codex-runtime.sh \
    --webcodex-project /Users/wang/Documents/webcodex/projects/CZ2128
  bash scripts/sync-codex-runtime.sh --check \
    --webcodex-project /Users/wang/Documents/webcodex/projects/CZ2128
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --check)
      MODE="check"
      shift
      ;;
    --webcodex-project)
      if [[ $# -lt 2 || -z "$2" ]]; then
        echo "missing value for --webcodex-project" >&2
        usage
        exit 64
      fi
      WEB_PROJECTS+=("$2")
      shift 2
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

resolve_project_root() {
  local requested="$1"

  if [[ ! -d "${requested}" ]]; then
    echo "WebCodex project root does not exist: ${requested}" >&2
    exit 66
  fi

  (
    cd "${requested}"
    pwd -P
  )
}

if [[ "${MODE}" == "check" ]]; then
  status_line "${CODEX_SOURCE}" "${CODEX_DEST}" "Codex AGENTS"
  status_line "${AGY_SOURCE}" "${AGY_DEST}" "agy engineer-specialist"

  for requested in "${WEB_PROJECTS[@]}"; do
    root="$(resolve_project_root "${requested}")"
    dest="${root}/.codex/AGENTS.md"
    status_line "${CODEX_SOURCE}" "${dest}" "WebCodex Engineer AGENTS [${root}]"
  done

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

  mkdir -p "$(dirname "${dest}")"
  cp "${src}" "${dest}"
  chmod 0644 "${dest}"
  echo "${label}: installed ${dest}"
}

install_one "${CODEX_SOURCE}" "${CODEX_DEST}" "Codex AGENTS"
install_one "${AGY_SOURCE}" "${AGY_DEST}" "agy engineer-specialist"

for requested in "${WEB_PROJECTS[@]}"; do
  root="$(resolve_project_root "${requested}")"
  dest="${root}/.codex/AGENTS.md"
  install_one "${CODEX_SOURCE}" "${dest}" "WebCodex Engineer AGENTS [${root}]"
done

echo "sync complete"
echo "Codex runtime: ${CODEX_DEST}"
echo "agy specialist: ${AGY_DEST}"

if [[ ${#WEB_PROJECTS[@]} -eq 0 ]]; then
  echo "WebCodex runtime: no project target requested"
else
  echo "WebCodex runtime: synced ${#WEB_PROJECTS[@]} project target(s)"
fi

#!/usr/bin/env bash
# Legacy bash runner - for Linux/Mac users who prefer shell scripts.
# Cross-platform alternative: python scripts/run_agent.py

set -euo pipefail

PROJECT_PATH="${1:-}"
if [[ -z "${PROJECT_PATH}" ]]; then
  echo "Usage: scripts/run_agent.sh <project_path>" >&2
  exit 2
fi

RUNNER="${SDR_RUNNER:-none}"
RULES_FILE="prompts/SDR_RULES.txt"

if [[ ! -f "${RULES_FILE}" ]]; then
  echo "Missing rules file: ${RULES_FILE}" >&2
  exit 2
fi

if [[ "${RUNNER}" == "none" ]]; then
  echo "SDR_RUNNER=none -> skipping agent run (manual mode)."
  exit 0
fi

SPEC_FILE="${PROJECT_PATH}/SPEC.md"
METHOD_FILE="${PROJECT_PATH}/METHOD.md"

if [[ ! -f "${SPEC_FILE}" || ! -f "${METHOD_FILE}" ]]; then
  echo "Project missing SPEC.md or METHOD.md in ${PROJECT_PATH}" >&2
  exit 2
fi

PROMPT=$(cat <<'EOF'
Read the project files:
- SPEC.md
- METHOD.md
- CLAIMS.yml
- EVIDENCE.csv
- REPORT.md

Follow SDR_RULES strictly. Update CLAIMS.yml, then EVIDENCE.csv, then REPORT.md.
EOF
)

case "${RUNNER}" in
  gemini)
    if ! command -v gemini >/dev/null 2>&1; then
      echo "gemini CLI not found. Install Gemini CLI and set GEMINI_API_KEY." >&2
      exit 2
    fi
    # Gemini CLI uses GEMINI.md automatically if present.
    gemini -p "$(cat "${RULES_FILE}")"$'\n\n'"${PROMPT}" --yolo --dir "${PROJECT_PATH}"
    ;;

  claude)
    if ! command -v claude >/dev/null 2>&1; then
      echo "Claude Code CLI not found. Install it and set ANTHROPIC_API_KEY." >&2
      exit 2
    fi
    # Many setups support appending a system prompt file; if yours differs, adjust here.
    claude --append-system-prompt-file "${RULES_FILE}" --cwd "${PROJECT_PATH}" "${PROMPT}"
    ;;

  codex)
    if ! command -v codex >/dev/null 2>&1; then
      echo "Codex CLI not found. Install it (npm i -g @openai/codex) and set OPENAI_API_KEY." >&2
      exit 2
    fi
    # Codex CLI interface can vary by version; treat this as adapter stub.
    # Recommendation: use codex in 'exec' mode pointing at the project directory.
    codex exec --cwd "${PROJECT_PATH}" --system "$(cat "${RULES_FILE}")" --prompt "${PROMPT}"
    ;;

  copilot)
    echo "Copilot is IDE/terminal-driven; best used locally. This adapter is a stub."
    echo "Run locally and let Copilot update artifacts under ${PROJECT_PATH}, then run validators."
    exit 2
    ;;

  kilo)
    echo "Kilo Code CLI adapter stub (local-first)."
    echo "Suggestion: create .kilocode/skills/sdr/ and run kilo with that skill + project path."
    exit 2
    ;;

  opencode)
    echo "OpenCode adapter stub (local-first)."
    echo "Suggestion: configure an OpenCode agent to follow prompts/SDR_RULES.txt and update ${PROJECT_PATH}."
    exit 2
    ;;

  antigravity)
    echo "Antigravity adapter stub (interactive/local)."
    echo "Suggestion: run Antigravity in your IDE with SDR_RULES and point it at ${PROJECT_PATH}."
    exit 2
    ;;

  *)
    echo "Unknown SDR_RUNNER: ${RUNNER}" >&2
    echo "Valid: none|gemini|claude|codex|copilot|kilo|opencode|antigravity" >&2
    exit 2
    ;;
esac

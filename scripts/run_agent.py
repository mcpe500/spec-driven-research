#!/usr/bin/env python3
"""
Cross-platform SDR agent runner.
Supports: gemini, claude, codex, copilot, kilo, opencode, antigravity
"""

import argparse
from datetime import datetime
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES_FILE = ROOT / "prompts" / "SDR_RULES.txt"

VALID_RUNNERS = [
    "none",
    "gemini",
    "claude",
    "codex",
    "copilot",
    "kilo",
    "opencode",
    "antigravity",
]

SDR_PROMPT = """Read the project files:
- SPEC.md
- METHOD.md
- CLAIMS.yml
- EVIDENCE.csv
- REPORT.md

Follow SDR_RULES strictly. Update CLAIMS.yml, then EVIDENCE.csv, then REPORT.md."""


class RunLogger:
    def __init__(self, log_path: Path, enabled: bool) -> None:
        self.log_path = log_path
        self.enabled = enabled

    def append_block(self, lines: list[str]) -> None:
        if not self.enabled:
            return
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        text = "\n".join(lines).rstrip() + "\n\n"
        self.log_path.open("a", encoding="utf-8", newline="\n").write(text)


RUN_LOGGER: RunLogger | None = None


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def redact_cli_args(args: list[str]) -> list[str]:
    """Redact large/sensitive prompt arguments so logs stay readable and safe."""
    redacted: list[str] = []
    omit_next = False
    omit_next_for = {"-p", "--prompt", "--system"}

    for a in args:
        if omit_next:
            redacted.append("<omitted>")
            omit_next = False
            continue

        if a in omit_next_for:
            redacted.append(a)
            omit_next = True
            continue

        if "\n" in a or len(a) > 200:
            redacted.append("<omitted>")
        else:
            redacted.append(a)

    return redacted


def die(msg: str) -> None:
    """Print error and exit."""
    if RUN_LOGGER is not None:
        RUN_LOGGER.append_block(
            [
                f"### agent_run: ERROR ({now_iso()})",
                f"- message: {msg}",
            ]
        )
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def resolve_command(cmd: str) -> str | None:
    """Resolve a command name to an executable path using PATH/PATHEXT."""
    return shutil.which(cmd)


def run_resolved_command(resolved: str, args: list[str], *, cwd: Path | None = None) -> None:
    """Run a resolved command cross-platform.

    On Windows, many CLIs are installed as .cmd/.bat wrappers (e.g. via npm). Those
    can't be launched directly via CreateProcess reliably unless invoked through cmd.
    """
    is_windows = os.name == "nt"
    suffix = Path(resolved).suffix.lower()
    cwd_str = str(cwd) if cwd is not None else None

    cmd: list[str]
    if is_windows and suffix in {".cmd", ".bat"}:
        cmd = ["cmd", "/c", resolved, *args]
    else:
        cmd = [resolved, *args]

    if RUN_LOGGER is not None:
        RUN_LOGGER.append_block(
            [
                f"### agent_run: COMMAND ({now_iso()})",
                f"- cwd: {cwd_str or ''}",
                f"- cmd: {cmd[:3] + redact_cli_args(cmd[3:]) if (is_windows and suffix in {'.cmd', '.bat'}) else [cmd[0], *redact_cli_args(cmd[1:])]}",
            ]
        )

    try:
        subprocess.run(cmd, check=True, cwd=cwd_str)
    except FileNotFoundError as e:
        die(
            "Failed to start CLI process. This usually means the command is only available "
            "as a shell alias/function, or PATH differs between your shell and Python. "
            f"Resolved='{resolved}'. Original error: {e}"
        )
    except subprocess.CalledProcessError as e:
        die(f"CLI exited with status {e.returncode}: {cmd}")


def run_gemini(project_path: Path, rules: str) -> None:
    """Run Gemini CLI."""
    resolved = resolve_command("gemini")
    if not resolved:
        die(
            "gemini CLI not found in PATH. Install Gemini CLI and set GEMINI_API_KEY. "
            "(Note: Python can't use PowerShell-only aliases.)"
        )
    
    prompt = f"{rules}\n\n{SDR_PROMPT}"
    run_resolved_command(
        resolved,
        ["-p", prompt, "--yolo", "--dir", str(project_path)],
        cwd=project_path,
    )


def run_claude(project_path: Path, rules_file: Path) -> None:
    """Run Claude Code CLI."""
    resolved = resolve_command("claude")
    if not resolved:
        die(
            "Claude Code CLI not found in PATH. Install it and set ANTHROPIC_API_KEY. "
            "(Note: Python can't use PowerShell-only aliases.)"
        )
    
    run_resolved_command(
        resolved,
        [
            "--append-system-prompt-file",
            str(rules_file),
            SDR_PROMPT,
        ],
        cwd=project_path,
    )


def run_codex(project_path: Path, rules: str) -> None:
    """Run OpenAI Codex CLI."""
    resolved = resolve_command("codex")
    if not resolved:
        die("Codex CLI not found. Install it (npm i -g @openai/codex) and set OPENAI_API_KEY.")
    
    run_resolved_command(
        resolved,
        [
            "exec",
            "--cwd",
            str(project_path),
            "--system",
            rules,
            "--prompt",
            SDR_PROMPT,
        ],
        cwd=project_path,
    )


def run_copilot(project_path: Path) -> None:
    """Copilot stub - IDE/terminal driven."""
    print("=" * 60)
    print("Copilot is IDE/terminal-driven; best used locally.")
    print("This adapter is a stub.")
    print()
    print("Instructions:")
    print(f"1. Open {project_path} in your IDE with Copilot enabled")
    print("2. Use Copilot Chat with the SDR_RULES.txt as context")
    print("3. Update artifacts: CLAIMS.yml -> EVIDENCE.csv -> REPORT.md")
    print("4. Run validator: python scripts/validate_project.py <project>")
    print("=" * 60)
    if RUN_LOGGER is not None:
        RUN_LOGGER.append_block(
            [
                f"### agent_run: STUB ({now_iso()})",
                "- runner: copilot",
                f"- project: {project_path}",
            ]
        )
    sys.exit(2)


def run_kilo(project_path: Path) -> None:
    """Kilo Code CLI stub."""
    print("=" * 60)
    print("Kilo Code CLI adapter stub (local-first).")
    print()
    print("Suggestion:")
    print("1. Create .kilocode/skills/sdr/ with SDR skill definitions")
    print(f"2. Run kilo with that skill pointing at {project_path}")
    print("3. Update artifacts following SDR_RULES.txt")
    print("=" * 60)
    if RUN_LOGGER is not None:
        RUN_LOGGER.append_block(
            [
                f"### agent_run: STUB ({now_iso()})",
                "- runner: kilo",
                f"- project: {project_path}",
            ]
        )
    sys.exit(2)


def run_opencode(project_path: Path) -> None:
    """OpenCode adapter stub."""
    print("=" * 60)
    print("OpenCode adapter stub (local-first).")
    print()
    print("Suggestion:")
    print("1. Configure an OpenCode agent to follow prompts/SDR_RULES.txt")
    print(f"2. Point it at {project_path}")
    print("3. Let it update CLAIMS.yml -> EVIDENCE.csv -> REPORT.md")
    print("=" * 60)
    if RUN_LOGGER is not None:
        RUN_LOGGER.append_block(
            [
                f"### agent_run: STUB ({now_iso()})",
                "- runner: opencode",
                f"- project: {project_path}",
            ]
        )
    sys.exit(2)


def run_antigravity(project_path: Path) -> None:
    """Antigravity adapter stub."""
    print("=" * 60)
    print("Antigravity adapter stub (interactive/local).")
    print()
    print("Suggestion:")
    print("1. Run Antigravity in your IDE")
    print("2. Load SDR_RULES.txt as system context")
    print(f"3. Point it at {project_path}")
    print("4. Follow the artifact update order")
    print("=" * 60)
    if RUN_LOGGER is not None:
        RUN_LOGGER.append_block(
            [
                f"### agent_run: STUB ({now_iso()})",
                "- runner: antigravity",
                f"- project: {project_path}",
            ]
        )
    sys.exit(2)


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Run an SDR agent to update project artifacts"
    )
    ap.add_argument(
        "project_path",
        help="Path to project folder, e.g. projects/contoh-topik"
    )
    ap.add_argument(
        "--runner", "-r",
        default=os.environ.get("SDR_RUNNER", "none"),
        choices=VALID_RUNNERS,
        help="Agent runner to use (default: none, or from SDR_RUNNER env var)"
    )
    ap.add_argument(
        "--no-log",
        action="store_true",
        help="Disable writing RUN_LOG.md history entries"
    )
    ap.add_argument(
        "--log-file",
        default="RUN_LOG.md",
        help="Run history log filename inside the project folder (default: RUN_LOG.md)"
    )
    args = ap.parse_args()

    project_path = Path(args.project_path)
    runner = args.runner.lower()

    # Validate project path
    if not project_path.exists() or not project_path.is_dir():
        die(f"Project path not found: {project_path}")

    global RUN_LOGGER
    RUN_LOGGER = RunLogger(project_path / str(args.log_file), enabled=not bool(args.no_log))
    RUN_LOGGER.append_block(
        [
            f"## SDR agent run ({now_iso()})",
            f"- project: {project_path}",
            f"- runner: {runner}",
            f"- python: {sys.version.split()[0]}",
            "- note: prompts/system text is omitted from logs by design",
        ]
    )

    spec_file = project_path / "SPEC.md"
    method_file = project_path / "METHOD.md"
    if not spec_file.exists() or not method_file.exists():
        die(f"Project missing SPEC.md or METHOD.md in {project_path}")

    # Validate rules file
    if not RULES_FILE.exists():
        die(f"Missing rules file: {RULES_FILE}")

    rules = RULES_FILE.read_text(encoding="utf-8")

    # Handle runners
    if runner == "none":
        print("SDR_RUNNER=none -> skipping agent run (manual mode).")
        print(f"Edit artifacts manually in {project_path}, then run validator.")
        if RUN_LOGGER is not None:
            RUN_LOGGER.append_block(
                [
                    f"### agent_run: SKIPPED ({now_iso()})",
                    "- runner: none",
                ]
            )
        return

    print(f"Running SDR agent: {runner}")
    print(f"Project: {project_path}")
    print("-" * 40)

    if runner == "gemini":
        run_gemini(project_path, rules)
    elif runner == "claude":
        run_claude(project_path, RULES_FILE)
    elif runner == "codex":
        run_codex(project_path, rules)
    elif runner == "copilot":
        run_copilot(project_path)
    elif runner == "kilo":
        run_kilo(project_path)
    elif runner == "opencode":
        run_opencode(project_path)
    elif runner == "antigravity":
        run_antigravity(project_path)
    else:
        die(f"Unknown runner: {runner}. Valid: {', '.join(VALID_RUNNERS)}")

    if RUN_LOGGER is not None:
        RUN_LOGGER.append_block(
            [
                f"### agent_run: OK ({now_iso()})",
                f"- runner: {runner}",
            ]
        )


if __name__ == "__main__":
    main()

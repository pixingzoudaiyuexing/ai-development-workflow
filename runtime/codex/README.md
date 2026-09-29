# Shared Engineer Runtime Deployment

This directory contains the canonical Engineer runtime rules shared by Codex and WebCodex.

## Canonical Source

```text
runtime/codex/AGENTS.md
```

Verified deployment targets:

```text
Ordinary Codex:
~/.codex/AGENTS.md

WebCodex:
<WebCodex registered project root>/.codex/AGENTS.md
```

Ordinary Codex loads the global file from its home directory. WebCodex does not automatically load that home-level file; it loads the shared runtime copy from the registered project root.

## Three Layers

```text
~/.codex/AGENTS.md
= machine-wide Engineer runtime behavior

<project>/AGENTS.md
= project-specific engineering rules

Current Engineer Task
= current outcome, scope, acceptance, and risk
```

Do not copy the full long-form `roles/ENGINEER.md` into global AGENTS. The long-form role is the workflow source of truth; the runtime AGENTS file is the compact always-loaded execution contract.

## agy Specialist

Canonical custom-agent source:

```text
runtime/agy/engineer-specialist/agent.md
```

Deployment target:

```text
~/.gemini/config/agents/engineer-specialist/agent.md
```

Codex invokes it through the canonical launcher:

```text
/Users/wang/bin/agy --agent engineer-specialist ...
```

## Sync

From a local checkout of this workflow repository:

```bash
bash scripts/sync-codex-runtime.sh
```

Check without changing local files:

```bash
bash scripts/sync-codex-runtime.sh --check
```

The script installs both the Codex global AGENTS file and the agy Engineer Specialist definition. Existing different destination files are backed up before replacement.

A new Codex session is required for newly installed global AGENTS instructions to be loaded.

## WebCodex

Engineer responsibilities are the same for Codex and WebCodex, but the verified runtime loading locations differ.

Current verified behavior:

```text
Ordinary Codex:
~/.codex/AGENTS.md
→ loaded as machine-wide Engineer rules

WebCodex:
~/.codex/AGENTS.md
→ not automatically loaded

<WebCodex registered project root>/.codex/AGENTS.md
→ verified shared Engineer runtime rules

<WebCodex registered project root>/AGENTS.md
→ verified project-specific rules
```

The same canonical source remains:

```text
runtime/codex/AGENTS.md
```

Do not maintain a separate hand-edited WebCodex Engineer rules file.

Sync the shared Engineer rules into an explicit registered WebCodex project:

```bash
bash scripts/sync-codex-runtime.sh \
  --webcodex-project /Users/wang/Documents/webcodex/projects/CZ2128
```

Check without changing files:

```bash
bash scripts/sync-codex-runtime.sh --check \
  --webcodex-project /Users/wang/Documents/webcodex/projects/CZ2128
```

For WebCodex, do not rely on parent-workspace AGENTS inheritance, deeper scoped AGENTS injection, or `AGENTS.override.md` until those behaviors are separately re-verified.

The deployment target `<project>/.codex/AGENTS.md` is the shared Engineer runtime layer. It must not overwrite `<project>/AGENTS.md`, which remains project-specific.

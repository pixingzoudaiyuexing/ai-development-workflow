# Codex Runtime Deployment

This directory contains the canonical runtime rules for the Engineer when using Codex.

## Canonical Source

```text
runtime/codex/AGENTS.md
```

Deployment target on Owner's Mac:

```text
~/.codex/AGENTS.md
```

Codex loads global AGENTS instructions from its home directory and then adds repository / directory-specific AGENTS instructions.

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

Engineer responsibilities are the same for Codex and WebCodex.

WebCodex runtime placement / loading of AGENTS is intentionally deferred until its actual runtime behavior is investigated. Do not assume the Codex global path is automatically inherited by WebCodex.

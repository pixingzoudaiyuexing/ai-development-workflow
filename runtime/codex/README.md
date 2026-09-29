# Engineer Runtime Deployment

This directory contains the canonical always-loaded Primary Engineer runtime rules.

## Canonical Source

```text
runtime/codex/AGENTS.md
```

The path is retained for compatibility, but the file itself is runtime-neutral. Do not maintain separate Codex and WebCodex Engineer rule sets.

## Local Deployment

Deploy one shared local copy on Owner's Mac:

```text
~/.codex/AGENTS.md
```

Engineer runtimes consume this same file through their native instruction-loading mechanism. Where a runtime requires explicit registration, point it at the same absolute file rather than creating another rule copy. For the current WebCodex setup, this file is configured once as a Runner-global instruction source.

Do not copy the shared runtime rules into individual projects.

Project-specific rules remain:

```text
<project>/AGENTS.md
```

Current task instructions remain in the current Engineer Task.

The intended layering is:

```text
~/.codex/AGENTS.md
= shared Primary Engineer runtime rules

<project>/AGENTS.md
= project-specific rules

Current Engineer Task
= current goal, scope, acceptance, and risk
```

## agy Specialist

Canonical custom-agent source:

```text
runtime/agy/engineer-specialist/agent.md
```

Deployment target:

```text
~/.gemini/config/agents/engineer-specialist/agent.md
```

Engineer invokes it through:

```text
/Users/wang/bin/agy --agent engineer-specialist ...
```

## Sync

From a local checkout of this workflow repository:

```bash
bash scripts/sync-codex-runtime.sh
```

Check without changing files:

```bash
bash scripts/sync-codex-runtime.sh --check
```

The script syncs:

- the shared Engineer runtime to `~/.codex/AGENTS.md`;
- the agy Engineer Specialist definition to `~/.gemini/config/agents/engineer-specialist/agent.md`.

Existing different destination files are backed up before replacement.

After changing an instruction-source path in a runtime, apply that runtime's configuration as required. Changing the contents of the already configured shared file is then picked up by subsequent instruction observation according to that runtime's native behavior.

## Context Budget

Keep `runtime/codex/AGENTS.md` compact.

WebCodex combines Runner-global and project instruction sources under bounded projection budgets. Project rules must remain available even when global guidance is long, so essential global behavior — Primary Engineer identity, safety, agy role, validation, review boundary, and reporting — must fit early in this file.

Long-form explanation belongs in:

```text
roles/ENGINEER.md
```

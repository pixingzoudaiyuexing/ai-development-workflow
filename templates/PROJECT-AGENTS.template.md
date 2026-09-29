# PROJECT AGENTS — TEMPLATE

> Copy this file to the root of a project repository as `AGENTS.md`.
> Keep it project-specific. Do not duplicate the global Engineer role or generic Codex behavior here.

## Project Identity

- Project:
- Repository:
- Primary language / stack:
- Package manager:
- Runtime / platform:

## Source of Truth

- Architecture:
- Product / behavior decisions:
- API / schema contracts:
- Deployment / infrastructure facts:
- Generated code sources:

## Repository Map

- `src/`:
- `tests/`:
- `docs/`:
- Other important paths:

## Standard Commands

### Install

```bash
# command
```

### Test

```bash
# command
```

### Typecheck

```bash
# command
```

### Lint

```bash
# command
```

### Build

```bash
# command
```

### Local Run / Smoke Test

```bash
# command
```

## Engineering Constraints

- Required architecture patterns:
- Compatibility requirements:
- Performance constraints:
- Security constraints:
- Data / migration constraints:
- API compatibility rules:

## Must Not

- Do not edit:
- Do not commit generated artifacts unless:
- Do not change public behavior without:
- Do not run destructive production actions without:

## Validation Expectations

For changes in this repository, use the smallest sufficient set of:

- focused tests;
- regression tests;
- typecheck;
- lint;
- build;
- runtime / integration / smoke evidence.

Document any validation that cannot be run and why.

## Git / Delivery Rules

- Default branch:
- Branch policy:
- Commit expectations:
- PR requirement:
- CI expectations:

## Project-specific agy Context

Only add facts that help a read-only specialist understand this repository, such as:

- upstream libraries whose versions matter;
- important external services;
- architecture boundaries;
- known fragile areas;
- test conventions.

Do not place proxy configuration, global Engineer behavior, secrets, or machine-specific credentials here.

## Directory Overrides

Keep required project-wide rules in the repository-root `AGENTS.md`.

Use deeper directory-scoped instruction files only when the active runtime is verified to load them for that scope. Do not assume an override mechanism is portable across runtimes.

Do not bloat the root file with rules that are irrelevant to the whole project.

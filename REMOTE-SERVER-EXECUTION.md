# Remote Server Execution Capability — Netcatty MCP

> Scope: authorized remote Linux server operations through the local Codex executor's `netcatty-external` MCP.
> This is an **optional execution capability**, not a new Role Mask, project dependency, or automatic permission granted to every AI conversation.

## 1. Capability and Boundary

- The actual executor must confirm that `netcatty-external` is available in **its own current runtime** before using it.
- Codex may use available Netcatty MCP sessions to inspect, operate, deploy, and validate authorized servers. Other AI conversations do **not** inherit Codex's MCP permissions.
- Product Manager / Project Manager / Project + Product Manager define the outcome, target server, scope, risk, authorization, and acceptance criteria. They must not claim to have executed commands they did not run.
- The existing **Engineer** Role Mask owns authorized technical execution and evidence. DevOps, remote operations, and test/acceptance are task scopes, **not newly created canonical Role Masks**. Independent Reviewer remains a separate formal-review role when required.
- Do not connect to or modify any server just to register this capability.

## 2. Owner-provided Acceptance Baseline (2026-10-14)

The Owner reports a successful acceptance exercise using macOS 15.7.4 (Apple Silicon), Netcatty 1.1.83, Codex CLI 0.151.0, and an enabled local-only MCP named `netcatty-external` registered in `~/.codex/config.toml` with permission mode **Confirm**. The exercise reported discovery of 67 MCP tool definitions.

Reported **PASS** in that local Codex environment:

- MCP discovery and calls;
- identifying saved SSH hosts and active sessions;
- reusing an existing SSH connection;
- running remote Linux commands and retrieving command output / exit status;
- listing and reading remote files through SFTP;
- identifying a remote Linux distribution;
- existing SSH connections remaining usable after the test.

**Not yet verified** in that exercise: establishing a new SSH connection; SFTP writing/upload/deletion; actual business deployment; restoration after fully restarting Netcatty and Codex.

This section is a historical, **Owner-provided** baseline, not independent proof from this repository and not a live statement about host, session, version, or MCP health. Re-check the relevant runtime before each actual operation. Do not publish server inventories, addresses, host credentials, or connection secrets in workflow documents.

## 3. Tool Discovery and Session Discipline

When a task requires a remote Linux server:

1. Determine the **authorized target server** by its saved Netcatty host name; avoid duplicating SSH endpoints or credentials into project files or prompts.
2. Verify whether `netcatty-external` tools are currently exposed to this executor. Inspect their **actual schemas** before invoking them; do not guess arguments.
3. When provided by the installed MCP version, use `get_environment` for environment/sessions and `vault_hosts_list` for saved hosts; prefer an existing matching SSH session.
4. Use `host_open` only if needed for the authorized target. Do not open every saved host.
5. Use `terminal_execute` for suitable short commands; `terminal_start` and `terminal_poll` for supported long-running work; `sftp_*` for supported file operations. Use only tools and operations confirmed available in the current runtime.
6. Before package/service changes, identify `/etc/os-release`, architecture, package manager, init/service manager, and installed components. Do not assume Debian/Ubuntu commands on Alpine/OpenRC.
7. On MCP failure, report the actual tool/permission/connection blocker. Do not claim execution and do not automatically ask the Owner to perform manual SSH steps if a viable authorized Codex handoff exists.

## 4. Authorization, Safety, and Risk Gates

- Preserve Netcatty's **Confirm** permission mode. Never silently switch it to Auto, bypass approval prompts, or evade MCP/host permissions.
- Read-only diagnostics may proceed within the authorized task, subject to Confirm approval prompts.
- Before configuration changes, installs/upgrades, file writes, or deployments, inspect existing state and dependencies; explain relevant impact. Back up or provide a recovery path when warranted.
- Assess service disruption before restarting/replacing services. Inspect targets carefully before deletion; do not perform broad or destructive file operations without explicit current-task authorization.
- SSH, firewall, network and authentication changes require extra checks against lockout. Irreversible/high-risk operations require explicit Owner authorization and applicable `RISK-GATES.md` review gates.
- Never export, copy into prompts, log, commit, or disclose SSH passwords, keys, tokens, MCP bridge credentials, or other secrets.
- A working remote command does not implicitly authorize deployment, privilege escalation, touching another host, or changing production data.

## 5. Engineering, Deployment, and Acceptance

Engineer begins with the real project repository, scoped `AGENTS.md`, architecture docs, Git branch/HEAD/status, and relevant tests. Netcatty does not replace local validation, Git/review gates, or release authority.

For an authorized deployment or repair:

```text
identify target + scope + authority
→ inspect current MCP / SSH session + remote OS and service state
→ local implementation / tests / Git / review (when applicable)
→ assess change risk, backup / rollback, and approval
→ perform authorized remote actions with Netcatty MCP
→ verify remote service and business behavior
→ report actual Evidence + remaining risks
```

Keep separate outcome states:

- implementation complete;
- local tests passed;
- transfer/write completed;
- remote deployment completed;
- service started/healthy;
- real business endpoints/functions verified.

A transfer success or shell exit code alone does not prove the service or business is available. Record relevant target identity, actual commands/actions, output/exit status, service logs, endpoint checks, timestamps where useful, redacted evidence, rollback status, and any validation not run.

## 6. Cross-Conversation Routing

When the current role/runtime lacks Netcatty MCP:

- do not assume access inherited from Codex or a prior conversation;
- deliver one complete, directly forwardable task to an already authorized Codex **Engineer** conversation, with project/recipient code when used, target saved-host **name**, task scope and non-goals, read/write/deployment authority, risk and review requirements, acceptance checks, and expected redacted evidence;
- if no actual execution channel exists, report the missing link rather than claiming deployment;
- verify the returned evidence before updating project status; historical host/session reports are not live facts.

See `WORKFLOW.md`, `HANDOFF.md`, `RISK-GATES.md`, and `runtime/codex/AGENTS.md` for the surrounding role, execution, and safety rules.

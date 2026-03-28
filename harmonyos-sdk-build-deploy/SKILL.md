---
name: harmonyos-sdk-build-deploy
description: Use when Codex needs official HarmonyOS/OpenHarmony SDK toolchain workflows for build output generation, packaging, install, launch, signing, logs, or device-debug based on local developer documentation. Trigger on DevEco SDK command-line tool usage, `hdc`, `bm`, `aa`, `hilog`, `packing-tool`, HAP/HSP/APP packaging, signing, device install, launch, or build/deploy troubleshooting where Codex should prefer local official docs over third-party wrappers.
---

# HarmonyOS SDK Build Deploy

Use this skill when the user wants HarmonyOS or OpenHarmony build, packaging, install, launch, or device-debug guidance and the answer should follow the official HarmonyOS documentation and DevEco SDK toolchain.

Keep the main response focused on the correct official path. Do not default to third-party npm wrappers, custom deploy helpers, or repo-local abstractions unless the user explicitly asks for them.

Prefer local official docs discovered through `HARMONYOS_DOCS_ROOT`. If local docs are unavailable or invalid, fall back to searching the official HarmonyOS documentation site at `https://developer.huawei.com/consumer/cn/doc/`.

Treat `DEVECO_SDK_HOME` as a preferred local environment variable when the repository or local shell already uses it to point at the DevEco SDK root. This variable is a useful local convention, not the only official way to locate the SDK. If it is missing, fall back to the repository's existing build command, the current `PATH`, or OS-appropriate DevEco Studio installation paths before guessing tool locations.

## Workflow Decision Tree

1. Confirm whether the task is about official HarmonyOS toolchain usage.
   Triggers include `hdc`, `bm`, `aa`, HAP/HSP/APP packaging, signing, device install, launch, logs, or build/deploy troubleshooting.
2. Prefer official docs before inferring commands.
   Start with `references/official-build-deploy-sources.md`.
3. Resolve the SDK and tool location before inventing commands.
   - Prefer `DEVECO_SDK_HOME` when it is already set by the repository or user environment
   - Otherwise inspect the repository's existing command lines and scripts
   - Otherwise inspect `PATH` and OS-specific DevEco Studio installation locations
   - Only then derive individual tool paths such as `hdc`, `hvigorw`, or packaging tools
4. Choose the narrowest tool path that solves the request.
   - Build outputs with the repository's real `hvigorw` or DevEco build path
   - Device connection, file transfer, direct install, logs: `hdc`
   - Install, uninstall, dump app info inside device shell: `bm`
   - Launch, stop, attach debug, measure startup: `aa`
   - Package build outputs into HAP/HSP/APP: `packing-tool`
   - Sign native ELF artifacts: `binary-sign-tool`
5. Distinguish build from deploy.
   - Build means producing project outputs with the DevEco or SDK build chain already used by the repo.
   - Deploy means moving artifacts to a device, installing them, launching abilities, and checking logs.
6. Distinguish debug delivery from release packaging.
   - Debug delivery usually ends at HAP install plus `aa start` or DevEco run/debug.
   - Release delivery may require signing checks, APP packaging, and packaging-tool constraints.

## Official Tool Selection

### `hdc`

Use for:
- checking connected devices
- opening shell sessions
- sending or receiving files
- direct HAP install or uninstall
- live device logs and basic transport

Read:
- `references/official-build-deploy-sources.md` section `hdc`

### `bm`

Use for:
- installing or uninstalling from inside `hdc shell`
- querying installed bundles
- checking bundle state after install

Important:
- official docs explicitly require entering `hdc shell` first
- `bm install` uses device-side paths, not host-side paths

Read:
- `references/official-build-deploy-sources.md` section `bm`

### `aa`

Use for:
- launching a UIAbility or service
- stopping service abilities or extension abilities
- attach or wait-for-debug flows
- startup timing and basic launch diagnostics

Important:
- official docs also treat `aa` as a shell tool; when running through `hdc shell`, quote the full command

Read:
- `references/official-build-deploy-sources.md` section `aa`

### `packing-tool`

Use for:
- packaging DevEco build outputs into HAP, HSP, or APP
- multi-HAP or multi-project APP packaging
- understanding packaging-time validation rules

Important:
- package inputs come from DevEco build artifacts
- do not invent file paths; inspect the project's real outputs or the build logs

Read:
- `references/official-build-deploy-sources.md` section `packing-tool`

### `binary-sign-tool`

Use for:
- signing ELF binaries
- checking native code signature metadata

Important:
- this is not the general HAP signing workflow
- use it only when the task specifically concerns binary signing of ELF artifacts

Read:
- `references/official-build-deploy-sources.md` section `binary-sign-tool`

### Build path resolution

Use for:
- locating the SDK root before build or packaging commands
- deciding whether to use a repository-local `hvigorw` or a DevEco-installed wrapper
- distinguishing app-module builds from `ohosTest` builds

Important:
- official docs confirm that command-line tools are obtained from the SDK embedded in DevEco Studio or from Command Line Tools
- treat `DEVECO_SDK_HOME` as a preferred local convention when present, but not as an official universal requirement
- on macOS, Windows, and Linux, DevEco installation roots differ, so never hardcode one OS path as the only answer
- if the repository already provides a working `hvigorw` command, keep it
- if the repository has separate `entry@default` and `entry@ohosTest` targets, choose the one that matches the requested artifact

Read:
- `references/official-build-deploy-sources.md` section `SDK and build-path resolution`

## Response Rules

- Prefer the repository's existing DevEco or `hvigorw` build command when a project already defines one.
- Resolve the SDK root first: prefer `DEVECO_SDK_HOME`, otherwise inspect repo commands, `PATH`, or OS-appropriate DevEco install locations.
- Use official tool names and official argument patterns from local docs.
- Be explicit about host-side path versus device-side path.
- When install, launch, or build depends on bundle name, module name, target, product, or ability name, derive them from the project before giving commands.
- If the user wants troubleshooting, identify the failing stage first:
  - SDK discovery or path resolution
  - toolchain discovery
  - device connection
  - build output generation
  - packaging
  - install
  - launch
  - runtime logs
- Treat `HARMONYOS_DOCS_ROOT` as valid when it points either to the docs repository root or directly to its `zh-cn/` subtree
- If `HARMONYOS_DOCS_ROOT` is missing or invalid, search `https://developer.huawei.com/consumer/cn/doc/` before falling back to generic advice

## When To Load Extra Context

- Load `references/official-build-deploy-sources.md` first for all tasks.
- If the user wants concrete day-to-day commands for build, install, launch, logs, or packaging, use the `Common command patterns` section in `references/official-build-deploy-sources.md`.
- If the user asks about project structure, generated outputs, HAP composition, or single-HAP vs multi-HAP tradeoffs, also inspect the local quick-start docs referenced there.
- If the request is about the current repository, inspect the repo's actual build scripts and AGENTS instructions after the official docs, then adapt the command sequence to the repo instead of replacing it.
- If the request is about `aa test`, `ohosTest`, `testRunner`, or HarmonyOS Test Kit wiring, hand off to `$harmonyos-test-kit` for test-framework specifics and keep this skill focused on the underlying build and device toolchain.

## Boundaries

- Do not turn this skill into a generic HarmonyOS project architecture guide. For project scaffolding or app completion, use `$harmonyos-project-builder`.
- Do not use this skill for ArkTS V2 state-management or UI semantics. For that, use `$harmonyos-arkts-v2-assistant`.
- Do not assume that a third-party deploy wrapper is authoritative just because it exists. The baseline should remain the local official docs and the repo's existing DevEco workflow.

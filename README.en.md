# HarmonyOS Programming Skills

Chinese version: [README.md](./README.md)  
English version: this file

This repository bundles four reusable HarmonyOS programming skills:

- `harmonyos-project-builder`
- `harmonyos-sdk-build-deploy`
- `harmonyos-arkts-v2-assistant`
- `harmonyos-test-kit`

They are designed to work together for HarmonyOS and OpenHarmony application development, covering project setup, official SDK build and deploy workflows, ArkTS authoring guidance, and official Test Kit testing workflows.

## Included skills

### `harmonyos-project-builder`

Use when an empty or partial HarmonyOS project needs to become a complete working application.

Focus:

- project scaffolding
- directory layout
- DevEco and hvigor structure
- architecture and boundaries
- staged verification

### `harmonyos-sdk-build-deploy`

Use when official HarmonyOS SDK toolchain workflows are needed for:

- build
- package
- install
- launch
- logs
- signing
- device debug

Focus:

- `hdc`
- `bm`
- `aa`
- `packing-tool`
- `binary-sign-tool`

### `harmonyos-arkts-v2-assistant`

Use when ArkTS or `.ets` authoring guidance is needed.

Focus:

- ArkUI V2
- ArkUI V1 maintenance
- ArkTS versus TypeScript compatibility
- `.ets` authoring patterns
- MVVM and component boundaries

### `harmonyos-test-kit`

Use when official HarmonyOS Test Kit workflows are needed.

Focus:

- `@ohos/hypium` unit tests
- `@kit.TestKit` / `@ohos.UiTest` UI tests
- `PerfTest` white-box performance tests
- `ohosTest` / `testRunner` / `module.json5` wiring
- `aa test` execution and filtering

## Environment variables

These skills do not rely on hardcoded local paths.

Set these variables in your shell startup config, then restart your coding assistant:

```sh
export HARMONYOS_DOCS_ROOT="/path/to/docs-repo-or-zh-cn"
export HARMONYOS_SAMPLES_ROOT="/path/to/applications_app_samples"
```

Example:

```sh
export HARMONYOS_DOCS_ROOT="$HOME/playground/docs"
export HARMONYOS_SAMPLES_ROOT="$HOME/playground/applications_app_samples"
```

Rules:

- `HARMONYOS_DOCS_ROOT` may point either to the docs repository root or directly to its `zh-cn/` subtree
- `HARMONYOS_SAMPLES_ROOT` should point to the `applications_app_samples` repository root
- if local docs are unavailable, the skills fall back to the official HarmonyOS documentation site
- if local samples are unavailable, the skills still cover core workflows and only require samples when a task genuinely depends on sample inspection

## Using the skills

Copy or sync these directories into the skills directory used by your coding assistant:

- `harmonyos-project-builder/`
- `harmonyos-sdk-build-deploy/`
- `harmonyos-arkts-v2-assistant/`
- `harmonyos-test-kit/`

If your environment uses a central skills directory such as `$CODEX_HOME/skills`, place these skill folders there directly.

## Why one repository

These four skills share:

- cross-references between skills
- the same environment-variable contract
- a single HarmonyOS development workflow surface

Keeping them together avoids version drift between project architecture guidance, SDK build and deploy guidance, ArkTS authoring guidance, and testing guidance.

---
name: harmonyos-project-builder
description: Use when Codex needs to turn an empty or partial HarmonyOS/OpenHarmony project into a complete working application. Covers project scaffolding, directory layout, DevEco configuration, ArkTS UI architecture, state-management choices, service and ability boundaries, native or runtime integration, build and deploy workflow, and staged verification. Trigger on requests to build a HarmonyOS app from scratch, scaffold a project, complete an unfinished app, set up DevEco or hvigor structure, add VPN or extension abilities, wire native code, or define a project architecture and delivery plan.
---

# HarmonyOS Project Builder

## Overview

Build HarmonyOS projects in phases. Do not jump straight into feature code from an empty repository. Establish the project shape, configuration, architecture, runtime boundaries, and verification flow first, then implement features incrementally.

Use official HarmonyOS docs and samples before inventing structure. Prefer local copies discovered through `HARMONYOS_DOCS_ROOT` and `HARMONYOS_SAMPLES_ROOT`. If docs are unavailable locally, fall back to searching the official HarmonyOS documentation site at `https://developer.huawei.com/consumer/cn/doc/`. Read [references/project-blueprint.md](references/project-blueprint.md) for the target project shape, [references/system-client-pattern.md](references/system-client-pattern.md) for VPN or runtime-heavy apps, and [references/verification-checklist.md](references/verification-checklist.md) for the staged completion criteria.

For official SDK toolchain details such as `hdc`, `bm`, `aa`, packaging, signing, and device-side deploy flows, use `$harmonyos-sdk-build-deploy`. This skill should decide when build and deploy verification is required, not restate the full command-line tool reference.

When the task is true scaffolding, use `scripts/scaffold_harmonyos_layout.py` to create the base directory layout before adding feature code.

## Source Priority

Consult sources in this order:

1. Repository `AGENTS.md` and existing project files
2. Local official docs discovered from `HARMONYOS_DOCS_ROOT`
3. Local official samples discovered from `HARMONYOS_SAMPLES_ROOT`
4. Official HarmonyOS documentation site `https://developer.huawei.com/consumer/cn/doc/` when local docs are unavailable or invalid
5. General HarmonyOS knowledge only when the sources above do not answer the question

Never assume a generic HarmonyOS layout is correct if the repository already defines one.

Treat `HARMONYOS_DOCS_ROOT` as valid when it points either to the docs repository root or directly to its `zh-cn/` subtree. Treat `HARMONYOS_SAMPLES_ROOT` as valid when it points to the `applications_app_samples` repository root. If either environment variable is missing or invalid, continue with the remaining sources instead of failing immediately.

## Workflow

### 1. Determine the project class

Classify the target before creating files:

- Simple ArkTS UI app
- Multi-page app with shared state
- App with background or extension abilities
- App with native bridge or runtime wrapper
- VPN or networking client
- Existing repo that needs completion rather than fresh scaffolding

If the repository already has structure, extend it. Do not rebuild it around a different architecture unless the user explicitly asks for a redesign.

### 2. Establish the minimum working skeleton

Before feature work, ensure the project has:

- App and module config files
- A valid entry module
- Main pages routing
- Base resource structure
- A buildable hvigor configuration
- A clear ArkTS source layout

Prefer a layout that separates:

- `pages/` for composition and page entry
- `viewmodel/` for UI-facing state transitions
- `service/` for orchestration, IO, bridge, persistence, and events
- `model/` for observed UI models and plain DTOs
- `vpn/`, `extension/`, `native/`, or runtime folders when the app actually needs them

If the repository is still missing these directories, prefer creating them with `scripts/scaffold_harmonyos_layout.py` instead of rebuilding the same folder tree by hand.

### 3. Pick the UI architecture early

For new UI work, default to ArkUI V2:

- `@ComponentV2`
- `@ObservedV2`
- `@Trace`
- `@Local`
- `@Param`
- `@Event`
- `@LocalBuilder` when local composition is necessary

Keep pages thin. Put runtime coordination and nontrivial state transitions into viewmodels or services.

If the app is expected to grow beyond one page or one form, use MVVM-style separation from the start instead of waiting for later cleanup.

### 4. Define system boundaries before integration

When the project involves platform or native capabilities, define the boundary explicitly:

- UI-observed state stays in UI and ViewModel layers
- Cross-process, persistence, event-bus, bridge, and native boundaries use plain DTOs
- Native, runtime, or Go wrappers do not receive observed UI objects directly
- Abilities and extensions expose a clear contract to services or viewmodels

Do not patch over boundary issues with JSON deep copies, ad hoc listeners, or duplicated state fields.

### 5. Build feature slices, not disconnected files

Implement one end-to-end slice at a time:

1. Data model or DTO
2. Service or integration logic
3. ViewModel
4. UI composition
5. Verification

Complete one slice before starting the next, unless the user explicitly wants scaffolding only.

### 6. Verify by stage

Use staged verification:

- Config and compile validation first
- Runtime startup next
- Feature-path verification after that
- Device deployment last when needed

Do not claim the project is complete only because files exist. Completion requires passing the relevant checks in [references/verification-checklist.md](references/verification-checklist.md).

## Phase Gates

### Phase 1: Skeleton

Exit this phase only when:

- The directory structure is coherent
- Build config files are present and internally consistent
- Entry pages or abilities are wired
- Resources and routing are minimally usable

### Phase 2: Architecture

Exit this phase only when:

- Page, ViewModel, service, and model responsibilities are clear
- V1 versus V2 state-management choice is explicit
- Native or extension boundaries are defined when applicable

### Phase 3: Functional slices

Exit this phase only when:

- Each user-visible flow has all required layers wired together
- Persistence, import, logging, or background support is attached where needed
- Error paths have at least basic handling

### Phase 4: Delivery readiness

Exit this phase only when:

- The project builds with the repository's real commands
- Required device or runtime checks pass
- Known risks or unimplemented areas are called out explicitly

## Decision Rules

### Architecture

- Prefer one project-wide structure over per-feature improvisation
- If the repository already contains `pages`, `viewmodel`, `service`, and `model`, keep that pattern
- Split runtime-facing orchestration out of UI structs as soon as it becomes stateful or asynchronous

### State management

- Default to V2 for new code
- Avoid mixing V1 and V2 casually
- Treat `@LocalBuilder` parameter passing as a refresh-risk area
- Do not serialize observed objects across boundaries

### Project setup

- Use DevEco and hvigor directly unless the repository explicitly uses another wrapper
- Read existing `build-profile.json5`, `app.json5`, `module.json5`, and `hvigorfile.ts` before changing build commands
- Match existing products, modules, and build modes
- For official SDK build, install, launch, packaging, signing, and log workflows, defer to `$harmonyos-sdk-build-deploy`

### Native or runtime integration

- Introduce a narrow service boundary between UI/ViewModel and native/runtime code
- Keep start, stop, status, logs, and selector updates as explicit flows
- Prefer DTO mapping rather than leaking internal runtime models upward

## Typical Build-Out Patterns

### Empty project to basic app

Do this in order:

1. Create config and routing skeleton
2. Add one landing page
3. Add one ViewModel-backed interaction
4. Confirm buildability

### Basic app to complete multi-page app

Do this in order:

1. Move shared state into viewmodels or services
2. Split reusable views from page composition
3. Add persistence or app-wide state
4. Add verification for page transitions and state restoration

### App to system-capability client

Do this in order:

1. Define the capability boundary and permissions
2. Add the required ability, extension, or bridge layer
3. Wire service APIs to ViewModel state
4. Add logs, status, and failure reporting
5. Verify on device when the capability requires it

For VPN, native bridge, or runtime-wrapper apps, also read [references/system-client-pattern.md](references/system-client-pattern.md).

## Verification

Use the repository's real commands rather than generic placeholders.

When the repository provides build and deploy instructions in `AGENTS.md`, follow those. When it does not, inspect the existing hvigor and module configuration first, then use `$harmonyos-sdk-build-deploy` to choose the correct official SDK path for compile, package, install, launch, or device-debug work.

For complex projects, report verification in three buckets:

- Build status
- Runtime or device status
- Remaining risks

Keep this skill focused on whether the project has reached the required verification stage. Keep detailed SDK tool selection and command guidance in `$harmonyos-sdk-build-deploy`.

## Output Style

When using this skill:

- State the current phase and the next phase
- Make architecture choices explicit instead of implying them
- Prefer small, complete slices over long speculative plans
- When blocked, identify the missing project fact instead of inventing one

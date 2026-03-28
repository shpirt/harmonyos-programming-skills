---
name: harmonyos-project-builder
description: Use when Codex needs to turn an empty or partial HarmonyOS/OpenHarmony project into a complete working application. Covers official Stage-model project setup, directory layout, DevEco configuration, ArkTS UI architecture, state-management choices, ability and native integration boundaries, and staged verification. Trigger on requests to build a HarmonyOS app from scratch, scaffold a project, complete an unfinished app, set up DevEco or hvigor structure, add abilities or native integration, or define a project architecture and delivery plan.
---

# HarmonyOS Project Builder

## Overview

Build HarmonyOS projects in phases. Do not jump straight into feature code from an empty repository. Establish the official Stage-model project shape, configuration, runtime boundaries, and verification flow first, then implement features incrementally.

Use official HarmonyOS docs and official samples before inventing structure. Prefer local copies discovered through `HARMONYOS_DOCS_ROOT` and `HARMONYOS_SAMPLES_ROOT`. If docs are unavailable locally, fall back to searching the official HarmonyOS documentation site at `https://developer.huawei.com/consumer/cn/doc/`.

Read [references/project-blueprint.md](references/project-blueprint.md) for the official build-first project shape, [references/system-client-pattern.md](references/system-client-pattern.md) for optional layering patterns that appear in official MVVM or system-capability samples, and [references/verification-checklist.md](references/verification-checklist.md) for staged completion criteria.

For official SDK toolchain details such as `hdc`, `bm`, `aa`, packaging, signing, and device-side deploy flows, use `$harmonyos-sdk-build-deploy`. This skill should decide when build and deploy verification is required, not restate the full command-line tool reference.

When the task is true scaffolding, use `scripts/scaffold_harmonyos_layout.py` only after aligning the target layout with official docs or official sample structure.

## Source Priority

Consult sources in this order:

1. Local official docs discovered from `HARMONYOS_DOCS_ROOT`
2. Local official samples discovered from `HARMONYOS_SAMPLES_ROOT`
3. Official HarmonyOS documentation site `https://developer.huawei.com/consumer/cn/doc/` when local docs are unavailable or invalid
4. Repository `AGENTS.md` and existing project files
5. General HarmonyOS knowledge only when the sources above do not answer the question

Treat `HARMONYOS_DOCS_ROOT` as valid when it points either to the docs repository root or directly to its `zh-cn/` subtree. Treat `HARMONYOS_SAMPLES_ROOT` as valid when it points to the `applications_app_samples` repository root. If either environment variable is missing or invalid, continue with the remaining sources instead of failing immediately.

Do not use the current repository as the default architecture template for new projects. Use the repository only to extend or preserve an already existing codebase.

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

### 2. Establish the official minimum working skeleton

Before feature work, ensure the project has the official Stage-model build-first structure:

- `AppScope/app.json5`
- root `build-profile.json5`
- root `hvigorfile.ts`
- module `build-profile.json5`
- module `hvigorfile.ts`
- `entry/src/main/module.json5`
- `entry/src/main/ets/entryability`
- `entry/src/main/ets/pages`
- `entry/src/main/resources`
- page routing config under `resources/base/profile/`

These items come from official docs and default Stage-model project generation. Treat them as the baseline before introducing extra engineering layers.

### 3. Add only the engineering layers the project actually needs

After the official skeleton is in place, inspect official samples relevant to the target complexity.

For example, the official `StateMgmtV2MVVM` sample uses this shape under `entry/src/main/ets/`:

```text
entry/src/main/ets/
  entryability/
  model/
  pages/
  settingability/
  view/
  viewmodel/
```

Treat that as a valid official MVVM-style sample pattern for larger ArkTS apps. In that pattern:

- `pages/` holds page entry and composition
- `view/` holds reusable presentational sections
- `viewmodel/` holds UI-facing state transitions
- `model/` holds UI-facing models
- additional ability folders such as `settingability/` are added only when the sample or feature set needs them

For system-capability or runtime-heavy apps, add only the extra implementation layers that the selected official sample pattern, required ability type, or native integration actually forces you to introduce. Common examples are:

- `service/` when orchestration, persistence, import, or bridge coordination no longer fits cleanly in page or ViewModel code
- ability-specific source folders only when the app really adds another ability or extension beyond `entryability/`
- `bridge/` or native-facing folders only when native integration is present

Do not pre-create project-specific folders in a generic scaffolding flow. Add source folders only when a concrete ability, integration boundary, or official sample pattern requires them.

### 4. Pick the UI architecture early

For new UI work, default to ArkUI V2:

- `@ComponentV2`
- `@ObservedV2`
- `@Trace`
- `@Local`
- `@Param`
- `@Event`
- `@LocalBuilder` when local composition is necessary

Keep pages focused on entry and composition. If the app grows beyond simple page logic, use official MVVM-style sample patterns before inventing a custom split.

### 5. Define system boundaries before integration

When the project involves platform or native capabilities, define the boundary explicitly:

- UI-observed state stays in UI or ViewModel layers
- Cross-process, persistence, event-bus, bridge, and native boundaries use plain DTOs
- Native, runtime, or Go wrappers do not receive observed UI objects directly
- Abilities and extensions expose a clear contract to services or UI-facing coordinators

Do not patch over boundary issues with JSON deep copies, ad hoc listeners, or duplicated state fields.

### 6. Build feature slices, not disconnected files

Implement one end-to-end slice at a time:

1. Data model or DTO
2. Service or integration logic when needed
3. ViewModel or UI-facing coordination when needed
4. UI composition
5. Verification

Complete one slice before starting the next, unless the user explicitly wants scaffolding only.

### 7. Verify by stage

Use staged verification:

- Config and compile validation first
- Runtime startup next
- Feature-path verification after that
- Device deployment last when needed

Do not claim the project is complete only because files exist. Completion requires passing the relevant checks in [references/verification-checklist.md](references/verification-checklist.md).

## Phase Gates

### Phase 1: Skeleton

Exit this phase only when:

- The official Stage-model project shape is coherent
- Build config files are present and internally consistent
- Entry ability, pages, resources, and routing are minimally usable

### Phase 2: Architecture

Exit this phase only when:

- UI, ViewModel, service, and model responsibilities are clear where those layers exist
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

- Default to the official Stage-model project skeleton for empty projects
- Introduce extra folders only when official samples, required ability types, or real project complexity justify them
- If the repository already contains a coherent internal folder split, keep that pattern unless a redesign is explicitly requested
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

- Introduce a narrow service or bridge boundary between UI-facing layers and native/runtime code
- Keep start, stop, status, logs, and selector updates as explicit flows
- Prefer DTO mapping rather than leaking internal runtime models upward

## Typical Build-Out Patterns

### Empty project to basic app

Do this in order:

1. Create the official Stage-model skeleton and routing config
2. Add one landing page under `pages/`
3. Add one interaction using the lightest necessary state pattern
4. Confirm buildability

### Basic app to structured ArkTS app

Do this in order:

1. Keep entry ability, pages, and resources aligned with the official layout
2. Add `view/` or `views/`, `viewmodel/`, or `model/` only if official sample patterns match the target complexity
3. Add persistence or app-wide state only when the feature set requires it
4. Add verification for page transitions and state restoration

### App to system-capability client

Do this in order:

1. Define the capability boundary and permissions
2. Add only the required ability implementation, extension source set, or bridge layer
3. Wire service APIs to UI-facing state
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
- Explicitly say when a layer is required by official project shape versus added as an optional engineering layer
- Prefer small, complete slices over long speculative plans
- When blocked, identify the missing official or project fact instead of inventing one

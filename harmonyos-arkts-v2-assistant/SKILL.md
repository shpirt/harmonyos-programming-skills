---
name: harmonyos-arkts-v2-assistant
description: Use for HarmonyOS/OpenHarmony ArkTS code work when Codex needs official documentation and samples to answer `.ets` syntax, state management, component semantics, migration, compile-error, API-usage, or legacy ArkUI maintenance questions. Trigger on `.ets` files, ArkTS decorators, `@kit` or `@ohos` APIs, HarmonyOS/OpenHarmony context, `@ComponentV2`, `@ObservedV2`, `@Trace`, `@Local`, `@Param`, `@Event`, `@LocalBuilder`, `@State`, `@Prop`, `@Link`, `@Provide`, `@Consume`, `@StorageLink`, `@StorageProp`, `@Watch`, or when V1/V2 state-management choices are relevant inside code.
---

# HarmonyOS ArkTS V2 Assistant

## Overview

Use official HarmonyOS documentation and sample projects before relying on memory. Prefer local copies discovered through `HARMONYOS_DOCS_ROOT` and `HARMONYOS_SAMPLES_ROOT`. If docs are unavailable locally, fall back to searching the official HarmonyOS documentation site at `https://developer.huawei.com/consumer/cn/doc/`. Treat this skill as a decision guide for ArkTS syntax and ArkUI state-management work, with V2 as the default path for new code.

Read [references/local-harmonyos-sources.md](references/local-harmonyos-sources.md) when you need exact local doc paths or sample locations.
Read [references/legacy-v1-maintenance.md](references/legacy-v1-maintenance.md) when the target is an older ArkUI V1 codebase or the request mentions classic V1 decorators.
Read [references/arkts-vs-ts.md](references/arkts-vs-ts.md) when the problem is really a TypeScript-to-ArkTS compatibility issue rather than a state-management issue.
Read [references/ets-authoring-patterns.md](references/ets-authoring-patterns.md) when the task is about everyday `.ets` authoring patterns such as list rendering, conditional UI, builders, dialog usage, navigation, gestures, animation, or `.ets` versus `.ts` file boundaries.

For empty-project scaffolding, project completion, directory layout, ability boundaries, or staged delivery planning, use `$harmonyos-project-builder`. For official SDK build, install, launch, packaging, signing, and device-debug workflows, use `$harmonyos-sdk-build-deploy`.

## Source Priority

Consult sources in this order:

1. Local official docs discovered from `HARMONYOS_DOCS_ROOT`
2. Local official samples discovered from `HARMONYOS_SAMPLES_ROOT`
3. The official HarmonyOS documentation site `https://developer.huawei.com/consumer/cn/doc/` when local docs are unavailable or invalid
4. The current repository's code and build instructions
5. General ArkTS knowledge only when the sources above do not answer the question

Prefer citing the local doc path or sample path you used.

Treat `HARMONYOS_DOCS_ROOT` as valid when it points either to the docs repository root or directly to its `zh-cn/` subtree. Treat `HARMONYOS_SAMPLES_ROOT` as valid when it points to the `applications_app_samples` repository root. If local docs or samples are missing, continue with the remaining sources instead of failing; only ask the user to clone or point to local repositories when the task genuinely needs offline docs or sample inspection.

## Workflow

### 1. Classify the request

Put the task into one primary bucket:

- Syntax or compile error
- ArkTS vs TypeScript syntax compatibility
- ArkUI state management
- Legacy ArkUI V1 maintenance
- `.ets` authoring patterns and file boundaries
- Component split or MVVM architecture
- Migration from TS, JS, or ArkUI V1 to V2
- API usage for `@kit` or `@ohos`
- Performance or rendering refresh bug

### 2. Pick the right source first

- For V2 state-management or component-boundary questions, open:
  - `application-dev/ui/state-management/arkts-state-management-overview.md`
  - `application-dev/ui/state-management/arkts-mvvm-v2.md`
  - `application-dev/ui/state-management/arkts-new-local.md`
  - `application-dev/ui/state-management/arkts-localBuilder.md`
- For coding style or error-handling examples, open:
  - `application-dev/quick-start/arkts-coding-style-guide.md`
  - `contribute/style-guide/style-guide-example-code-style.md`
- For ArkTS vs TypeScript compatibility questions, open:
  - `application-dev/quick-start/arkts-migration-background.md`
  - `application-dev/quick-start/typescript-to-arkts-migration-guide.md`
  - `application-dev/faqs/faqs-arkui-arkts.md`
- For app-model questions such as `globalThis` and `Context`, open:
  - `application-dev/faqs/faqs-ability.md`
- For `.ets` authoring patterns and file-boundary questions, open:
  - `references/ets-authoring-patterns.md`
- For implementation patterns, find the closest sample under:
  - `code/DocsSample/ArkUISample/StateMgmtV2MVVM`
  - `code/DocsSample/ArkUISample/ParadigmStateManagement`
- For legacy ArkUI V1 maintenance, open:
  - `references/legacy-v1-maintenance.md`
- For TypeScript habit conflicts in `.ets` files, open:
  - `references/arkts-vs-ts.md`

Resolve those relative paths against `HARMONYOS_DOCS_ROOT` and `HARMONYOS_SAMPLES_ROOT` when local copies exist. If docs are missing locally, search the official site for the same document title or topic before falling back to generic advice. If samples are missing locally, proceed without them unless the task specifically depends on sample inspection.

### 3. Default to V2 for new code

For new HarmonyOS UI work:

- Prefer `@ComponentV2`
- Prefer `@ObservedV2` plus `@Trace` for observable models
- Prefer `@Local` for internal component state
- Prefer `@Param` for input
- Prefer `@Event` for output
- Prefer MVVM-style separation when the component is coordinating runtime or business state

Only preserve V1 patterns when one of these is true:

- The target code already uses V1 throughout and the user asked for a narrow fix
- A required API or surrounding component still depends on V1 behavior
- Migrating to V2 would materially increase scope beyond the user request

When you keep V1, say so explicitly and avoid mixing V1 and V2 casually.

### 3a. Legacy V1 maintenance mode

When the target file or feature already uses ArkUI V1 decorators such as `@State`, `@Prop`, `@Link`, `@Provide`, `@Consume`, `@StorageLink`, `@StorageProp`, or `@Watch`, treat the task as V1 maintenance unless the user explicitly asks for migration.

In V1 maintenance mode:

- keep fixes inside the existing V1 model unless the current change genuinely requires migration
- do not introduce `@ComponentV2`, `@ObservedV2`, `@Local`, `@Param`, or `@Event` into a narrow V1 fix
- explain the answer as `V1-compatible` rather than `V2-first`
- call out when the problem is a V1 limitation instead of hiding it behind a partial V2 rewrite
- only propose migration as a second option when it materially improves correctness or maintainability

### 4. Answer with repository-safe guidance

When suggesting code:

- Match the repository's existing architecture and decorators
- Keep page components focused on composition
- Move runtime coordination and state transitions into ViewModel or service layers when the codebase already follows that split
- Verify whether a refresh issue is a state-observation problem before proposing copied state or manual sync
- Keep UI composition and ArkUI-specific declarations in `.ets`; keep plain helper logic, DTOs, and non-UI utilities in `.ts` when the repository already follows that split

## Decision Rules

### State management

- Recommend V2 for new code unless there is a strong compatibility reason not to
- Use `@Local` only for internal state that must not be initialized externally
- Use `@Param @Once` only when the child needs one-time initialization and local mutation afterward
- Use `@Event` instead of recreating V1-style implicit two-way flows
- Use `@ObservedV2` and `@Trace` when nested object properties must trigger refresh
- In legacy V1 code, keep `@State`, `@Prop`, `@Link`, `@Provide`, `@Consume`, `@StorageLink`, `@StorageProp`, and `@Watch` semantics coherent instead of mixing in V2 replacements ad hoc
- For nested refresh issues in V1, check whether the real problem is missing `@Observed` or `@ObjectLink`, not a need to jump straight to V2

### `@LocalBuilder`

Treat `@LocalBuilder` as a common refresh trap.

- Prefer no-arg `@LocalBuilder` functions that read state through `this`
- Do not assume value-passed parameters in `@LocalBuilder` will refresh the way ordinary component reads do
- When diagnosing a refresh bug, compare the failing builder with direct reads in the component body
- If the issue involves cross-component builder passing, check whether the problem is parent-child ownership rather than plain syntax

### `globalThis` and `Context`

- Do not recommend `globalThis` to obtain `Context` in Stage-model code
- Prefer the official `UIAbility` and UI data-sync patterns from local docs
- Treat singleton replacements as application-specific, not the default official answer

### Error handling

- For Promise-based APIs, prefer `.catch((err: BusinessError) => ...)` when that matches official examples
- For `try/catch`, use `catch (error)` and cast inside the block, such as `const err: BusinessError = error as BusinessError`
- Prefer examples aligned with local official style guides rather than generic TypeScript advice

## Typical Tasks

### Syntax or compile errors

Read the error text, locate the relevant local ArkTS rule, and answer with:

1. The exact incompatible pattern
2. The HarmonyOS-preferred replacement
3. A minimal corrected example
4. The local doc path or sample path used

### ArkTS vs TypeScript syntax compatibility

When the code looks valid in ordinary TypeScript but fails in `.ets` or ArkTS:

1. Identify the TypeScript habit or feature being used
2. Explain whether ArkTS disallows it outright or narrows the allowed form
3. Replace it with the HarmonyOS-preferred ArkTS form
4. Keep the example minimal and valid in the surrounding ArkUI context
5. Cite the migration guide, ArkTS FAQ, or local source used

### Legacy ArkUI V1 maintenance

When the request is about an older V1 page or component:

1. Identify the active V1 decorators and ownership model
2. Keep the immediate fix in V1 unless the user asked for migration
3. Check parent-child sync, storage decorators, and nested observation before proposing structural rewrites
4. Mention if the issue is a known V1 limitation or decorator misuse
5. Offer migration to V2 only as a separate follow-up path

### V1 to V2 migration

Map the existing code to V2 concepts:

- `@Component` -> `@ComponentV2`
- `@State` internal state -> `@Local`
- `@Prop` -> `@Param`
- `@Link` -> explicit `@Param` plus `@Event`
- `@Observed` or `@ObjectLink` cases -> review whether `@ObservedV2` plus `@Trace` is the proper replacement

Call out places where migration changes semantics, especially child mutation, nested observation, and storage behavior.

### MVVM or component decomposition

Use the local MVVM V2 docs and samples when the task involves:

- Splitting a large page
- Moving logic out of the UI struct
- Introducing models or viewmodels
- Reusing stateful child components

Prefer examples modeled after `StateMgmtV2MVVM` sample structure. That official sample organizes `entry/src/main/ets/` with `entryability/`, `pages/`, `view/`, `viewmodel/`, `model/`, and `settingability/`; when guiding `.ets` work, preserve or extend that official sample layout instead of inventing a repo-specific split.

### `.ets` authoring patterns

When the request is about writing or restructuring everyday `.ets` code:

1. decide whether the issue is rendering control, builder usage, navigation, dialog, gesture, animation, or file-boundary placement
2. keep ArkUI-specific composition in `.ets`
3. keep plain utilities, transport types, and non-UI helpers in `.ts` unless the surrounding codebase already does otherwise
4. prefer the smallest idiomatic ArkUI pattern instead of inventing framework-like abstractions
5. cite the local doc or sample path used

## Verification

Do not impose a fixed build script for every HarmonyOS project.

Before compiling:

- Read the target repository's `AGENTS.md`, build docs, and existing hvigor usage
- Use the project's real build command instead of a generic `assembleApp` assumption
- If no build is requested and the task is documentation-only, do not force compilation

When you change code, prefer the lightest valid verification for the repository:

- ArkTS compile or hvigor build first
- Device or runtime verification only when the task requires it

## Output Style

When answering with this skill:

- Lead with the recommended HarmonyOS-specific approach
- Mention whether the answer is V2-first, V1-compatible, or migration-specific
- For syntax-compatibility questions, explicitly distinguish `TypeScript habit` from `ArkTS-allowed form`
- For `.ets` authoring questions, explicitly distinguish `UI composition in .ets` from `plain logic in .ts` when relevant
- Include one small corrected code example instead of a long tutorial unless the user asked for depth
- Name the local doc path or sample path that justifies the recommendation

## Boundaries

- Keep this skill focused on ArkTS, ArkUI V2, state-management, decorator choice, component boundaries, migration, and refresh behavior
- Do not turn this skill into a project scaffolding or delivery-planning guide; use `$harmonyos-project-builder` for that
- Do not turn this skill into an SDK command-line deployment guide; use `$harmonyos-sdk-build-deploy` for that
- Do not treat every V1 issue as an automatic migration task; support narrow V1 maintenance when the repository is still on V1

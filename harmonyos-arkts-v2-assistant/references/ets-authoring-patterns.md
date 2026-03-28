# `.ets` Authoring Patterns

Use this reference for day-to-day HarmonyOS `.ets` authoring questions that are not primarily about V1/V2 migration.

## Use this reference for

- conditional rendering
- `ForEach` or `LazyForEach`
- `@Builder` or `@LocalBuilder`
- dialogs and prompt-style UI
- navigation and page composition
- gestures and event handling
- animation patterns
- deciding whether code belongs in `.ets` or `.ts`

## File-boundary guidance

Prefer this split unless the repository already uses a different structure:

- `.ets`: ArkUI components, page composition, decorators, builders, rendering logic, UI event wiring
- `.ts`: plain helper functions, DTOs, pure domain logic, parsing helpers, constants, non-UI utilities

If a file needs ArkUI decorators, UI structs, or builder syntax, it belongs in `.ets`.

If a file is just data transformation or utility logic with no ArkUI syntax, it usually belongs in `.ts`.

## High-value doc entry points

Look under `HARMONYOS_DOCS_ROOT` first, then search the official docs site if local docs are unavailable:

- `application-dev/ui/rendering-control/arkts-rendering-control-ifelse.md`
- `application-dev/ui/rendering-control/arkts-rendering-control-foreach.md`
- `application-dev/ui/state-management/arkts-builder.md`
- `application-dev/ui/state-management/arkts-localBuilder.md`
- `application-dev/reference/apis-as/js-apis-promptAction.md`
- `application-dev/reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md`
- `application-dev/reference/apis-arkui/arkui-ts/ts-methods-custom-dialog-box.md`
- `application-dev/reference/apis-arkui/arkui-ts/ts-explicit-animation.md`

## Pattern guidance

### Rendering control

- use straightforward conditional rendering for simple branches
- use `ForEach` with stable keys for repeated UI
- when data is large or incremental, check whether `LazyForEach` is more appropriate

### Builder usage

- use `@Builder` for reusable UI construction where parameter passing is intentional
- use `@LocalBuilder` for local component composition that should read the current component state
- if refresh behavior is wrong, check whether the builder is reading stale passed values instead of `this`

### Dialogs

- use the documented dialog or prompt APIs rather than custom ad hoc overlays unless the design genuinely requires it
- keep dialog state ownership clear: opener, confirm path, cancel path

### Navigation

- keep navigation structure at page or container level
- avoid mixing routing decisions deep inside leaf components when a page-level coordinator can own them

### Gestures and animations

- keep gesture handlers close to the rendered element they affect
- keep animation state explicit instead of hiding it behind unrelated helper layers

## Output guidance

When answering `.ets` authoring questions:

- say what pattern category the issue belongs to
- show the smallest idiomatic ArkUI form
- mention if the real fix is about file placement rather than syntax

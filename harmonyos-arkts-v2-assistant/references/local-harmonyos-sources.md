# Local HarmonyOS Sources

Use these sources before relying on general ArkTS memory.

## Environment variables

- `HARMONYOS_DOCS_ROOT`
- `HARMONYOS_SAMPLES_ROOT`

Resolve paths as follows:

- `HARMONYOS_DOCS_ROOT` may point either to the docs repository root or directly to its `zh-cn/` subtree
- `HARMONYOS_SAMPLES_ROOT` should point to the `applications_app_samples` repository root
- if `HARMONYOS_DOCS_ROOT` is missing or invalid, search `https://developer.huawei.com/consumer/cn/doc/` by document title or topic
- if `HARMONYOS_SAMPLES_ROOT` is missing or invalid, continue without local samples unless the task specifically requires sample inspection

## Docs paths relative to `HARMONYOS_DOCS_ROOT`

## State-management docs

- `application-dev/ui/state-management/arkts-state-management-overview.md`
- `application-dev/ui/state-management/arkts-mvvm-v2.md`
- `application-dev/ui/state-management/arkts-new-local.md`
- `application-dev/ui/state-management/arkts-localBuilder.md`

Use these for:

- V1 vs V2 choice
- `@ComponentV2`, `@ObservedV2`, `@Trace`, `@Local`, `@Param`, `@Event`
- MVVM layout and component boundaries
- `@LocalBuilder` refresh and ownership behavior

## App-model and FAQ docs

- `application-dev/faqs/faqs-ability.md`

Use this for:

- `globalThis` and `Context`
- Stage-model behavior
- common `UIAbility` questions

## Style guides

- `application-dev/quick-start/arkts-coding-style-guide.md`
- `contribute/style-guide/style-guide-example-code-style.md`

Use these for:

- naming and coding style
- `BusinessError` examples
- `try/catch` and Promise error-handling examples

## Everyday `.ets` authoring docs

- `application-dev/ui/rendering-control/arkts-rendering-control-ifelse.md`
- `application-dev/ui/rendering-control/arkts-rendering-control-foreach.md`
- `application-dev/ui/state-management/arkts-builder.md`
- `application-dev/ui/state-management/arkts-localBuilder.md`
- `application-dev/reference/apis-as/js-apis-promptAction.md`
- `application-dev/reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md`
- `application-dev/reference/apis-arkui/arkui-ts/ts-methods-custom-dialog-box.md`
- `application-dev/reference/apis-arkui/arkui-ts/ts-explicit-animation.md`

Use these for:

- conditional rendering
- `ForEach` and `LazyForEach`
- `@Builder` and `@LocalBuilder`
- dialogs and prompt UI
- navigation structure
- explicit animation patterns

## Sample paths relative to `HARMONYOS_SAMPLES_ROOT`

- `code/DocsSample/ArkUISample/StateMgmtV2MVVM`
- `code/DocsSample/ArkUISample/ParadigmStateManagement`

Use these for:

- V2 MVVM sample structure
- official `entry/src/main/ets/` layout such as `entryability/`, `pages/`, `view/`, `viewmodel/`, `model/`, and `settingability/` in `StateMgmtV2MVVM`
- `@Local`, `@Param`, `@Event`
- `@ObservedV2`, `@Trace`, `@Monitor`, `@Computed`
- `@LocalBuilder` cases including refresh pitfalls

## Fast search hints

Run targeted searches instead of loading entire trees:

```bash
rg -n "@ComponentV2|@ObservedV2|@Trace|@Local|@Param|@Event|@LocalBuilder" "$HARMONYOS_DOCS_ROOT" "$HARMONYOS_SAMPLES_ROOT" -g '*.md' -g '*.ets'
```

```bash
rg -n "globalThis|BusinessError|catch \\(error\\)" "$HARMONYOS_DOCS_ROOT" -g '*.md'
```

---
name: harmonyos-test-kit
description: Use when Codex needs official HarmonyOS/OpenHarmony Test Kit workflows for ArkTS unit tests, UI tests, performance tests, test-runner wiring, or command-line test execution. Trigger on `@ohos/hypium`, `@kit.TestKit`, `@ohos.UiTest`, `Driver`, `ON`, `aa test`, `ohosTest`, `testRunner`, `OpenHarmonyTestRunner`, unit-test, UI-test, performance-test, or when Codex should follow local official docs and samples for HarmonyOS testing.
---

# HarmonyOS Test Kit

## Overview

Use this skill for official HarmonyOS application testing workflows based on Test Kit. Prefer local official docs and local official samples before inventing project-specific test structure.

Read [references/official-test-kit-sources.md](references/official-test-kit-sources.md) first for doc paths, sample paths, and command templates.
Read [references/test-module-structure.md](references/test-module-structure.md) when the task is about `ohosTest`, `module.json5`, `testRunner`, or how to place test code in a Stage-model project.

For project scaffolding or app-completion work, use `$harmonyos-project-builder`.
For general SDK build, packaging, install, launch, or device-debug workflows outside testing, use `$harmonyos-sdk-build-deploy`.
For app code semantics inside `.ets` business code, use `$harmonyos-arkts-v2-assistant`.

## Source Priority

Consult sources in this order:

1. Local official docs discovered from `HARMONYOS_DOCS_ROOT`
2. Local official samples discovered from `HARMONYOS_SAMPLES_ROOT`
3. Official HarmonyOS documentation site `https://developer.huawei.com/consumer/cn/doc/` when local docs or samples are unavailable
4. The target repository's existing test modules, test scripts, and build instructions
5. General HarmonyOS knowledge only when the sources above do not answer the question

Treat `HARMONYOS_DOCS_ROOT` as valid when it points either to the docs repository root or directly to its `zh-cn/` subtree. Treat `HARMONYOS_SAMPLES_ROOT` as valid when it points to the `applications_app_samples` repository root. If local docs or samples are missing, continue with the remaining sources instead of failing immediately.

## Workflow

### 1. Classify the testing task

Put the request into one primary bucket:

- Unit test with `@ohos/hypium`
- UI test with `@kit.TestKit` or `@ohos.UiTest`
- Performance test with `PerfTest`
- `ohosTest` module or `module.json5` wiring
- `aa test` execution or filtering
- Test failure diagnosis
- Converting a manual validation path into an automated test

### 2. Load the narrowest official source first

- For overall Test Kit capability selection, open:
  - `application-dev/application-test/test-kit-overview.md`
- For ArkTS unit testing with `@ohos/hypium`, open:
  - `application-dev/application-test/unittest-guidelines.md`
- For UI automation with `Driver`, `ON`, component lookup, gestures, or waits, open:
  - `application-dev/application-test/uitest-guidelines.md`
- For white-box performance testing, open:
  - `application-dev/application-test/perftest-guideline.md`
- For `aa test` execution parameters, open:
  - `application-dev/tools/aa-tool.md`
- For `testRunner` and module wiring, open:
  - `application-dev/quick-start/module-configuration-file.md`
- For official sample structure and sample code, inspect:
  - `code/Project/Test/jsunit`
  - `code/Project/Test/uitest`
  - `code/Project/Test/perftest`

Resolve those relative paths against `HARMONYOS_DOCS_ROOT` and `HARMONYOS_SAMPLES_ROOT` when local copies exist. If they do not, search the official site for the same document title or topic.

### 3. Preserve the official test layout

For Stage-model application testing, prefer the official sample layout before inventing custom structure:

- keep the app module under `entry/src/main`
- keep test code under `entry/src/ohosTest`
- keep test scripts under `entry/src/ohosTest/ets/test`
- keep the test module's `module.json5` aligned with the official `ohosTest` sample shape
- add or adjust `testRunner` only when the selected official workflow requires it

Do not create project-specific testing folders unless the repository already uses them or a concrete official sample pattern requires them.

### 4. Pick the right testing layer

- Use unit tests for logic, API return values, state transitions, and non-UI behavior
- Use UI tests when the behavior depends on rendered UI, component lookup, gestures, focus, dialogs, or navigation
- Use performance tests only when the task is explicitly about measurable timing, CPU, memory, startup delay, page-switch latency, or scroll FPS
- If the repository already has a test style, extend it instead of rewriting everything around a different framework

### 5. Keep tests aligned with official execution flows

- Prefer DevEco Studio execution when the user wants IDE-driven testing
- Prefer `aa test` when the user wants command-line execution or test filtering
- Distinguish Stage-model and FA-model parameters when giving `aa test` commands
- If test execution depends on SDK location or `hvigorw`, prefer a repository-provided build command first, then `DEVECO_SDK_HOME`, then OS-appropriate DevEco paths
- Derive bundle name, module name, and runner name from the actual project before giving final commands

## Decision Rules

### Unit tests

- Use `@ohos/hypium` as the official ArkTS unit-test base
- Keep test cases in `describe` and `it` form aligned with official examples
- Use async test style when the behavior is asynchronous
- Use assertions to validate concrete outcomes rather than relying on logs alone

### UI tests

- Treat UI tests as unit-test-based scripts that additionally use Test Kit UI APIs
- Use `Driver.create()` as the main test entry for UI operations
- Use `ON` matchers and component lookup before coordinate-based fallback when possible
- Use `waitForIdle` or `waitForComponent` after UI-triggering actions when the page needs time to settle
- Do not invent repository-specific page-driver abstractions unless the codebase already has them

### Performance tests

- Use `PerfTest` only for explicit performance measurement needs
- Define metrics, action code, reset code, iteration count, and timeout explicitly
- Keep performance assertions tied to measurable thresholds instead of generic pass or fail language

### Test module wiring

- Prefer the official `ohosTest` module shape from the samples
- Read the repository's real `module.json5` and `oh-package.json5` before changing test wiring
- Use the documented `testRunner` tag only when that wiring is actually required by the selected test flow
- Do not invent nonstandard test entry layouts when the official sample already covers the needed case

### Command-line execution

- Use `aa test` argument patterns from the official docs
- For Stage-model apps, prefer `-m <module-name>` when needed
- For FA-model apps, use `-p <package-name>` only when the official docs say that flow applies
- Keep filter examples grounded in official parameters such as `class`, `itName`, `level`, `size`, `testType`, `timeout`, and `stress`

## Typical Tasks

### Add or fix a unit test

1. inspect the existing `ohosTest` module and current `@ohos/hypium` usage
2. align the new test with the official sample structure
3. keep the test focused on one behavior and one assertion path at a time
4. provide the smallest valid `aa test` or IDE execution path when execution is requested

### Add or fix a UI test

1. confirm the UI behavior really requires rendered interaction
2. use official `Driver` and `ON` patterns first
3. add waits only where page state actually changes asynchronously
4. prefer semantic component lookup before coordinate-only interaction
5. provide the narrowest runnable test command when execution is requested

### Add or fix a performance test

1. define the metric list and measured code path explicitly
2. add reset logic if repeated runs need environment cleanup
3. keep thresholds explicit and reviewable
4. cite the official PerfTest doc or sample used

### Fix `ohosTest` or `testRunner` wiring

1. inspect the repository's current `entry/src/ohosTest` structure
2. compare it against the official `jsunit` or `uitest` sample layout
3. inspect `module.json5` and `testRunner` config before editing
4. preserve the repository's current module names and bundle metadata unless the user asked for a broader refactor

### Run tests from the command line

1. derive bundle name, module name, and runner name from the real project
2. choose the narrowest `aa test` invocation that matches the request
3. add filters such as `class`, `itName`, `level`, `size`, or `testType` only when needed
4. report test output or failure stage clearly

## Verification

Do not force the same test command on every HarmonyOS project.

Before execution:

- read the repository's `AGENTS.md`, build instructions, and existing test modules
- verify whether the app needs build or install steps first
- use the repository's real build command when compilation is required before testing
- if SDK location matters for the test build, prefer `DEVECO_SDK_HOME` when the repository or environment already uses it

When code changes are involved, prefer the lightest valid verification:

- compile the affected test module first when possible
- run the narrowest unit, UI, or perf test path that matches the request
- use broader test-package execution only when the user asked for it or the change scope requires it

## Output Style

When using this skill:

- lead with the official Test Kit path
- state whether the answer is for unit, UI, performance, wiring, or execution flow
- cite the local doc path or sample path used
- keep examples minimal and runnable
- distinguish clearly between app code under test and test code under `ohosTest`

## Boundaries

- Keep this skill focused on official HarmonyOS testing workflows, not general app architecture
- Do not turn this skill into a generic build and deploy guide; use `$harmonyos-sdk-build-deploy` for that
- Do not turn this skill into an ArkTS business-code semantics guide; use `$harmonyos-arkts-v2-assistant` for that
- Do not derive testing structure from the current repository when the official test samples already provide a valid pattern

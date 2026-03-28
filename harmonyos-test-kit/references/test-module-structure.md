# Test Module Structure

Use this reference when the task is about where HarmonyOS tests live, how `ohosTest` is wired, or how to align a project with the official testing samples.

## Official Stage-model sample shape

The official `jsunit` and `uitest` samples use this split:

```text
entry/
  src/main/
    module.json5
    ets/
      entryability/
      pages/
  src/ohosTest/
    module.json5
    ets/
      testability/
      test/
```

Treat this as the default testing layout for Stage-model application tests.

## What belongs where

- `entry/src/main`: app code under test
- `entry/src/ohosTest`: test module code
- `entry/src/ohosTest/ets/test`: unit, UI, or performance test scripts
- `entry/src/ohosTest/ets/testability`: test ability entry used by the official samples
- `entry/src/ohosTest/module.json5`: test module metadata for the `ohosTest` module

## `testRunner` config

The official module configuration docs define `testRunner` as:

- `name`: test runner object name
- `srcPath`: path to test-runner code

Use this only when the selected test flow actually needs explicit runner wiring. Do not invent a custom runner when the default official sample flow already works.

## Practical rules

- Keep the app module and test module separate
- Add tests under `ohosTest` instead of mixing them into production `ets/` folders
- Reuse the official sample structure before introducing custom testing directories
- Derive bundle name, module name, and ability names from the real project before writing commands
- If the repository already has a coherent test layout, extend it instead of forcing a different official sample shape midstream

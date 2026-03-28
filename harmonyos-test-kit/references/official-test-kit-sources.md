# Official Test Kit Sources

Use this file as the first navigation map for HarmonyOS and OpenHarmony application testing.

## Environment variables

- `HARMONYOS_DOCS_ROOT`
- `HARMONYOS_SAMPLES_ROOT`
- `DEVECO_SDK_HOME`

Resolve paths as follows:

- `HARMONYOS_DOCS_ROOT` may point either to the docs repository root or directly to its `zh-cn/` subtree
- `HARMONYOS_SAMPLES_ROOT` should point to the `applications_app_samples` repository root
- `DEVECO_SDK_HOME`, when present, should point to the DevEco SDK root directory
- if local docs or samples are missing, search `https://developer.huawei.com/consumer/cn/doc/` by document title before falling back to generic guidance

## Core docs relative to `HARMONYOS_DOCS_ROOT`

- `application-dev/application-test/test-kit-overview.md`
  - use to choose between unit, UI, and performance testing
- `application-dev/application-test/unittest-guidelines.md`
  - use for `@ohos/hypium`, `describe`, `it`, assertions, async tests, and `aa test` patterns
- `application-dev/application-test/uitest-guidelines.md`
  - use for `Driver`, `ON`, component lookup, gestures, waits, and UI automation
- `application-dev/application-test/perftest-guideline.md`
  - use for `PerfTest`, metrics, iterations, reset code, and thresholds
- `application-dev/tools/aa-tool.md`
  - use for `aa test` command-line execution and filter parameters
- `application-dev/quick-start/module-configuration-file.md`
  - use for `testRunner` wiring

## Official samples relative to `HARMONYOS_SAMPLES_ROOT`

- `code/Project/Test/jsunit`
  - Stage-model unit test sample
- `code/Project/Test/uitest`
  - Stage-model UI test sample
- `code/Project/Test/perftest`
  - Stage-model performance test sample

## Common command patterns

Replace placeholders with real project values.

### SDK root examples

```bash
export DEVECO_SDK_HOME=/Applications/DevEco-Studio.app/Contents/sdk
```

```powershell
$env:DEVECO_SDK_HOME = '<DevEco Studio install dir>\sdk'
```

Use these as examples only. On different operating systems, the DevEco installation root differs. Prefer repository commands or the already-configured environment over hardcoded paths.

### Run all tests in a Stage-model module

```bash
hdc shell aa test -b <bundle-name> -m <module-name> -s unittest <runner-name>
```

### Run selected test suite or test case

```bash
hdc shell aa test -b <bundle-name> -m <module-name> -s unittest <runner-name> -s class <describe-name>
```

```bash
hdc shell aa test -b <bundle-name> -m <module-name> -s unittest <runner-name> -s class <describe-name>#<it-name>
```

### Run by test metadata

```bash
hdc shell aa test -b <bundle-name> -m <module-name> -s unittest <runner-name> -s level <level>
```

```bash
hdc shell aa test -b <bundle-name> -m <module-name> -s unittest <runner-name> -s size <small|medium|large>
```

```bash
hdc shell aa test -b <bundle-name> -m <module-name> -s unittest <runner-name> -s testType <function|performance|...>
```

### Timeout or repeated execution

```bash
hdc shell aa test -b <bundle-name> -m <module-name> -s unittest <runner-name> -s timeout <ms>
```

```bash
hdc shell aa test -b <bundle-name> -m <module-name> -s unittest <runner-name> -s stress <count>
```

## Search hints

```bash
rg -n "@ohos/hypium|describe\(|it\(|expect\(|abilityDelegatorRegistry|OpenHarmonyTestRunner" "$HARMONYOS_SAMPLES_ROOT/code/Project/Test" -g '*.ets' -g '*.ts'
```

```bash
rg -n "Driver.create|ON\.|waitForIdle|waitForComponent|PerfTest|PerfMetric|aa test|testRunner" "$HARMONYOS_DOCS_ROOT" "$HARMONYOS_SAMPLES_ROOT/code/Project/Test" -g '*.md' -g '*.ets' -g '*.ts'
```

# Local Official Build And Deploy Sources

Use this file as the first navigation map for HarmonyOS and OpenHarmony build, package, install, launch, and device-debug tasks.

## Environment variables

- `HARMONYOS_DOCS_ROOT`
- `HARMONYOS_SAMPLES_ROOT`
- `DEVECO_SDK_HOME`

Resolve paths as follows:

- `HARMONYOS_DOCS_ROOT` may point either to the docs repository root or directly to its `zh-cn/` subtree
- `HARMONYOS_SAMPLES_ROOT` may point to a local `applications_app_samples` repository, but this skill does not require samples for its core workflows
- `DEVECO_SDK_HOME`, when present, should point to the DevEco SDK root directory rather than a nested tool directory
- if `HARMONYOS_DOCS_ROOT` is missing or invalid, search `https://developer.huawei.com/consumer/cn/doc/` by document title or tool name before falling back to generic advice

## Priority

When platform behavior is unclear, prefer this order:

1. local official docs
2. local official samples if a command needs an end-to-end example
3. official HarmonyOS documentation site `https://developer.huawei.com/consumer/cn/doc/`
4. project-local build scripts and AGENTS instructions

## Core Entry Points

### SDK command-line overview

- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/tools/command-line-tools-overview.md`
- Use for:
  - confirming which official tools exist in the SDK
  - confirming that the SDK is obtained from DevEco Studio or Command Line Tools
  - picking between `hdc`, `aa`, `bm`, `hilog`, `packing-tool`
- Key facts:
  - the SDK embedded in DevEco Studio already contains the main command-line tools
  - command-line tools can also come from Command Line Tools
  - the docs confirm the SDK lives under the DevEco Studio installation's `sdk` directory, but do not require a single environment-variable name for locating it

### SDK and build-path resolution

- Use for:
  - locating the SDK root before build or packaging commands
  - deciding whether `DEVECO_SDK_HOME` is usable in the current environment
  - deriving tool paths in a cross-platform-safe way
- Preferred order:
  1. repository-provided build command or script
  2. `DEVECO_SDK_HOME` when already set by the user or repository
  3. `PATH` for tools already exposed by the environment
  4. OS-appropriate DevEco Studio installation roots
- Cross-platform notes:
  - macOS example SDK root: `/Applications/DevEco-Studio.app/Contents/sdk`
  - Windows example SDK root: `<DevEco Studio install dir>\sdk`
  - Linux example SDK root: `<DevEco Studio install dir>/sdk`
- Important reminders:
  - do not hardcode one operating system path as the only valid answer
  - `DEVECO_SDK_HOME` should point to the SDK root, not directly to `hdc`, `hvigorw`, or a nested toolchain path
  - if the repository already calls a specific `hvigorw`, keep that command unless the user asked to normalize it

### `hdc`

- Path relative to `HARMONYOS_DOCS_ROOT`: `device-dev/subsystems/subsys-toolchain-hdc-guide.md`
- Use for:
  - device discovery
  - USB or TCP connection
  - shell access
  - host-to-device file transfer
  - direct install or uninstall
  - live logs and transport troubleshooting
- Typical tasks:
  - `hdc list targets`
  - `hdc shell`
  - `hdc file send`
  - `hdc install`
  - `hdc hilog`
- Important reminders:
  - `hdc` lives under the SDK toolchains directory
  - `hdc kill -r` is a documented recovery action when the service gets stuck

### `bm`

- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/tools/bm-tool.md`
- Use for:
  - install, uninstall, dump, and clean bundle operations from the device shell
- Typical tasks:
  - `bm install -p /data/local/tmp/app.hap`
  - `bm uninstall -n com.example.app`
  - `bm dump -n com.example.app`
- Important reminders:
  - official docs say to enter `hdc shell` before using `bm`
  - `bm` expects device-side paths
  - `-g` can auto-grant debug app permissions in supported cases

### `aa`

- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/tools/aa-tool.md`
- Use for:
  - launch, stop, attach, appdebug, and startup measurement
- Typical tasks:
  - `aa start -a EntryAbility -b com.example.app`
  - `aa force-stop com.example.app`
  - `aa start ... -W`
- Important reminders:
  - when called via `hdc shell`, quote the full `aa ...` command
  - `-W` is the documented startup timing path for explicit UIAbility launch

### `packing-tool`

- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/tools/packing-tool.md`
- Use for:
  - packaging DevEco build outputs into HAP, HSP, APP, HQF, or multi-project APP artifacts
  - understanding packaging validation rules
- Typical tasks:
  - HAP packaging from build outputs
  - APP packaging from HAP or HSP inputs
  - checking multi-project packaging constraints
- Important reminders:
  - package inputs come from DevEco build outputs
  - the doc explains how to inspect build logs to find actual packaging input paths
  - packaging performs legality checks on generated `module.json`

### `binary-sign-tool`

- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/tools/binary-sign-tool.md`
- Use for:
  - signing ELF binaries
  - printing signature, certificate, and permission info
- Important reminders:
  - this is for native binaries, not the whole app package signing flow

## Supporting Quick-Start Docs

### HAP structure and debug delivery

- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/quick-start/hap-package.md`
- Use for:
  - understanding single-HAP versus multi-HAP tradeoffs
  - checking how HAP install and update flows relate to debugging
  - confirming that debug install can go through `hdc` directly or `hdc shell` plus `bm`

### Application and module config

- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/quick-start/app-configuration-file.md`
- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/quick-start/module-configuration-file.md`
- Use for:
  - mapping package output metadata back to `app.json5` and `module.json5`
  - deriving bundle, module, and ability names for launch or install instructions

### Module structure and quick start

- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/quick-start/module-structure.md`
- Path relative to `HARMONYOS_DOCS_ROOT`: `application-dev/quick-start/start-with-ets-stage.md`
- Use for:
  - understanding default Stage-model layout
  - confirming where generated outputs and entry modules come from

## How To Apply These Sources

### If the user asks to build the current repository

1. read the repo's AGENTS instructions and existing build scripts
2. confirm the real DevEco or `hvigorw` command already used by the repo
3. resolve the SDK location via repository command, `DEVECO_SDK_HOME`, `PATH`, or OS-specific DevEco install root
4. distinguish whether the requested build is for the main app target or an `ohosTest` target
5. use official docs only to justify or troubleshoot the toolchain path

### If the user asks how to install or launch on a device

1. use `hdc` to confirm device connectivity
2. choose direct `hdc install` or `hdc shell` plus `bm install` based on where the artifact lives
3. use `aa start` when the app or ability must be launched explicitly
4. use `hdc hilog` or repo-specific log commands for runtime diagnosis

### If the user asks how to package for release

1. confirm whether the task is HAP, HSP, or APP packaging
2. inspect the project's real build outputs
3. use `packing-tool` guidance for the exact package mode
4. only bring in signing guidance that matches the artifact type

## Common command patterns

Use these as starting templates. Replace placeholders with the real project values instead of inventing them.

### SDK root examples

Use these only as examples, not as universal hardcoded answers.

```bash
export DEVECO_SDK_HOME=/Applications/DevEco-Studio.app/Contents/sdk
```

```powershell
$env:DEVECO_SDK_HOME = '<DevEco Studio install dir>\sdk'
```

### `hvigorw` app-module build

```bash
DEVECO_SDK_HOME=<sdk-root> <hvigorw-path> --no-daemon --mode module -p module=<module>@<target> -p product=<product> -p buildMode=<debug|release> assembleHap
```

Use for:

- building the main app HAP when the repository already relies on `hvigorw`
- explicitly selecting module target, product, and build mode from the repository's real build profile

### `hvigorw` `ohosTest` build

```bash
DEVECO_SDK_HOME=<sdk-root> <hvigorw-path> --no-daemon --mode module -p module=<module>@ohosTest -p product=<product> -p buildMode=debug assembleHap
```

Use for:

- compiling a HarmonyOS `ohosTest` package before `aa test` or device-side test execution
- keeping test-target builds distinct from main-app builds

### Device discovery and shell

```bash
hdc list targets
```

```bash
hdc -t <device-id> shell
```

Use for:

- checking whether a device is connected
- selecting the right target when multiple devices are present
- entering device shell before `bm` or `aa`

### Host-to-device file transfer

```bash
hdc -t <device-id> file send <host-hap-path> /data/local/tmp/<app-file-name>.hap
```

Use for:

- moving a built HAP to a device before `bm install`
- pushing additional debug assets when device-side install paths are needed

### Direct HAP install from host

```bash
hdc -t <device-id> install <host-hap-path>
```

Use for:

- simple debug delivery when the HAP is already on the host
- one-step install without entering shell

### Install with `bm` from device shell

```bash
hdc -t <device-id> shell "bm install -p /data/local/tmp/<app-file-name>.hap"
```

Use for:

- install flows that already depend on a device-side path
- `bm` options such as `-g`, `-d`, or `-w`

Optional variants:

```bash
hdc -t <device-id> shell "bm install -p /data/local/tmp/<app-file-name>.hap -g"
```

```bash
hdc -t <device-id> shell "bm install -p /data/local/tmp/<app-file-name>.hap -w 180"
```

### Uninstall and bundle inspection

```bash
hdc -t <device-id> shell "bm uninstall -n <bundle-name>"
```

```bash
hdc -t <device-id> shell "bm dump -n <bundle-name>"
```

Use for:

- clean reinstall loops
- checking whether the installed bundle name matches the expected app

### Launch and stop

```bash
hdc -t <device-id> shell "aa start -a <ability-name> -b <bundle-name>"
```

```bash
hdc -t <device-id> shell "aa force-stop <bundle-name>"
```

Use for:

- explicit launch after install
- restarting the app during debug loops

If startup timing matters:

```bash
hdc -t <device-id> shell "aa start -a <ability-name> -b <bundle-name> -W"
```

### Logs

```bash
hdc -t <device-id> hilog
```

Use for:

- runtime log inspection after install or launch
- checking startup errors, permission failures, or crashes

### Build command selection

Do not invent a generic `hvigorw` command if the repository already defines one.

Use this order:

1. `AGENTS.md`
2. existing project build scripts
3. existing `hvigorfile.ts`, `build-profile.json5`, `app.json5`, and `module.json5`
4. official docs only to justify the final command shape

Typical module build shape when the repo uses hvigor directly:

```bash
<hvigorw> --no-daemon --mode module -p module=<module>@<target> -p product=<product> -p buildMode=<build-mode> assembleHap
```

Adapt the exact flags to the repository instead of copying this blindly.

### Packaging with `packing-tool`

Typical HAP packaging shape:

```bash
java -jar app_packing_tool.jar --mode hap --json-path <module.json> --out-path <output.hap>
```

Typical APP packaging shape:

```bash
java -jar app_packing_tool.jar --mode app --hap-path <hap-or-dir> --out-path <output.app>
```

Only use these after inspecting the real build outputs and the official packaging doc for the needed mode.

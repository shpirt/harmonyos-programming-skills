# Project Blueprint

Use this blueprint when turning an empty or partial HarmonyOS project into a complete application.

## Official build-first artifacts

Inspect or create these first:

- `AppScope/app.json5`
- root `build-profile.json5`
- root `hvigorfile.ts`
- module `build-profile.json5`
- module `hvigorfile.ts`
- module `src/main/module.json5`
- `entry/src/main/ets/entryability`
- `entry/src/main/ets/pages`
- `entry/src/main/resources`
- page routing config under `resources/base/profile/`

These items come from the official Stage-model project structure and quick-start flow. Do not start feature code until this buildable skeleton is coherent.

## Official Stage-model source shape

For an ArkTS Stage-model app, the official docs and default project generation establish this core shape:

```text
AppScope/
  app.json5
entry/
  build-profile.json5
  hvigorfile.ts
  src/main/
    module.json5
    ets/
      entryability/
      pages/
    resources/
      base/profile/
```

Use this as the default for empty projects.

## Optional engineering subfolders

HarmonyOS docs do not mandate one fixed set of internal engineering subfolders under `entry/src/main/ets/`.

For larger apps, official MVVM samples show concrete layouts such as:

```text
entry/src/main/ets/
  entryability/
  model/
  pages/
  settingability/
  view/
  viewmodel/
```

This mirrors the official `StateMgmtV2MVVM` sample. Other official samples may use `views/` instead of `view/`, but do not invent those folders unless the selected official sample pattern or project complexity justifies them.

For more complex system-capability projects, you may also add:

```text
entry/src/main/ets/
  service/
  extension/
  bridge/
```

Treat these as optional engineering layers derived from official sample patterns and actual project scope, not as a HarmonyOS-mandated directory standard.

## Example responsibility split for larger apps

- `pages/`: page entry, composition, routing glue
- `view/` or `views/`: reusable presentational components
- `viewmodel/`: UI-facing state transitions and coordination
- `service/`: IO, persistence, event, import, runtime, and bridge orchestration when the app needs them
- `model/`: UI-facing models and plain DTOs
- `extension/`, `bridge/`, or native-facing folders: only when the app requires those capabilities

## Good defaults

- Use ArkUI V2 for new UI work
- Keep official Stage-model build artifacts and source layout intact
- Introduce extra layers only when official samples or project complexity justify them
- Keep observed UI state out of persistence and transport payloads
- Treat high-frequency status updates as a design concern, not a last-mile patch

## Common completion gaps

- The official Stage-model skeleton is incomplete or inconsistent
- Pages exist but routing config is incomplete
- UI is wired, but build config is incomplete
- Extra layers were added too early without a real need
- Runtime starts, but status and logs do not flow back to UI
- Persistence stores observed objects instead of DTOs
- Feature code exists, but no device or runtime verification path is documented

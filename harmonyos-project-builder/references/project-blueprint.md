# Project Blueprint

Use this blueprint when turning an empty or partial HarmonyOS project into a complete application.

## Build-first artifacts

Inspect or create these first:

- `AppScope/app.json5`
- root `build-profile.json5`
- module `build-profile.json5`
- module `hvigorfile.ts`
- root `hvigorfile.ts`
- module `src/main/module.json5`
- page routing config under `resources/base/profile/`

Do not start feature code until these files form a coherent buildable skeleton.

## Recommended source layout

Use only the folders the project actually needs.

```text
entry/src/main/ets/
  pages/
  view/
  viewmodel/
  service/
  model/
  vpn/
  extension/
  bridge/
```

## Responsibility split

- `pages/`: page entry, composition, routing glue
- `view/`: reusable presentational components
- `viewmodel/`: UI-facing state transitions and coordination
- `service/`: IO, persistence, event, import, runtime, bridge orchestration
- `model/`: observed UI models and plain DTOs
- `vpn/` or `extension/`: system-facing abilities and extension logic
- `bridge/` or native-facing directories: narrow boundary to native or Go runtime

## Good defaults

- Use ArkUI V2 for new UI work
- Keep ViewModel and service boundaries explicit
- Keep observed UI state out of persistence and transport payloads
- Treat high-frequency status updates as a design concern, not a last-mile patch

## Common completion gaps

- Pages exist but no ViewModel layer
- UI is wired, but build config is incomplete
- Runtime starts, but status and logs do not flow back to UI
- Persistence stores observed objects instead of DTOs
- Feature code exists, but no device or runtime verification path is documented

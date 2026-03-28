# System Client Pattern

Use this pattern when the HarmonyOS project is more than a plain UI app, especially when it includes VPN, extension abilities, native bridge code, or a wrapped runtime such as Go or C++.

## Official baseline first

Start from the official Stage-model project structure:

- `entry/src/main/ets/entryability`
- `entry/src/main/ets/pages`
- `entry/src/main/resources`
- `module.json5`, `app.json5`, and build files

Only add further layers after that baseline is in place.

## Optional engineering layers for complex clients

This is a pragmatic layering pattern for complex system-capability clients. It is not an official HarmonyOS directory standard.

Official MVVM and advanced samples show that larger apps may benefit from layers such as:

- `view/` or `views/`: reusable visual sections
- `viewmodel/`: UI-facing state transitions
- `model/`: UI-facing models or DTOs

For system-capability clients, add further layers only when a concrete capability requires them:

- `service/`: orchestration, lifecycle, persistence, event flow, import, and bridge calls once those responsibilities outgrow page or ViewModel code
- additional ability or extension source folders only when the app actually defines them
- native-facing directories such as `cpp/`, `native/`, or runtime wrappers only when native integration is present

Do not treat project-specific folders as a default part of a generic HarmonyOS layout. Use only the layers that the feature set and official sample pattern actually need.

## Boundary rules

- UI and ViewModel-style layers may use observed models
- Persistence, event transport, bridge calls, and native boundaries should use plain DTOs
- Runtime start, stop, status, selectors, counters, and logs should move through explicit service APIs
- Do not pass observed UI objects directly into bridge or native code

## Runtime flow checklist

For runtime-backed clients, define these flows early:

1. Configuration or import flow
2. Start flow
3. Stop flow
4. Status snapshot flow
5. Logs flow
6. User actions such as selector change or reconnect

Each flow should have:

- one service entry point
- one UI-facing state update path
- one UI representation

## VPN or extension-specific notes

- Define permissions and declarations before UI polish
- Keep extension-facing lifecycle handling out of page code
- Expose explicit service methods for tunnel lifecycle rather than embedding platform calls in components
- Verify on device because compile success is not enough for VPN-like features

## Frequent failure modes

- UI directly managing runtime lifecycle
- duplicated status fields across UI and service layers
- status updates that bypass a consistent UI-facing state path
- bridge payloads carrying observed objects
- logs available only in the native layer and not surfaced to the app

## Good completion signal

The project is on a sound path when:

- the official Stage-model skeleton is intact
- the app builds
- the runtime can start and stop through explicit non-UI APIs
- the UI can display current status and logs
- selector or configuration changes propagate through one consistent path

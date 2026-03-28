# System Client Pattern

Use this pattern when the HarmonyOS project is more than a plain UI app, especially when it includes VPN, extension abilities, native bridge code, or a wrapped runtime such as Go or C++.

## Recommended layers

For system-capability clients, prefer these layers:

- `pages/`: composition and screen entry
- `view/`: reusable visual sections
- `viewmodel/`: UI-facing state transitions
- `service/`: orchestration, lifecycle, persistence, event flow, import, and bridge calls
- `model/`: observed UI models plus plain DTOs for transport or storage
- `vpn/` or `extension/`: ability and extension integration
- native-facing directories such as `cpp/`, `native/`, or runtime wrappers

## Boundary rules

- UI and ViewModel layers may use observed models
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
- one ViewModel-facing state update path
- one UI representation

## VPN or extension-specific notes

- Define permissions and declarations before UI polish
- Keep extension-facing lifecycle handling out of page code
- Expose explicit service methods for tunnel lifecycle rather than embedding platform calls in components
- Verify on device because compile success is not enough for VPN-like features

## Frequent failure modes

- UI directly managing runtime lifecycle
- duplicated status fields across page and service layers
- status updates that bypass ViewModel state
- bridge payloads carrying observed objects
- logs available only in the native layer and not surfaced to the app

## Good completion signal

The project is on a sound path when:

- the app builds
- the runtime can start and stop through service APIs
- the UI can display current status and logs
- selector or configuration changes propagate through one consistent path

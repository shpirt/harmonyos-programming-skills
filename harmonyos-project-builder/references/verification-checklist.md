# Verification Checklist

Use this checklist before calling a HarmonyOS project complete.

## Build

- Config files parse correctly
- hvigor command succeeds for the intended module, product, and build mode
- Generated HAP or output artifact exists in the expected path

## Startup

- App launches without immediate crash
- Entry page or ability loads expected content
- Required permissions and declarations are present

## UI architecture

- Page composition is separated from runtime orchestration
- Shared state is not duplicated across unrelated components
- V1 and V2 usage is intentional rather than accidental

## Runtime and integration

- Service or bridge APIs return consistent status
- Logs are available at the layer where operators need them
- Start and stop flows are explicit and idempotent enough for the use case
- Transport and persistence layers use plain DTOs rather than observed objects

## Device validation

- Installation works on the intended device class
- Required system capability behaves on device, not just in compile output
- Failure paths produce actionable logs

## Delivery

- Known gaps are listed explicitly
- Build command and verification command are documented in the repository context
- The next unfinished phase is clear

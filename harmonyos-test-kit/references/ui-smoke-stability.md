# UI Smoke Stability

Use these rules for general-purpose HarmonyOS mobile UI smoke tests.

## First-screen assertions

- assert only top-of-screen or clearly stable structural elements on initial render
- do not assume lower sections of a long `Scroll` page are visible on first paint
- prefer section titles or app titles over seeded sample-task text

## Scroll strategy

- prefer semantic lookup before coordinate interaction
- if semantic lookup cannot reach below-fold content, use explicit swipe coordinates
- prefer repeated short or medium swipes over one aggressive fling when reliability matters
- add `waitForIdle` after a scroll that changes visible content

## Component lookup

- use `waitForComponent` when the node may appear after render or scroll
- if the next action targets the same component, use the returned component instance directly
- avoid redundant second lookups unless the UI is expected to re-render between steps

## Assertion scope

- smoke tests should prove the core path works, not exhaustively validate copy or seeded demo content
- keep the path minimal: launch, locate the primary flow, perform one interaction, verify one meaningful state change

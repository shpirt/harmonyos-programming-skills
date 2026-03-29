# Review Checkpoints

## Overview

Use these checkpoints when reviewing a HarmonyOS app screen, flow, or design proposal. They are derived from the local UX design docs, especially:

- `/Users/shpirt/playground/docs/zh-cn/design/ux-design/design-checklist.md`
- `/Users/shpirt/playground/docs/zh-cn/design/ux-design/app-ux-design.md`
- `/Users/shpirt/playground/docs/zh-cn/design/ux-design/visual-basis.md`
- `/Users/shpirt/playground/docs/zh-cn/design/ux-design/multimodal-component-overview.md`

## Pre-Implementation Review

- Is the device scope explicit: phone only, or multi-device?
- Is the navigation model clear: flat, hierarchical, or hybrid?
- Is the expected adaptation path defined for rotation, resizing, split screen, and large font?
- Are the required input modes explicit: touch, mouse, keyboard, remote, gamepad?
- Are official HarmonyOS components sufficient before proposing custom controls?

## Mandatory Checks

These should normally be treated as blocking issues for a production-ready design.

- Layout must not clip, deform, truncate, or leave excessive empty space across intended devices.
- Grid-based layouts must align containers to the grid correctly.
- If a grid is annotated, the actual layout must genuinely follow it.
- Layout sizing should use `vp`, except where strict pixel control is truly necessary.
- Text sizing should use `fp` and remain stable under larger system font settings.

## Recommended Checks

These are strong recommendations unless the product has a justified exception.

- Navigation structure should stay understandable and consistent across devices.
- The design should state the responsive grid type and breakpoint behavior when applicable.
- Non-grid screens should declare which adaptive layout abilities are used.
- Colors should prefer layered parameters and should behave acceptably in dark mode.
- Controls should cover normal, disabled, pressed, focused, active, and hover states when those states are relevant.
- System-provided components should be preferred over custom variants where possible.

## Component Review

- Does the component fit the user task, not just the visual style?
- Does it behave correctly for the actual device class?
- Are keyboard focus and mouse hover states present when needed?
- If the component is custom, does it preserve the same interaction contract as the system component it replaces?

## Navigation Review

- Can the user always tell where they are, where they can go, and how to return?
- Is the primary navigation mechanism singular and legible in each context?
- If hierarchy depth grows, is there a compensating mechanism such as breadcrumbs or fast return?
- If the app adapts across devices, is the control placement changed without breaking the user’s mental model?

## Layout Review

- Does the screen survive narrow, wide, portrait, landscape, and split-window cases?
- Are spacing and alignment systematic rather than ad hoc?
- Is the interface overcrowded or visibly underfilled?
- Are adaptation strategies explicit: stretch, equal split, ratio, scale, extend, hide, wrap?

## Motion Review

- Does motion explain hierarchy change, continuity, or gesture outcome?
- Are transition styles consistent with the navigation model?
- Is there any motion that feels decorative but harms clarity or perceived speed?

## Output Template

When reporting findings, prefer this structure:

1. Scope: device classes, input modes, and reviewed screens
2. Blocking issues: mandatory-rule violations
3. Improvements: recommended refinements
4. Source basis: local doc paths used
5. Next actions: concrete implementation changes

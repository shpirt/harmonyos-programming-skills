---
name: harmonyos-ui-ux-guidelines
description: Use when the user needs HarmonyOS or OpenHarmony app UI/UX design guidance, design review, page structure advice, navigation choices, responsive or adaptive layout decisions, multimodal input consistency, component semantics, editing-flow decisions, visual rules, motion rules, or a pre-implementation or post-implementation design audit against HarmonyOS app design specifications.
---

# HarmonyOS UI UX Guidelines

## Overview

Use this skill for HarmonyOS app design decisions and design reviews. It helps turn the official HarmonyOS app design specifications into practical constraints for page structure, navigation, layout, interaction, visual styling, motion, and multimodal component usage.

Read [references/local-ux-docs.md](references/local-ux-docs.md) first for the local documentation map. Read [references/review-checkpoints.md](references/review-checkpoints.md) when the task is a concrete UI review, implementation acceptance check, or design gap analysis.

Prefer local docs under `HARMONYOS_DOCS_ROOT` when available. In this environment, the key local source is `zh-cn/design/ux-design/`. If local docs are missing or incomplete, fall back to the official design site: [HarmonyOS app design](https://developer.huawei.com/consumer/cn/design/).

## Source Priority

Consult sources in this order:

1. Local design docs under `HARMONYOS_DOCS_ROOT`, especially `zh-cn/design/ux-design/`
2. The official HarmonyOS design site `https://developer.huawei.com/consumer/cn/design/`
3. The target repository's current UI, product requirements, and screenshots or Figma files
4. General UI/UX knowledge only when the official sources do not answer the question

Treat the local docs root as valid when it points either to the docs repository root or directly to its language subtree. If the design docs exist locally, prefer citing those file paths instead of the website.

## Workflow

### 1. Classify the design task

Put the request into one primary bucket:

- Whole-app UX review
- Page or flow structure design
- Navigation pattern choice
- Layout, grid, adaptive, or responsive behavior
- Interaction and multimodal input consistency
- Visual styling, typography, iconography, or app icon work
- Motion and transition review
- Component selection and control-state review
- Pre-dev design constraints for implementation
- Post-dev acceptance review against HarmonyOS design rules

### 2. Load the narrowest official source first

- For overall design entry and topic selection, read:
  - `zh-cn/design/ux-design/Readme-CN.md`
- For cross-device UX principles, read:
  - `zh-cn/design/ux-design/app-ux-design.md`
- For navigation structure, read:
  - `zh-cn/design/ux-design/app-navigation-structure-design.md`
  - `zh-cn/design/ux-design/app-page-structure-design.md`
- For layout and adaptation, read:
  - `zh-cn/design/ux-design/ui-layout-overview.md`
  - `zh-cn/design/ux-design/grid-system.md`
  - `zh-cn/design/ux-design/adaptive-layout.md`
  - `zh-cn/design/ux-design/responsive-layout.md`
  - `zh-cn/design/ux-design/ui-layout-cases.md`
- For interaction and input modes, read:
  - `zh-cn/design/ux-design/human-machine-interaction-basis.md`
  - `zh-cn/design/ux-design/typical-input-modes.md`
  - `zh-cn/design/ux-design/unified-interaction-events.md`
- For visual design, read:
  - `zh-cn/design/ux-design/visual-basis.md`
  - `zh-cn/design/ux-design/visual-colors.md`
  - `zh-cn/design/ux-design/visual-fonts.md`
  - `zh-cn/design/ux-design/visual-icons.md`
  - `zh-cn/design/ux-design/visual-app-icons.md`
- For motion, read:
  - `zh-cn/design/ux-design/animation-overview.md`
  - `zh-cn/design/ux-design/animation-design-principles.md`
  - `zh-cn/design/ux-design/animation-attributes.md`
  - `zh-cn/design/ux-design/transition-animation.md`
  - `zh-cn/design/ux-design/gesture-animation.md`
- For control and component choice, read:
  - `zh-cn/design/ux-design/multimodal-component-overview.md`
  - the specific `multimodal-*.md` file for the component in question
- For acceptance review and handoff quality, read:
  - `zh-cn/design/ux-design/design-checklist.md`
  - `zh-cn/design/ux-design/design-specifications.md`
  - `zh-cn/design/ux-design/design-deliverable-overview.md`

### 3. Review structure before pixels

When reviewing a screen or flow, inspect in this order:

1. Information architecture and navigation
2. Cross-device layout behavior
3. Input and interaction consistency
4. Component choice and control states
5. Visual parameters such as spacing, color, and typography
6. Motion and transition behavior

Do not start with color or styling tweaks when the navigation model or layout strategy is still wrong.

### 4. Translate design rules into implementation constraints

When the task is paired with app implementation:

- convert design guidance into explicit engineering requirements
- call out whether the UI must support phone only or multiple device classes
- identify required input modes such as touch, mouse, keyboard, remote, or gamepad
- distinguish mandatory rules from recommended refinements
- prefer system-provided components and patterns before custom ones
- if a screen mixes browse, create, edit, and summary responsibilities, decide explicitly whether the one-page composition is still acceptable or whether the flow should split

### 5. End with an actionable review

For review tasks, produce:

- concrete findings tied to HarmonyOS design rules
- severity or priority when useful
- the official local doc path used
- the smallest viable next-step changes

## Decision Rules

### Architecture and navigation

- Prefer navigation that is clear, shallow, and consistent across devices
- Treat three levels as the practical upper bound unless the product clearly justifies deeper structure
- Avoid mixing multiple primary navigation systems in the same context unless the flow truly requires hybrid navigation
- For multi-device apps, adapt the navigation control placement to the device while preserving the user’s mental model

### Layout and adaptation

- Assume layout must react to rotation, split screen, window resizing, and font scaling
- Prefer grid, adaptive, and responsive strategies over fixed-position layout
- Use container alignment against the grid, not arbitrary child-level alignment
- Flag clipping, deformation, excessive whitespace, and overcrowding as design failures, not polish issues

### Interaction

- Treat multimodal input consistency as part of core UX, not an optional desktop enhancement
- If a screen can be used with mouse or keyboard, review hover, focus, active, and disabled states explicitly
- Prefer system interaction behavior unless there is a product-specific reason to customize it
- When a user starts editing an item from a list, prefer a spatially local edit state or a clearly signaled transition; avoid silent jumps to a distant edit region unless the UI makes that mapping obvious

### Visual design

- Use `vp` for layout sizing and `fp` for text sizing unless a strict pixel-controlled case justifies `px`
- Prefer layered design parameters and system resources over hard-coded visual values where possible
- Expect dark-mode resilience and large-font resilience in production-quality reviews

### Components

- Prefer official HarmonyOS multimodal components and their documented states
- Review whether the chosen component matches the device and interaction mode, not just the raw function
- If a custom component replaces a system component, review its states and interaction parity explicitly
- If a control is really choosing state rather than triggering a one-off action, review whether a selection-oriented component is more appropriate than a generic button

### Motion

- Motion should clarify hierarchy, causality, and continuity rather than exist for decoration
- Review transitions together with navigation and gesture semantics
- Flag motion that obscures state change, causes latency perception, or conflicts with input expectations

## Output Style

When using this skill:

- lead with the relevant HarmonyOS design rule
- separate mandatory issues from recommended improvements when the docs do so
- cite the local doc path used whenever practical
- convert abstract design guidance into implementation-safe, testable recommendations
- keep recommendations specific to the user’s device scope and app scenario

## Boundaries

- This skill guides design quality and design-rule compliance; it does not replace ArkTS coding guidance
- For HarmonyOS project scaffolding, use `$harmonyos-project-builder`
- For ArkTS, ArkUI, and state-management implementation details, use `$harmonyos-arkts-v2-assistant`
- For build, packaging, install, launch, and device-debug flows, use `$harmonyos-sdk-build-deploy`
- For `ohosTest`, UI automation, and test-runner wiring, use `$harmonyos-test-kit`

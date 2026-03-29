# Local UX Docs

## Overview

Use this file as the first navigation map for HarmonyOS and OpenHarmony app UI/UX design work.

Primary local root in this environment:

- `/Users/shpirt/playground/docs/zh-cn/design/ux-design/`

Official online fallback:

- [HarmonyOS app design](https://developer.huawei.com/consumer/cn/design/)

## Core Entry Points

### General entry

- `Readme-CN.md`
  - topic index for all major design areas

### Design principles

- `app-ux-design.md`
  - cross-device principles: 差异性、一致性、灵活性、兼容性
  - use for multi-device direction before reviewing details

### Navigation and page structure

- `app-navigation-structure-design.md`
  - use for flat, hierarchical, and mixed navigation choices
- `app-page-structure-design.md`
  - use for page-level structure and content organization

### Layout and adaptation

- `ui-layout-overview.md`
  - top-level layout overview
- `grid-system.md`
  - grid usage and alignment logic
- `adaptive-layout.md`
  - adaptive techniques such as stretch, equal split, scaling, wrap, extend, hide
- `responsive-layout.md`
  - breakpoint-driven responsive behavior
- `ui-layout-cases.md`
  - applied layout cases across device classes

### Interaction and input

- `human-machine-interaction-basis.md`
  - interaction fundamentals
- `typical-input-modes.md`
  - input-mode coverage expectations
- `unified-interaction-events.md`
  - interaction consistency across devices and inputs

### Visual system

- `visual-basis.md`
  - `vp`, `fp`, 8vp grid, layered visual parameters
- `visual-colors.md`
  - color guidance
- `visual-fonts.md`
  - typography guidance
- `visual-icons.md`
  - icon guidance
- `visual-app-icons.md`
  - application icon rules

### Motion

- `animation-overview.md`
  - motion overview
- `animation-design-principles.md`
  - motion principles
- `animation-attributes.md`
  - timing and motion attributes
- `transition-animation.md`
  - page and state transitions
- `gesture-animation.md`
  - gesture-linked motion behavior

### Components

- `multimodal-component-overview.md`
  - official component families and control states
- `multimodal-*.md`
  - component-specific guidance such as bottom tab, sidebar, title bar, dialog, button, text box, search box

### Review and handoff

- `design-checklist.md`
  - mandatory vs recommended design review rules
- `design-specifications.md`
  - specification document expectations for multi-device delivery
- `design-deliverable-overview.md`
  - handoff package overview
- `design-effect-drawings.md`
  - effect drawing guidance
- `design-annotated-drawings.md`
  - annotated drawing guidance
- `design-map-cached-drawings.md`
  - sliced asset guidance
- `design-resources.md`
  - system design resources and layered parameters

## Common Use Cases

### Review a whole app before implementation

Read in order:

1. `app-ux-design.md`
2. `app-navigation-structure-design.md`
3. `ui-layout-overview.md`
4. `design-checklist.md`

### Review a built screen that looks wrong on multiple devices

Read in order:

1. `ui-layout-overview.md`
2. `grid-system.md`
3. `adaptive-layout.md`
4. `responsive-layout.md`
5. `design-checklist.md`

### Review a control or component choice

Read in order:

1. `multimodal-component-overview.md`
2. the specific `multimodal-*.md` file
3. `typical-input-modes.md` if the device input set matters

### Review visual consistency

Read in order:

1. `visual-basis.md`
2. `visual-colors.md`
3. `visual-fonts.md`
4. `visual-icons.md`

### Review motion and transitions

Read in order:

1. `animation-overview.md`
2. `animation-design-principles.md`
3. `transition-animation.md`
4. `gesture-animation.md`

## Search Hints

```bash
rg -n "导航|布局|响应式|自适应|交互|视觉|动效|多态控件|自检" /Users/shpirt/playground/docs/zh-cn/design/ux-design -g '*.md'
```

```bash
rg -n "vp|fp|hover|获焦|悬停|激活态|底部页签|侧边导航|弹出框|搜索框" /Users/shpirt/playground/docs/zh-cn/design/ux-design -g '*.md'
```

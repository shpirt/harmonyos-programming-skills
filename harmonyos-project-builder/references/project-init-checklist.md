# Project Init Checklist

Use this checklist when a HarmonyOS app request sounds complete but the user did not specify enough delivery constraints.

Resolve these items before deep implementation when they materially affect scope:

- target device class: phone only, tablet, wearable, TV, or multi-device
- target API level or known device API when build, install, or SysCap behavior may differ
- delivery goal: compile-only, runnable in DevEco, installable on device, or full demo
- data scope: in-memory sample data, local persistence, remote API, or unspecified
- navigation scope: single-page demo, multi-page app, or undecided
- testing scope: no tests, logic tests only, or logic plus UI smoke test
- validation scope: feature demo, skill validation, or production-like proof

If the user does not answer, choose the narrowest safe defaults and state them:

- prefer phone-first unless the request clearly spans multiple device classes
- prefer in-memory demo data unless persistence is requested
- prefer explicit statement of test scope instead of leaving it implicit
- prefer at least one test path for sample apps built to validate tooling or skills

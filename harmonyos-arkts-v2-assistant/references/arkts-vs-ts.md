# ArkTS Vs TypeScript

Use this reference when code looks acceptable in ordinary TypeScript but fails, warns, or behaves differently in ArkTS or `.ets` files.

## Primary doc entry points

Look under `HARMONYOS_DOCS_ROOT` first, then search the official docs site if local docs are unavailable:

- `application-dev/quick-start/arkts-migration-background.md`
- `application-dev/quick-start/typescript-to-arkts-migration-guide.md`
- `application-dev/faqs/faqs-arkui-arkts.md`

These are the first places to check before giving generic TypeScript advice.

## When to use this reference

Use it for questions like:

- "This TypeScript pattern compiles in TS but fails in ArkTS"
- ".ets compile error that looks like a language restriction"
- "What is the ArkTS equivalent of this TS pattern"
- "Can I use this TypeScript feature in ArkTS"

## Answer pattern

Structure answers in this order:

1. identify the TypeScript habit or construct
2. explain the ArkTS restriction or narrower rule
3. show the HarmonyOS-preferred replacement
4. give a minimal corrected example
5. cite the migration guide, FAQ, or local doc path used

## Common categories to check

### Type-system and syntax restrictions

Check whether the issue is caused by:

- unsupported or narrowed language constructs in ArkTS
- stricter decorator usage or `.ets` placement rules
- incompatible initialization or class-member patterns
- invalid state-variable or UI-struct usage that plain TS would allow

### UI-context restrictions

Some patterns fail not because of pure language syntax, but because ArkUI imposes extra rules in `.ets` files.

Check whether the problem really belongs to:

- component decorators
- state variable declarations
- builder usage
- custom component construction
- context or lifecycle usage

### Migration framing

Do not frame every compatibility fix as a full migration task.

- for a local compile error, provide the smallest ArkTS-compatible fix first
- for repeated patterns across a file or module, mention a broader migration path second

## Search hints

```bash
rg -n "TypeScript|ArkTS语法|迁移指导|适配规则|语法使用常见问题" "$HARMONYOS_DOCS_ROOT" -g '*.md'
```

```bash
rg -n "any|unknown|declare|interface|type |keyof|typeof|infer|as const|namespace|enum|decorator" . -g '*.ets' -g '*.ts'
```

## Output guidance

For ArkTS-versus-TS questions:

- say explicitly whether the issue is `language compatibility`, `ArkUI rule`, or both
- prefer one minimal ArkTS-valid rewrite over multiple speculative alternatives
- avoid generic TS-only advice when the file is clearly `.ets`

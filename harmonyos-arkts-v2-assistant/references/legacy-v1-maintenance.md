# Legacy ArkUI V1 Maintenance

Use this reference when the target codebase still relies on classic ArkUI V1 decorators and the user did not explicitly ask for migration.

## Maintenance stance

- Default to preserving V1 semantics for narrow fixes
- Do not mix V2 decorators into a local V1 repair unless the user asked for migration
- Prefer explaining the current V1 ownership and refresh model before proposing changes
- If the real fix would be large, separate:
  - immediate V1-compatible repair
  - optional V2 migration path

## Common V1 decorators to recognize

- `@State`
- `@Prop`
- `@Link`
- `@Provide`
- `@Consume`
- `@StorageLink`
- `@StorageProp`
- `@Watch`
- `@Observed`
- `@ObjectLink`

## Typical V1 maintenance questions

### Parent-child sync

Check whether the code intends:

- one-way init with local child ownership
- parent-driven refresh
- two-way binding through `@Link`
- dependency-style propagation through `@Provide` and `@Consume`

Do not replace `@Link` with V2 patterns in a narrow repair unless migration is in scope.

### Storage-backed state

For `@StorageLink` and `@StorageProp` issues:

- verify the storage key is correct
- verify the value type matches the stored data
- check whether the code depends on old null or undefined behavior
- check release notes if compilation or runtime behavior changed across platform versions

### Nested refresh problems

For objects nested under `@State`:

- plain `@State` only covers top-level replacement well
- nested object mutation may need `@Observed` and `@ObjectLink`
- do not jump to V2 unless the task actually includes migration

### Watchers and side effects

For `@Watch` issues:

- verify the watched field name is valid
- check whether the callback depends on ordering or initialization timing
- verify decorator key validation if the compiler reports stricter checks

## Suggested doc and search entry points

Look for these topics under `HARMONYOS_DOCS_ROOT` first, then the official docs site if local docs are unavailable:

- `arkts-link.md`
- `arkts-state.md`
- `arkts-prop.md`
- `arkts-provide-and-consume.md`
- `arkts-storage-link.md`
- `arkts-storage-prop.md`
- `arkts-watch.md`
- `arkts-observed-and-objectlink.md`

Also inspect release notes when a previously working V1 pattern now fails after SDK upgrades.

## Fast search hints

```bash
rg -n "@State|@Prop|@Link|@Provide|@Consume|@StorageLink|@StorageProp|@Watch|@Observed|@ObjectLink" "$HARMONYOS_DOCS_ROOT" "$HARMONYOS_SAMPLES_ROOT" -g '*.md' -g '*.ets'
```

```bash
rg -n "@State|@Prop|@Link|@Provide|@Consume|@StorageLink|@StorageProp|@Watch|@Observed|@ObjectLink" . -g '*.ets'
```

## Output guidance

When answering legacy V1 maintenance questions:

- explicitly say the answer is `V1-compatible`
- keep examples in V1 unless migration is requested
- explain whether the bug is caused by ownership, refresh depth, storage binding, or decorator misuse

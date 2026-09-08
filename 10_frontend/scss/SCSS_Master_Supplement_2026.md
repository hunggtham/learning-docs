# SCSS Master Supplement — Dart Sass Deep Dive (2026)

> Đọc sau:
>
> ```text
> SCSS_Beginner_to_Senior_2026.md
> ```
>
> File này không lặp syntax cơ bản. Nó bổ sung các phần cần để đi từ **Senior SCSS → Sass library/tooling specialist**:
>
> ```text
> module identity
> canonical URLs
> configuration lifecycle
> advanced meta programming
> selector algebra
> deep lists/maps
> recursion
> Sass value model
> calculations
> CSS compatibility
> deprecations
> migrator
> JS API
> custom importers/functions
> embedded protocol awareness
> package/library design
> testing
> performance
> release engineering
> ```

---

# 0. Mastery Boundary

Để “master SCSS” cần phân biệt 3 layer:

```text
Sass Language
→ Sass Compiler / Module Loader
→ Generated CSS / Browser
```

Và khi tích hợp build:

```text
SCSS
→ Dart Sass
→ PostCSS / transforms
→ minification
→ bundler
→ browser
```

Nhiều bug được gán “SCSS” thực ra nằm ở:
- load resolution,
- CSS cascade,
- bundler,
- deprecated dependency,
- source map,
- post-processing.

---

# 1. Dart Sass as Language Reference

Modern Sass development thực tế xoay quanh Dart Sass.

Các implementation cũ:
```text
Ruby Sass
LibSass / node-sass
```

không hỗ trợ đầy đủ module system hiện đại.

## Master rule

Nếu một package vẫn yêu cầu node-sass/LibSass compatibility:
- treat as legacy constraint,
- don't let it define new architecture.

---

# 2. CSS Compatibility Is a Core Sass Design Constraint

Sass cố gắng là CSS-compatible superset.

Khi CSS thêm syntax mới:
- slash separators,
- native nesting,
- Color 4,
- CSS function names,

Sass đôi khi phải deprecate old language behavior.

Đây là nguồn của nhiều breaking changes.

## Mental model

```text
CSS evolves
→ syntax conflict appears
→ Sass warns/deprecates
→ Sass changes semantics
```

---

# 3. Module Identity [DEEP]

`@use` không đơn thuần paste file.

Compiler resolves URL tới **canonical module identity**.

Một module canonicalized giống nhau:
- load once,
- execute once,
- CSS emit once.

Điều này làm module system predictable hơn `@import`.

---

# 4. Canonical URLs [DEEP]

Importer resolves user URL:

```text
"tokens"
```

thành canonical URL đại diện module duy nhất.

Nếu cùng physical module được canonicalize thành 2 URLs khác nhau:
- duplicate module load có thể xảy ra,
- CSS/config/state có thể khác expectation.

## Library/tooling concern

Custom importers phải implement canonicalization đúng.

---

# 5. Module Execution Model [DEEP]

Một Sass module:
1. dependencies load,
2. top-level statements execute,
3. members defined,
4. CSS generated,
5. module cached.

Import graph gần giống programming-language modules hơn text includes.

---

# 6. Configuration Timing [MUST]

```scss
@use "theme" with (
  $brand: red
);
```

Configuration áp khi module **first loaded**.

Nếu module đã load earlier:

```scss
@use "theme";
@use "theme" with (...);
```

configuration conflict/error.

## Design pattern

Centralize configuration in one entrypoint.

---

# 7. Configuration Ownership [ARCH]

Bad:

```text
component A configures theme
component B also configures theme
```

Good:

```text
application entrypoint
→ configures design system once
→ components @use configured module
```

---

# 8. Forward-before-use Pattern [ARCH]

Facade:

```scss
@forward "core" with (...);
@use "core";
```

Reason:
- downstream config can reach forward first,
- current module can then use same configured instance.

---

# 9. Private Configuration Deprecation [2026]

Modern Dart Sass deprecates configuring private variables via `with`.

Private members are implementation details.

## Rule

If consumers need to configure value:
- make it public intentionally,
- document it.

Do not use private naming and still expose config.

---

# 10. Public API Surface Audit [ARCH]

For each module list:

```text
public variables
public mixins
public functions
forwarded members
configuration variables
CSS side effects
```

Treat emitted CSS itself as part of public behavior.

---

# 11. CSS Side-effect Modules vs Tool Modules [ARCH]

## Tool module

```text
functions
mixins
variables
no CSS emitted on load
```

## CSS side-effect module

```scss
.button { ... }
```

emits CSS when used.

Separate them where practical.

Pattern:

```text
tools/
components/
```

Prevents accidental CSS emission from utility imports.

---

# 12. Side-effect-free Token Module [ARCH]

```scss
// _tokens.scss
$spacing: (...);
$colors: (...);

@function ... {}
```

No selector output.

Any consumer can `@use` safely.

---

# 13. CSS Emission Entry Point [ARCH]

Library may expose:

```text
library
library/css
library/tools
```

Concept:
- tools for Sass consumers,
- CSS entrypoint for full styles.

Avoid surprising consumer:
> I used one function and 200KB CSS appeared.

---

# 14. `meta.load-css()` Deep Use [ADV]

`meta.load-css()` loads CSS from module in dynamic context.

Unlike `@use`:
- useful inside mixins,
- designed for CSS loading, not member access.

Pattern:
```text
Configuration/condition
→ meta.load-css()
→ conditional CSS emission
```

Use sparingly.

---

# 15. `meta.module-variables()` [ADV]

Reflection over loaded module public members.

Concept:

```scss
@use "sass:meta";
@use "tokens";

$vars:
  meta.module-variables("tokens");
```

Returns map of variables.

Use cases:
- token export tooling,
- documentation generation,
- validation.

---

# 16. `meta.module-functions()` [ADV]

Get functions exposed by module.

Can build generic plugin/dispatch systems.

## Warning

Reflection increases abstraction cost.

Normal apps usually do not need.

---

# 17. `meta.module-mixins()` [ADV]

Modern Dart Sass can expose mixin references from module.

Use:
- framework-level composition,
- introspection tooling.

Don't dynamically call everything just because possible.

---

# 18. First-class Functions [ADV]

```scss
$fn:
  meta.get-function("scale");
```

Then:

```scss
$result:
  meta.call($fn, ...);
```

Pattern:
- strategy function,
- mapping pipeline.

---

# 19. First-class Mixins [ADV]

Modern Sass supports mixin references via meta APIs.

Concept:
```text
retrieve mixin
→ meta.apply
```

Useful advanced library technique.

---

# 20. Strategy Pattern in Sass [ARCH]

Different transform functions:

```text
linear
modular
fluid
```

Select function reference from config.

Then apply generic generator.

Equivalent to Strategy Pattern at compile time.

---

# 21. Higher-order Sass Pattern [ADV]

Function receiving/using function reference:

```text
data
+ transformation function
→ transformed data
```

Useful:
- token processors,
- scale generation.

Keep API narrow.

---

# 22. Argument Lists as Data [DEEP]

`$args...` is special argument-list value.

It can retain:
- positional arguments,
- keyword arguments.

`meta.keywords($args)` returns keyword map.

This is more than ordinary list semantics.

---

# 23. Rest Argument Placement Deprecations [2026]

Modern Sass tightened rules around misplaced rest arguments.

Rule:
- arbitrary/rest arguments belong where signature/call syntax expects,
- don't rely on permissive historical parsing.

Treat deprecation warnings as errors-to-fix.

---

# 24. Keyword Argument Compatibility [ARCH]

Public function:

```scss
@function token(
  $name,
  $fallback: null
) {}
```

Consumers may call:

```scss
token(
  $name: brand,
  $fallback: red
)
```

Rename `$fallback`:
→ potentially breaking API.

Library migration:
- temporarily accept old keyword where possible,
- issue warning,
- document major release.

---

# 25. Sass List Model [DEEP]

A list carries:
- elements,
- separator: space/comma/slash,
- bracketed flag.

Examples:

```text
a b c
a, b, c
a / b
[a, b]
```

These are not always interchangeable.

---

# 26. Single Values Are List-like [DEEP]

Sass list functions may treat:

```scss
10px
```

as a one-element list.

This can surprise validation logic.

Don't detect “is list” merely with naive assumptions.

---

# 27. Maps Are List-like [DEEP]

Map:

```scss
(a: 1, b: 2)
```

can behave as list of two-element pairs in list functions.

Powerful but dangerous for generic code.

Prefer map APIs when semantics are map.

---

# 28. Empty List / Empty Map Ambiguity [DEEP]

Historically `()` can represent empty list/map semantics depending context.

Reflection/type behavior must be understood when building generic functions.

Avoid API relying on ambiguous emptiness.

---

# 29. Slash-separated Lists [DEEP]

Modern Sass treats `/` as CSS-friendly separator direction.

Create intentionally with appropriate list APIs where needed.

Do not use `/` arithmetic.

---

# 30. Immutability Mental Model [ADV]

Sass list/map functions generally return modified copies rather than mutate in place.

```scss
$new:
  map.set(
    $old,
    key,
    value
  );
```

Think functional data transformations.

---

# 31. Deep Map Operations [ADV]

Modern `sass:map` supports nested operations:
- nested `get`,
- `set`,
- deep merge,
- deep remove.

Good for hierarchical token systems.

## Rule

If nested depth > 3–4 and every call uses long key paths:
- reconsider token data model.

---

# 32. Deep Merge Semantics [ADV]

Need define:
- does nested map recursively merge?
- does scalar replace map?
- what happens key collision?

Do not use deep merge blindly for themes.

Test resulting map.

---

# 33. Recursive Functions [ADV]

Sass allows recursive functions/mixins.

Use:
- flatten nested tokens,
- tree processing.

Example conceptual:

```scss
@function flatten($map, $prefix: null) {
  ...
}
```

---

# 34. Recursion Risks [ADV]

Risks:
- hard debug,
- compiler work,
- accidental infinite recursion,
- unclear output.

Prefer iterative `@each` for shallow known structures.

---

# 35. Recursive Token Flattener Pattern [ARCH]

Input:

```scss
(
  color: (
    text: (
      default: #111
    )
  )
)
```

Output conceptual:

```text
color-text-default: #111
```

Useful:
- CSS variable export,
- JSON-like token source.

But if design token system already has external tooling, don't duplicate it in Sass.

---

# 36. Sass Value Equality [DEEP]

`==` compares Sass values semantically according to Sass rules.

Units/colors can create interesting equivalences/conversions.

Do not assume string representation equality.

---

# 37. Numbers with Units as Algebra [DEEP]

Sass internally tracks numerator/denominator units.

Operations can produce compound units.

Example conceptual:

```text
px * px
px / s
```

Not all compound units valid CSS output.

Functions should validate output expectations.

---

# 38. `math.compatible()` [ADV]

Use before arithmetic requiring compatible units.

Example:
```scss
@if not math.compatible($a, $b) {
  @error "...";
}
```

Good robust library design.

---

# 39. Unitless Zero Pitfall [DEEP]

CSS often allows unitless `0`.

But Sass unit algebra:
```text
0
0px
```
can differ in function compatibility/type logic.

Don't strip units blindly.

---

# 40. CSS Calculations as Sass Values [DEEP]

Modern Sass represents calculation expressions such as:
- `calc`,
- `min`,
- `max`,
- `clamp`,
and may simplify compatible parts.

Do not assume every function call returns plain number.

Generic library code may need `meta.type-of()` awareness.

---

# 41. Calculation Preservation [ADV]

Goal:
- simplify compile-time known math,
- preserve browser-dependent math.

Example:

```scss
$gutter: 2rem;

.container {
  width:
    calc(100% - #{$gutter});
}
```

Modern Sass often supports interpolation-free calculation syntax too; prefer current clean syntax if compiler handles it.

---

# 42. CSS Function Name Collisions [DEEP]

CSS keeps adding functions.

Sass historically had global functions with same names.

This is one reason:
- module namespaces,
- global built-in deprecation,
- plain CSS function handling evolve.

Master rule:
> namespaced Sass function when you mean Sass computation.

---

# 43. Legacy `if()` Function Deprecation [2026]

Sass has historically had legacy `if()` function syntax.

Modern CSS is developing native conditional/value functions, creating compatibility pressure.

Recent Sass deprecates legacy `if()` form toward newer syntax/semantics.

Rule:
- follow current Dart Sass migration guidance,
- don't build new library API around deprecated legacy form.

---

# 44. Functions/Mixins Beginning `--` [2026]

Sass deprecated user Sass function/mixin names beginning with `--`.

Reason:
- reserve compatibility space for possible native CSS functions/mixins style syntax.

Do not define:

```scss
@mixin --foo {}
@function --bar() {}
```

---

# 45. Adjacent Compound Selector Changes [2026]

Recent/coming Sass changes tighten selectors with adjacent compounds to match CSS parsing/selector compatibility.

If code relies on exotic generated selector concatenation:
- run deprecation-clean build,
- inspect current breaking changes docs.

---

# 46. Selector Algebra [DEEP]

`sass:selector` treats selectors structurally, not strings.

Operations:
- unify,
- extend,
- replace,
- nest,
- append.

This is effectively selector algebra.

---

# 47. `selector.unify()` [ADV]

Goal:
find selector matching elements that match both inputs.

Concept:

```text
.foo + .bar
```

may unify depending structure.

Useful for advanced mixin generation.

---

# 48. `selector.is-superselector()` [ADV]

Checks if all elements matched by selector B are also matched by A.

Useful:
- framework validation,
- selector relationship reasoning.

---

# 49. Avoid String-built Selectors [MASTER]

Bad advanced code:
```scss
$selector:
  ".foo" + " > " + ".bar";
```

Better:
- interpolation for simple known case,
- `sass:selector` for structural manipulation.

Strings lose selector semantics.

---

# 50. `@extend` Algorithm Awareness [DEEP]

Extend performs selector transformation across stylesheet/module extension scope.

It may:
- unify compound selectors,
- generate permutations,
- trim redundant selectors.

This complexity explains output surprises.

---

# 51. Extend Scope under Module System [ADV]

Module system makes extension behavior more controlled than global legacy imports.

Still:
- extension crosses certain module relationships,
- understand dependency direction.

Avoid designing public library where consumers depend heavily on hidden extends.

---

# 52. Optional Extend [ADV]

`@extend ... !optional` avoids error if target not found.

Use:
- framework extension hooks where target genuinely optional.

Don't use to hide typo silently.

---

# 53. `@at-root` Query Syntax [DEEP]

Advanced `@at-root` can include/exclude rule types.

Concept:

```scss
@at-root
  (without: media) {
  ...
}
```

or with rule categories depending syntax.

Useful library metaprogramming.

Rare app-level need.

---

# 54. Bubbling At-rules [DEEP]

Sass historically “bubbles” nested at-rules such as media/supports outward while preserving selector context.

Example source:

```scss
.card {
  @media (...) {
    color: red;
  }
}
```

Compiler emits media wrapping `.card`.

Understand this when output order matters.

---

# 55. CSS Native Nesting Compatibility [MASTER]

SCSS nesting and native CSS nesting overlap but are not identical languages historically.

Modern Sass continually aligns CSS compatibility.

If publishing plain CSS source:
- don't assume SCSS nesting syntax always equals browser nesting semantics.

Compile SCSS.

---

# 56. Interpolation Changes Semantics [DEEP]

Inside some Sass contexts, interpolation can turn typed values into unquoted strings.

Example:
```scss
#{$number}
```

may lose numeric semantics for subsequent Sass operations.

Rule:
- interpolate at output boundary,
- keep typed Sass values internally.

---

# 57. Stringification Boundary Pattern [ARCH]

Internal:
```text
typed number/color/map
```

Only final:
```text
interpolate into selector/custom property/name
```

Equivalent:
> stringify late.

---

# 58. Modern Color 4 Model [MUST]

Colors now have:
- color space,
- channels,
- potentially missing channels,
- gamut differences.

Old assumption:
```text
color = RGB-like tuple
```
is insufficient.

---

# 59. `color.channel()` [ADV]

Use explicit space where ambiguity exists.

Concept:

```scss
color.channel(
  $color,
  "red",
  $space: rgb
)
```

Different from display-p3 red channel.

---

# 60. `color.to-space()` [ADV]

Convert representation to target color space where supported.

Use:
- library transforms,
- explicit palette calculations.

Conversion may alter gamut representation.

---

# 61. `color.adjust()` vs `color.scale()` [ADV]

## Adjust

Adds/subtracts channel amount.

## Scale

Moves channel proportionally toward min/max.

For design systems, `scale` often behaves more consistently across starting values.

But choose based on desired math, not rule-of-thumb.

---

# 62. Gamut Mapping Awareness [DEEP]

Wide-gamut colors may not display in target gamut.

Sass/browser conversion can involve out-of-gamut channels or mapping concerns.

Master color tooling should:
- choose color space explicitly,
- test output on actual browsers/displays.

---

# 63. Compile-time Color vs Runtime Color [MASTER]

If source is:

```css
var(--brand)
```

Sass does not know actual runtime color.

Cannot do:

```scss
color.scale(var(--brand), ...)
```

as if it were Sass color.

Use CSS:
- `color-mix`,
- relative colors,
- runtime color functions.

---

# 64. Dynamic CSS Variable Generator [ADV]

Function/mixin should preserve:
- numbers with units,
- strings,
- colors,
- booleans/null semantics.

Need define:
- how to serialize list?
- how to serialize map leaf?
- should null skip?
- should quoted string keep quotes?

A production generator needs explicit policy.

---

# 65. CSS Variable Serialization Policy [ARCH]

Example rules:

```text
number → emit as-is
color  → emit as-is
string → emit controlled interpolation
null   → skip
map    → recurse
list   → emit only if explicitly allowed
```

Don't rely on accidental `inspect()` output as production format.

---

# 66. Token Collision Detection [ADV]

Flatten:

```text
color-text
```

could arise from:
```text
(color: (text: ...))
```

and another source key.

Generator should detect duplicates and `@error`.

---

# 67. Token Schema Validation [ARCH]

Validate:
- required groups,
- allowed types,
- naming,
- no null where forbidden.

Sass has no static type system, so library must enforce contracts manually.

---

# 68. Sass as a Weakly Typed DSL [MASTER]

Sass supports typed runtime values but no compile-time interface/type declarations like TypeScript.

Therefore robust library relies on:
- `meta.type-of`,
- unit checks,
- map key checks,
- explicit errors.

---

# 69. Defensive Function Pattern [ARCH]

```scss
@function require-number(
  $value,
  $name
) {
  @if meta.type-of($value) != "number" {
    @error "#{$name} must be number.";
  }

  @return $value;
}
```

Use for reusable library boundaries, not every local helper.

---

# 70. Error Message Design [ARCH]

Bad:
```text
invalid
```

Good:
```text
token("space", 99):
unknown spacing key `99`.
Expected one of: 0,1,2,4,6.
```

Compiler errors are developer UX.

---

# 71. Deprecation API Design [ARCH]

If own library replaces API:

```scss
@mixin old-button(...) {
  @warn "old-button() is deprecated. Use button().";
  @include button(...);
}
```

Maintain bridge for one version window when feasible.

---

# 72. Deprecation Warnings as Product UX [MASTER]

A warning should say:
1. what deprecated,
2. replacement,
3. removal version/window if known,
4. migration link if library has docs.

---

# 73. Sass Migrator Architecture [ADV]

Sass Migrator can mechanically rewrite source for supported migrations.

Typical:
- module migration,
- division migration.

It operates on dependency graph with flags for dependencies/load paths.

Always:
- commit first,
- migrate,
- inspect diff,
- compile,
- visual regression.

---

# 74. Module Migration Is Architectural [MASTER]

Mechanical:
```text
@import → @use
```

but real questions:
- namespaces?
- public API?
- circular dependencies?
- configuration owner?
- CSS side effects?
- private variables?
- extend relationships?

Don't accept auto output without redesign.

---

# 75. Circular Dependency [DEEP]

Module systems generally cannot support arbitrary cycles like text import did.

Example:

```text
A @use B
B @use A
```

indicates architecture problem.

Fix:
- extract shared C,
- invert dependency,
- move config.

---

# 76. Dependency Inversion in Sass [ARCH]

Bad:
```text
tokens → components
components → tokens
```

Good:
```text
settings/tokens
↓
tools
↓
components
```

Dependencies point downward.

---

# 77. Layered Sass Dependency Graph [ARCH]

Recommended:

```text
settings
  ↓
tools
  ↓
runtime-token emission
  ↓
base/layout/components/utilities
```

A lower layer shouldn't depend on upper component.

---

# 78. CSS Cascade Layer + Sass Module Layer [MASTER]

They solve different problems.

Sass module:
```text
compile-time visibility/dependency
```

CSS `@layer`:
```text
runtime cascade precedence
```

Can combine:

```scss
@use "components/button";

@layer components {
  // emitted styles
}
```

Or component files themselves emit within designated CSS layer.

---

# 79. Avoid Naming Collision: “Module” vs “Layer”

Keep vocabulary:

```text
Sass module = @use/@forward
CSS layer   = @layer
```

They are orthogonal.

---

# 80. Sass JS API [ADV]

Dart Sass exposes JavaScript APIs for programmatic compilation.

Modern APIs include concepts:
- compile / compileString,
- async variants,
- importers,
- custom functions,
- logger,
- options.

Avoid legacy JS API.

---

# 81. Modern JS API vs Legacy JS API [MUST for tooling]

Legacy Node Sass-style APIs have been deprecated.

For new tooling:
- use Dart Sass modern API.

Check current JS API docs for exact signatures.

---

# 82. Programmatic Compile Pattern

Concept:

```js
import * as sass from "sass";

const result =
  sass.compile("src/main.scss", {
    style: "compressed"
  });

console.log(result.css);
```

Exact package/module syntax depends project environment.

---

# 83. `compileString()` Use Case

Compile dynamically generated Sass string:
- playground,
- editor,
- test harness.

Do not compile user-controlled Sass server-side without security/resource considerations.

---

# 84. Custom Functions from JS [ADV]

Host language can expose function to Sass.

Use cases:
- read design token source,
- integrate build metadata,
- domain-specific computation.

Risk:
- build becomes non-portable,
- function unavailable outside custom toolchain.

---

# 85. Custom Function Boundary [ARCH]

Before adding JS custom function ask:

```text
Could data be generated before Sass?
Could CSS variable solve runtime need?
Could Sass map solve compile-time need?
```

Custom host functions should be last-mile integration.

---

# 86. Custom Importers [ADV]

Importer controls module URL resolution/loading.

Use:
- virtual modules,
- package aliases,
- custom storage.

Requires correct:
- canonicalization,
- loading,
- syntax identification.

Tooling-specialist territory.

---

# 87. Importer Canonicalization Contract [DEEP]

If importer returns inconsistent canonical URL:
- same module may load multiple times,
- configuration semantics break,
- CSS duplicate.

Canonical URL must represent stable module identity.

---

# 88. File Importer vs Custom Importer

Modern JS API distinguishes importer styles depending use case.

Choose simplest built-in/file importer/load path before custom code.

---

# 89. Logger API [ADV]

Programmatic Sass compilation can intercept:
- warnings,
- debug messages,
- deprecations.

CI can:
- collect,
- classify,
- fail on first-party warnings.

---

# 90. Deprecation Controls [ADV]

Dart Sass offers controls for:
- silence selected deprecations,
- future/fatal deprecations,
- dependency warning behavior,

through CLI/API depending version.

Policy:
- never global-silence indefinitely.

---

# 91. CI Deprecation Budget Pattern [ARCH]

```text
first-party warnings = 0
dependency warnings  = tracked separately
```

Then:
- upgrade dependencies,
- maintain allowlist with expiry.

---

# 92. Compilation Performance [ADV]

Factors:
- module graph,
- file I/O,
- huge loops,
- selector extension,
- recursion,
- generated CSS volume,
- custom importers/functions.

Module system loads once, improving duplication compared to legacy imports.

---

# 93. Measure Compile Time [MASTER]

Do not optimize by guess.

Track:
```text
cold build
warm watch rebuild
CSS bytes
source map bytes
module count
```

Set regression thresholds for very large design systems.

---

# 94. Generator Performance [ADV]

Nested loops:

```text
N × M × K
```

can explode compile work/output.

Example:
```text
20 colors
× 20 states
× 10 breakpoints
= 4000 rule families
```

Ask whether consumer needs all combinations.

---

# 95. Lazy Generation Pattern [ARCH]

Instead of generate every utility:
- explicit enabled utility groups,
- generated from used design scale,
- separate entrypoints.

Sass itself doesn't automatically tree-shake semantic loops.

---

# 96. CSS Output Budget [MASTER]

Define budget:

```text
base CSS <= X KB gzip
utilities <= Y KB
single component <= Z KB
```

Numbers project-specific.

Inspect compiled result, not SCSS lines.

---

# 97. Source Map Cost [ADV]

Development:
- useful detailed maps.

Production:
- source map policy depends debugging/security/deployment.

Sass source maps can be further transformed by downstream tools; ensure chain stays correct.

---

# 98. Build Pipeline Ordering [MASTER]

Common:

```text
SCSS
→ Sass
→ PostCSS
→ prefix
→ optimize/minify
```

Why Sass first?
PostCSS expects CSS, not Sass language, unless special parser/plugin used.

Framework tooling may encapsulate this.

---

# 99. Browserslist Isn't Sass [MUST]

Dart Sass does not decide vendor prefixes from browserslist.

That belongs:
- PostCSS/Autoprefixer,
- bundler transformations.

Don't expect Sass update to fix prefix policy.

---

# 100. Sass + Native CSS Modernization Strategy [MASTER]

As CSS grows:
- reduce Sass-only abstractions that native CSS now handles better.

Candidates:
```text
runtime variables → CSS vars
responsive component → @container
nesting → native CSS if toolchain allows
color runtime → color-mix/relative colors
```

Keep Sass for:
```text
module/package API
compile-time data
generation
validation
```

---

# 101. Migration from Sass Variables to CSS Variables

Before:

```scss
$brand: #2563eb;

.button {
  color: $brand;
}
```

After:

```scss
:root {
  --brand: #2563eb;
}

.button {
  color: var(--brand);
}
```

Do when:
- theme/runtime override matters.

Don't migrate build-only constants with no runtime value just for fashion.

---

# 102. Hybrid Token Pattern [MASTER]

Sass source:

```scss
$tokens: (...);
```

Emit:
```css
:root {
  --...: ...;
}
```

Sass functions can also use same map for generated static fallbacks/utilities.

Single source can serve:
- compile-time generation,
- runtime CSS.

---

# 103. External Design Tokens [MASTER]

Large systems may use JSON/DTCG-like tokens outside Sass.

Pipeline:

```text
token source
→ generator
→ SCSS maps
→ CSS custom properties
→ platform outputs
```

At scale, Sass may be **consumer**, not source of truth.

---

# 104. Don't Parse JSON in Sass [MASTER]

If data source is JSON:
- transform with build tool,
- generate Sass/CSS.

Don't invent JSON parser with string functions in Sass.

Use right language for build task.

---

# 105. Testing Sass Functions [ADV]

Pure functions can be tested with:
- compile fixtures,
- assertion library/ecosystem,
- expected CSS/error snapshots.

Important cases:
- valid,
- boundary,
- invalid type,
- invalid unit,
- unknown key.

---

# 106. Golden CSS Tests [ADV]

Input SCSS:

```text
fixture.scss
```

Expected:
```text
fixture.css
```

Compile and compare.

Good for:
- mixins,
- generators,
- selector manipulation.

Normalize formatting when appropriate.

---

# 107. Error Tests [ADV]

Ensure:

```scss
token(unknown)
```

fails with expected diagnostic.

Public library quality includes failure behavior.

---

# 108. Visual Tests Still Required [MASTER]

Sass unit test can prove:
- generated CSS structure.

Cannot prove:
- browser layout correct,
- accessible interaction,
- cross-browser rendering.

Need CSS visual/component tests.

---

# 109. Snapshot Test Pitfall

Generated CSS snapshot can be huge/noisy.

Prefer:
- targeted fixture,
- semantic assertions,
- stable formatting.

Don't snapshot entire 500KB bundle for every unit test.

---

# 110. Linting SCSS [MUST]

Stylelint with SCSS-aware config/plugins can check:
- Sass at-rules,
- nesting,
- naming,
- deprecated patterns.

Rules should align architecture.

---

# 111. Ban Legacy Constructs [ARCH]

Possible policy:
```text
no Sass @import
no slash division
no global map-get
no old color helpers
no !global
restricted @extend
max nesting
```

Tooling support varies; CI grep/custom lint can supplement.

---

# 112. Package Publishing [ARCH]

Sass package should expose stable entrypoints.

Example conceptual:
```text
package/
├─ scss/
│  ├─ _index.scss
│  └─ ...
└─ dist/
   └─ styles.css
```

Consumers may want:
- precompiled CSS,
- Sass API.

Document both.

---

# 113. Package Resolution [ADV]

Node package Sass imports may be resolved via bundler/importer/package conventions.

Don't rely on undocumented resolution magic.

Publish clear import examples tested in common toolchains.

---

# 114. Version Compatibility Matrix [ARCH]

Library docs:

```text
Library 3.x
requires Dart Sass >= X
```

Needed when using newer:
- module APIs,
- map functions,
- color APIs,
- meta mixins,
- CSS compatibility changes.

---

# 115. LibSass Compatibility Is a Cost

Supporting old implementation means losing:
- `@use`,
- `@forward`,
- built-in module APIs,
- newer language features.

For modern library:
- don't support dead compiler unless business constraint explicit.

---

# 116. Breaking Change Monitoring [MASTER]

Track official Sass breaking changes.

Recent/current themes include:
- imports/global functions,
- Color 4 APIs,
- legacy JS API,
- mixed declarations,
- private configuration,
- legacy if,
- rest args,
- selector parsing,
- CSS function names.

Upgrade Sass proactively in CI.

---

# 117. Pinning vs Floating Compiler Version

Lockfile should make builds reproducible.

But also have periodic dependency update process:
- renovate/dependabot/manual,
- CI on new Sass release if critical library.

Avoid surprise after 2 years frozen.

---

# 118. Upgrade Test Matrix [ARCH]

On Sass upgrade:

```text
compile
deprecation warnings
unit fixtures
visual regression
bundle size
compile time
```

Especially for design system.

---

# 119. Mixed Declaration Migration [2026]

Old Sass historically reordered declarations around nested rules.

Modern Sass follows CSS behavior/order.

Migration strategy:
- keep base declarations grouped,
- avoid relying on historical hoisting,
- inspect compiled order.

---

# 120. Global Built-in Migration [2026]

Mechanical idea:

```scss
map-get(...)
```

→

```scss
@use "sass:map";
map.get(...)
```

Likewise:
- list,
- math,
- color,
- string,
- meta.

Benefit is language compatibility, not just style.

---

# 121. Color Migration [2026]

Old:
```scss
lighten($brand, 10%)
```

Don't mechanically replace with arbitrary function without intent.

Decide:
- adjust absolute lightness?
- scale toward white?
- operate in HSL or Oklch?
- runtime or compile-time?

Color migration is design decision.

---

# 122. Slash Migration [2026]

Arithmetic:
```scss
math.div(...)
```

CSS separator remains:
```scss
grid-row: 1 / 3;
```

Lists may need explicit slash separator APIs for computed Sass list generation.

---

# 123. Avoid Deprecation Cargo Cult

Don't rewrite code solely to silence warning without understanding semantic change.

Process:
```text
read warning
→ read breaking-change page
→ reproduce
→ migrate
→ test output
```

---

# 124. Master Anti-pattern — Sass Framework Inside App

Symptoms:
- 100 generic mixins,
- function dispatch,
- recursive config,
- selector DSL,
- huge generated utilities,
- no one knows output.

If app isn't publishing style framework:
simplify.

---

# 125. Master Anti-pattern — Runtime Logic in Sass

Bad expectation:
```text
if viewport > ...
if user selected dark...
if server data...
```

Sass runs before browser.

Use CSS/JS runtime.

---

# 126. Master Anti-pattern — CSS Hidden Behind Mixins

Source:

```scss
@include card-everything(
  compact,
  elevated,
  responsive
);
```

Reviewer can't see:
- display,
- overflow,
- focus,
- motion.

Use mixins for orthogonal reusable concerns, not whole component behavior unless library abstraction explicitly warrants.

---

# 127. Master Anti-pattern — Over-normalized Token Maps

Example:
```text
tokens.component.button.state.hover.color.background.default...
```

Every lookup 7 keys deep.

This mirrors database normalization, not useful styling.

Prefer semantic flatness where practical.

---

# 128. Master Pattern — Stable Semantic Boundary

Inside library can change:
- color math,
- spacing formula,
- map structure.

Public contract stays:
```text
token("color-action")
@mixin focus-ring
$radius-default config
```

Encapsulation matters even in Sass.

---

# 129. Master Pattern — Build-time Adapter

External token source/vendor:

```text
upstream API
→ adapter module
→ internal canonical values
```

All weird compatibility localized.

---

# 130. Master Pattern — Compile-time Feature Flags

Config:

```scss
$enable-grid-utilities: true !default;
```

Generator:

```scss
@if $enable-grid-utilities {
  ...
}
```

Good for library optional CSS bundles.

Bad for runtime feature state.

---

# 131. Feature Flag Budget

Too many flags create combinatorial test matrix.

Expose only high-value build options.

---

# 132. Master Pattern — Explicit CSS Side Effects

Document module:

```text
@use "library/tools"
→ emits no CSS

@use "library/components"
→ emits components
```

Consumer can reason bundle cost.

---

# 133. Master Pattern — Layer-aware Library

Library can emit CSS in named layer:

```scss
@layer ds.components {
  ...
}
```

Consumer controls global layer order.

This is often better than high specificity.

---

# 134. Library Layer Contract

Document:
```text
ds.reset
ds.base
ds.components
ds.utilities
```

Consumers can define layer ordering early.

Don't hide layer behavior.

---

# 135. Sass Config vs CSS Token Override API

Public library might offer both:

Compile-time:
```scss
@use "lib" with (
  $enable-legacy: false
);
```

Runtime:
```css
:root {
  --lib-brand: ...;
}
```

Different responsibilities.

---

# 136. Master Decision Matrix

## Use Sass variable when:
- compile-time only,
- generation,
- package config.

## CSS variable when:
- runtime theme,
- cascade,
- component override.

## Sass function when:
- compile-time value transformation.

## CSS function when:
- layout/runtime value.

## Mixin when:
- reusable style generation.

## Utility when:
- runtime composition.

## `@forward` when:
- package facade.

## `@extend` when:
- true selector semantic extension.

---

# 137. Performance Decision Matrix

Before generator:
```text
How many selectors?
How many declarations?
How many media variants?
Will users use them?
Can downstream purge safely?
```

Before mixin:
```text
How many include sites?
How large block?
Would runtime class be smaller?
```

---

# 138. Debugging Compile Errors [MASTER]

Workflow:

```text
1. read full Sass diagnostic
2. identify source span
3. check module namespace
4. inspect types with meta.type-of
5. inspect values with @debug/meta.inspect
6. reduce reproduction
7. check deprecation/breaking-change docs
8. inspect generated CSS after fix
```

---

# 139. Debugging Module Errors

Check:
- wrong URL,
- load path,
- namespace collision,
- module configured twice,
- private member access,
- circular dependency,
- importer canonicalization.

---

# 140. Debugging “Wrong CSS”

Determine layer:

```text
SCSS source wrong?
Compiler output wrong?
PostCSS transformed?
Minifier changed?
Browser cascade?
```

Always inspect generated CSS before blaming Sass.

---

# 141. Debugging Type Errors

Print:

```scss
@debug meta.type-of($value);
@debug meta.inspect($value);
```

Check:
- number units,
- map vs list,
- quoted string,
- null,
- calculation.

---

# 142. Debugging Map API

Before `map.get`:
```scss
@debug map.keys($map);
```

Validate nested keys.

Don't let missing map key silently propagate `null` into style unless intentional.

---

# 143. Debugging Color API

Check:
- color space,
- channel name,
- unit,
- whether value is Sass color or CSS runtime string/var.

Modern Color 4 makes implicit assumptions riskier.

---

# 144. Master Lab 1 — Module Graph

Build:
```text
settings
tools
tokens
components
facade
application
```

Verify:
- no cycles,
- config once,
- CSS emitted once.

---

# 145. Master Lab 2 — Sass Library API

Expose:
- 3 config vars,
- 2 functions,
- 2 mixins,
- facade prefix,
- one private helper.

Write consumer examples.

---

# 146. Master Lab 3 — Deep Token Compiler

Input nested map.

Features:
- flatten,
- validate,
- collision detect,
- skip null,
- emit CSS vars.

Add tests.

---

# 147. Master Lab 4 — Color 4 Palette

Use:
- Oklch,
- `color.scale`,
- `color.channel`,
- explicit spaces.

Compare output with CSS runtime color-mix.

---

# 148. Master Lab 5 — Selector Algebra

Use:
- unify,
- nest,
- superselector checks.

Inspect output and document why not string interpolation.

---

# 149. Master Lab 6 — Migrate Legacy Project

Legacy:
```text
@import
map-get
lighten
slash division
global variables
```

Migrate to:
- modules,
- built-ins,
- modern color,
- `math.div`.

Visual diff.

---

# 150. Master Lab 7 — JS API

Programmatically:
- compile file,
- capture warning,
- custom logger,
- source map awareness.

---

# 151. Master Lab 8 — Custom Function

Expose one safe JS custom function.

Then write alternative build step and compare coupling.

---

# 152. Master Lab 9 — Custom Importer

Implement virtual module resolver.

Verify same logical module canonicalizes once.

Tooling-specialist exercise.

---

# 153. Master Lab 10 — Output Budget

Create utility generator.

Measure:
- compile time,
- raw CSS,
- gzip,
- coverage.

Reduce output 30% without losing required API.

---

# 154. Master Self-Test

1. Canonical module URL là gì?
2. Vì sao module load once?
3. Configuration được áp lúc nào?
4. Vì sao configure-after-load fail?
5. Tool module khác CSS side-effect module?
6. `meta.load-css` khác `@use`?
7. Reflection APIs phù hợp khi nào?
8. Argument list khác normal list?
9. Map list-like behavior có pitfall gì?
10. Deep merge cần policy gì?
11. Unit algebra ảnh hưởng function design ra sao?
12. Sass calculation khác number?
13. Vì sao interpolate late?
14. Color space làm old color helpers problematic thế nào?
15. Selector unification là gì?
16. `@extend` không phải declaration copy vì sao?
17. Module dependency cycle sửa thế nào?
18. Sass module vs CSS layer?
19. Modern JS API dùng cho gì?
20. Custom importer cần canonicalize vì sao?
21. Custom function có portability cost gì?
22. Compile performance bottleneck nào?
23. Vì sao source size không đại diện output size?
24. Sass Migrator không thay architecture review vì sao?
25. Private config deprecation nói gì về API design?
26. Global built-in deprecation liên quan CSS compatibility thế nào?
27. Legacy `if()` deprecation liên quan CSS evolution ra sao?
28. `--` Sass function/mixin names vì sao deprecated?
29. Token schema validation thiết kế sao?
30. Generated CSS serialization policy cần gì?
31. External token source nên integrate thế nào?
32. Sass testing khác visual testing?
33. Package nên expose Sass + CSS entrypoints ra sao?
34. Version matrix cần khi nào?
35. Upgrade Sass cần test gì?
36. Mixin duplication vs utility tradeoff?
37. Feature flag compile-time khác runtime?
38. Layer-aware Sass library có lợi gì?
39. Khi nào Sass abstraction đã quá mức?
40. Khi nào bỏ Sass để dùng native CSS?

---

# 155. Mastery Rubric

## Senior SCSS
- modern modules,
- mixins/functions,
- maps,
- architecture,
- clean deprecations.

## Sass Library Engineer
- facade API,
- configuration,
- validation,
- selectors/meta,
- tests,
- versioning.

## Sass Tooling Specialist
- JS API,
- importer,
- custom functions,
- canonical URLs,
- compile diagnostics/performance.

## Master
Có thể:
- thiết kế compile-time API,
- migrate legacy system,
- explain compiler/module behavior,
- predict output cost,
- respond to CSS/Sass language evolution,
- biết khi nào **không dùng Sass**.

---

# 156. Modern 2026 Watchlist

Theo dõi official Sass Breaking Changes cho:
```text
@import removal path
global built-in removal
Color 4 APIs
legacy JS API
private config
legacy if()
rest argument rules
selector parsing
plain CSS function compatibility
mixed declaration semantics
```

Đừng học version-specific workaround như permanent pattern.

---

# 157. Production Checklist

Before merge:

```text
[ ] no Sass @import
[ ] no slash arithmetic
[ ] namespaced built-ins
[ ] no deprecated color helper
[ ] no first-party warnings
[ ] module graph acyclic
[ ] public config intentional
[ ] private internals not leaked
[ ] nesting reasonable
[ ] @extend reviewed
[ ] generated output inspected
[ ] bundle size acceptable
[ ] source maps work
[ ] CSS visual tests pass
[ ] browser behavior tested
```

---

# 158. Reference Map

Official:
- https://sass-lang.com/documentation/
- https://sass-lang.com/documentation/at-rules/use/
- https://sass-lang.com/documentation/at-rules/forward/
- https://sass-lang.com/documentation/at-rules/mixin/
- https://sass-lang.com/documentation/at-rules/function/
- https://sass-lang.com/documentation/modules/
- https://sass-lang.com/documentation/modules/meta/
- https://sass-lang.com/documentation/modules/selector/
- https://sass-lang.com/documentation/js-api/
- https://sass-lang.com/documentation/breaking-changes/
- https://sass-lang.com/documentation/breaking-changes/import/
- https://sass-lang.com/documentation/breaking-changes/slash-div/
- https://sass-lang.com/documentation/breaking-changes/color-functions/

---

# Kết luận

“Master SCSS” không có nghĩa biến Sass thành programming language phức tạp nhất có thể.

Maturity path:

```text
Beginner:
use variables/nesting

Intermediate:
mixins/maps/functions

Senior:
modules + architecture + output discipline

Master:
compiler/module model
+ library API
+ migration
+ tooling
+ compatibility
+ know when native CSS is better
```

Nguyên tắc cuối:

```text
Use Sass to make CSS authoring safer.
Never make CSS behavior harder to understand
just because Sass can generate it.
```

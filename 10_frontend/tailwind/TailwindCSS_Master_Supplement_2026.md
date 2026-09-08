# Tailwind CSS Master Supplement — v4.3 Deep Dive (2026)

> Đọc sau:
>
> `TailwindCSS_Beginner_to_Senior_2026.md`
>
> File này **không lặp lại catalog utility cơ bản**. Nó tập trung vào những phần cần để đi từ Senior Tailwind → Tailwind architecture/tooling/design-system specialist.
>
> Mental model:
>
> ```text
> source/template
> → Tailwind candidate detection
> → utility/variant resolution
> → generated CSS layers/theme variables
> → browser CSS engine
> ```
>
> Ký hiệu:
> - **[MASTER]**: cần hiểu sâu.
> - **[BUILD]**: compiler/build pipeline.
> - **[ARCH]**: design-system/package architecture.
> - **[V4]**: Tailwind v4.
> - **[V4.3]**: current feature trong v4.3.
> - **⚠**: edge case / migration / compatibility.

---

# 0. “Master Tailwind” nghĩa là gì?

Không phải nhớ toàn bộ utility.

Một Tailwind master phải phân biệt được lỗi nằm ở đâu:

```text
1. Template/source
2. Candidate scanner
3. Tailwind resolver
4. Generated CSS
5. Browser layout/cascade
```

Ví dụ:

```text
class không được generate
→ thường layer 1–3

rule có trong CSS nhưng UI sai
→ thường layer 4–5
```

Kỹ năng quan trọng nhất là **biết khi nào ngừng debug Tailwind và chuyển sang debug CSS**.

---

# 1. Tailwind v4 build model [MASTER]

Simplified pipeline:

```text
CSS entrypoint
+ @theme
+ @source
+ @utility
+ @custom-variant
+ scanned source files
        │
        ▼
candidate discovery
        │
        ▼
utility + variant resolution
        │
        ▼
CSS generation
        │
        ▼
browser
```

Tailwind là build-time system, không phải runtime class interpreter.

---

# 2. Candidate scanner không evaluate JavaScript

Bad:

```jsx
const cls = `bg-${color}-600`;
```

Tailwind không chạy JS để biết `color`.

Scanner cần nhìn thấy complete candidate:

```jsx
const colors = {
  blue: "bg-blue-600",
  red: "bg-red-600",
};
```

## CSS relation

CSS không liên quan lỗi này; CSS rule chưa từng được generate.

Đây là build-layer bug.

---

# 3. Static variant map pattern [ARCH]

```ts
const buttonVariants = {
  primary:
    "bg-blue-600 text-white hover:bg-blue-700",
  danger:
    "bg-red-600 text-white hover:bg-red-700",
} as const;
```

Lợi ích:
1. scanner-safe,
2. finite design combinations,
3. TypeScript friendly,
4. easy refactor,
5. semantic API.

Public component:

```tsx
<Button variant="danger" />
```

Internal Tailwind:

```text
bg-red-600 ...
```

---

# 4. Không expose Tailwind token thành domain API

Bad:

```tsx
<Button color="blue-600" />
<Card padding="p-6" />
```

Better:

```tsx
<Button variant="primary" />
<Card density="comfortable" />
```

Tailwind nên là implementation detail bên trong reusable component.

---

# 5. Automatic source detection [BUILD]

Tailwind v4 tự phát hiện source nhưng intentionally ignore nhiều loại path:
- paths trong `.gitignore`,
- `node_modules`,
- binary assets,
- CSS files,
- common lockfiles.

Điều này tối ưu scan nhưng có implication cho shared packages.

---

# 6. `@source` external package

```css
@import "tailwindcss";

@source "../node_modules/@acme/ui-lib";
```

Use khi dependency chứa source templates có Tailwind classes.

Workspace:

```css
@source "../../packages/ui/src";
```

---

# 7. Source base path

```css
@import "tailwindcss"
  source("../src");
```

Rất hữu ích trong monorepo nơi command chạy từ root nhưng stylesheet thuộc app con.

---

# 8. Ignore explicit source

```css
@source not "../src/legacy";
```

Dùng khi:
- large legacy tree,
- source không dùng Tailwind,
- muốn giảm invalidation/scan noise.

---

# 9. Disable automatic scanning

```css
@import "tailwindcss"
  source(none);

@source "../admin";
@source "../shared";
```

Use:
- multiple bundles,
- microfrontends,
- admin/storefront split.

---

# 10. Multiple bundle pattern [ARCH]

`admin.css`:

```css
@import "tailwindcss"
  source(none);

@source "../admin";
@source "../shared";
```

`storefront.css`:

```css
@import "tailwindcss"
  source(none);

@source "../storefront";
@source "../shared";
```

Mục tiêu:
- giảm CSS overlap,
- ownership rõ.

---

# 11. Safelist v4

Thay vì v3 `safelist` config, v4 có:

```text
@source inline(...)
```

Dùng cho utility candidates không xuất hiện literal trong scanned source.

Good:
- finite CMS options,
- generated static docs.

Bad:
- generate toàn palette × breakpoint × state “phòng khi cần”.

---

# 12. Candidate cardinality [BUILD]

Mỗi candidate condition có thể tạo CSS riêng:

```text
bg-blue-500
hover:bg-blue-500
dark:bg-blue-500
md:bg-blue-500
```

Do đó broad safelist có thể nhân output rất nhanh.

---

# 13. Tailwind không phải JS tree-shaking

Đúng mental model:

```text
usage-driven candidate generation
```

Không phải:
```text
ES module tree shaking
```

Điều này giúp bạn reasoning đúng về source detection.

---

# 14. `@theme` có hai vai trò [MASTER]

```css
@theme {
  --color-brand: oklch(.62 .2 255);
}
```

Vai trò 1 — compiler API:

```text
bg-brand
text-brand
border-brand
...
```

Vai trò 2 — runtime CSS token:

```css
--color-brand
```

Đây là điểm khác lớn so với normal CSS variable.

---

# 15. Normal CSS var không tự tạo utility

```css
:root {
  --brand: red;
}
```

Không tự tạo:

```text
bg-brand
```

Nhưng:

```css
@theme {
  --color-brand: red;
}
```

có thể tạo theme-driven color utilities.

---

# 16. Theme namespace là public API [ARCH]

Ví dụ:

```css
@theme {
  --radius-card: .75rem;
}
```

sinh:

```text
rounded-card
```

Đổi token name:
```text
--radius-card
→ --radius-panel
```

là API-breaking change cho markup dùng `rounded-card`.

Treat theme vocabulary như library API.

---

# 17. Strict theme surface

```css
@theme {
  --color-*: initial;

  --color-surface: ...;
  --color-text: ...;
  --color-action: ...;
  --color-danger: ...;
}
```

Lợi:
- dev không dùng arbitrary default palette.

Cost:
- examples/tutorial utilities có thể không tồn tại,
- semantic token context có thể quá rộng.

---

# 18. Primitive vs semantic token

Primitive:

```text
blue-600
gray-200
```

Semantic:

```text
action
surface
muted
danger
```

Large design systems thường cần hai tầng:

```text
primitive
→ semantic
→ component
```

---

# 19. Semantic role can be property-specific

Nếu define:

```text
--color-danger
```

Tailwind có thể cho dùng:
- `bg-danger`,
- `text-danger`,
- `border-danger`.

Nhưng design có thể cần:

```text
danger-bg
danger-fg
danger-border
```

khác màu.

Do đó semantic token design cần đủ specificity về role.

---

# 20. Runtime semantic variable pattern

```css
:root {
  --surface:
    var(--color-white);
  --text:
    var(--color-gray-950);
}

[data-theme="dark"] {
  --surface:
    var(--color-gray-950);
  --text:
    var(--color-white);
}
```

Use:

```html
<div
  class="
    bg-(--surface)
    text-(color:--text)
  "
>
```

Tailwind classes static, values runtime.

---

# 21. `@theme inline` deep reason

```css
@theme inline {
  --font-sans:
    var(--font-inter);
}
```

CSS custom properties resolve based on where variable is defined/evaluated.

`inline` helps generated utility use referenced value directly thay vì indirection có thể resolve ở unexpected scope.

---

# 22. `@theme static`

```css
@theme static {
  --color-brand: ...;
}
```

Forces theme variables emit dù không có matching utility usage.

Good:
- JS needs `getComputedStyle`,
- animation library references variable,
- shared theme package.

Bad:
- blindly on huge default theme if bundle budget tight.

---

# 23. Sharing theme package

```text
packages/
└─ brand/
   └─ theme.css
```

```css
@theme {
  --color-brand: ...;
  --font-brand: ...;
}
```

App:

```css
@import "tailwindcss";
@import "@company/brand/theme.css";
```

V4 CSS-first makes cross-project theme sharing much simpler than JS preset-only mental model.

---

# 24. Breakpoint token = behavior contract

```css
@theme {
  --breakpoint-md: 52rem;
}
```

Changing it changes every:

```text
md:*
```

through whole app.

This is not a cosmetic token change.

Treat breakpoint change as system-level behavior release.

---

# 25. Viewport vs container thresholds

Do not copy:

```text
sm/md/lg
```

values blindly into container size tokens.

Viewport breakpoint answers:
> page/window rộng bao nhiêu?

Container breakpoint answers:
> component có bao nhiêu space?

Hai systems có thể có different thresholds.

---

# 26. Container queries ownership

Use:

```text
md:
```

for page layout.

Use:

```text
@md:
```

for reusable component internals.

This single distinction prevents many responsive architecture problems.

---

# 27. `@container-size` [V4.3]

Regular:

```text
@container
```

creates inline-size container.

New v4.3:

```text
@container-size
```

creates size container.

Need `@container-size` when:
- block dimension matters,
- using `cqb`/`cqh`,
- querying height-like dimension.

---

# 28. Size containment side effect

CSS size containment changes sizing behavior more strongly than inline-size containment.

Therefore:

```text
@container-size
```

should not replace every `@container`.

Use only when block size information is needed.

---

# 29. Container query units

Tailwind arbitrary value exposes CSS units:

```text
w-[50cqw]
text-[5cqi]
h-[50cqb]
```

No custom plugin needed.

Framework doesn't abstract away CSS capability.

---

# 30. Functional `@utility` [MASTER]

```css
@utility tab-* {
  tab-size:
    --value(
      --tab-size-*,
      integer,
      [integer]
    );
}
```

This is a declarative mini-parser for a utility family.

Tailwind:
1. match prefix,
2. parse candidate value,
3. try resolvers,
4. emit valid declaration.

---

# 31. Theme resolver

```css
@theme {
  --tab-size-github: 8;
}

@utility tab-* {
  tab-size:
    --value(--tab-size-*);
}
```

Supports:

```text
tab-github
```

Does not necessarily accept arbitrary bare values unless you add other resolvers.

---

# 32. Bare resolver

```css
@utility tab-* {
  tab-size:
    --value(integer);
}
```

Supports:

```text
tab-2
tab-76
```

Bare type set is intentionally constrained.

---

# 33. Literal resolver

```css
@utility tab-* {
  tab-size:
    --value(
      "inherit",
      "initial",
      "unset"
    );
}
```

Supports:

```text
tab-inherit
tab-initial
tab-unset
```

---

# 34. Arbitrary resolver

```css
@utility tab-* {
  tab-size:
    --value([integer]);
}
```

Supports:

```text
tab-[12]
```

Arbitrary resolver types include CSS-like categories such as:
- length,
- color,
- percentage,
- angle,
- ratio,
- image,
- number,
- integer,
- etc.

---

# 35. Multi-source resolver

```css
@utility tab-* {
  tab-size:
    --value(
      --tab-size-*,
      integer,
      [integer]
    );
}
```

Resolver order matters when ambiguous.

Design utility grammar intentionally.

---

# 36. Different transform per source type

```css
@utility opacity-* {
  opacity:
    --value([percentage]);

  opacity:
    calc(
      --value(integer) * 1%
    );

  opacity:
    --value(--opacity-*);
}
```

Declarations whose value cannot resolve are omitted.

This lets theme/bare/arbitrary values transform differently.

---

# 37. Negative custom utilities

Need separate utility family:

```css
@utility inset-* {
  inset:
    --spacing(
      --value(integer)
    );
}

@utility -inset-* {
  inset:
    --spacing(
      --value(integer) * -1
    );
}
```

Tailwind doesn't assume every utility has valid negative semantics.

---

# 38. Modifier model

Candidate:

```text
text-lg/7
```

Concept:

```text
value = lg
modifier = 7
```

Functional utility:

```css
line-height:
  --modifier(...);
```

Use modifier only khi secondary value has obvious relationship.

---

# 39. `--default()` [V4.3]

```css
@utility tab-* {
  tab-size:
    --value(
      integer,
      --default(4)
    );
}
```

Now:

```text
tab
→ 4

tab-2
→ 2
```

Bare utility should only exist when default is intuitive.

---

# 40. `--modifier()` default

V4.3 also allows default modifier semantics via `--default()` inside modifier resolution.

Good for APIs where:
- value required or optional,
- modifier has natural default.

Avoid clever syntax nobody can predict.

---

# 41. Utility API design rules [ARCH]

Good utility:
- atomic concern,
- predictable prefix,
- token-friendly,
- arbitrary escape hatch only where useful,
- negative only when CSS accepts,
- modifier with clear meaning.

Bad:

```text
super-card-rounded-blue-lg
```

That's component abstraction, not utility.

---

# 42. Custom utility sorting

V4 custom utilities are sorted based partly on number of declarations/properties, helping multi-property component-like utilities remain overrideable by atomic utilities.

Implication:
**do not rely on file order** as conflict architecture for custom utilities.

---

# 43. `@utility` vs component class

Use `@utility`:

```css
@utility content-auto {
  content-visibility:auto;
}
```

Use component class:

```css
@layer components {
  .select2-dropdown {
    ...
  }
}
```

Use framework component abstraction for:
- Button,
- Dialog,
- Card,
- Tabs,
when structure/state/API belong together.

---

# 44. Variant = CSS transform

Variants modify generated CSS.

Examples:

```text
hover:
→ selector transformation

md:
→ media query

dark:
→ media/selector depending custom definition

supports-*:
→ @supports

group-*:
→ ancestor selector relation

peer-*:
→ sibling selector relation
```

Understanding this makes stacked variants predictable.

---

# 45. Variant stacking

```text
dark:md:hover:bg-blue-600
```

doesn't mean class magic.

It composes:
- dark condition,
- media condition,
- hover selector.

Debug by inspecting generated CSS structure.

---

# 46. `@custom-variant` as selector macro

Repeated arbitrary selector:

```text
[&:where([data-theme=midnight] *)]
```

promote:

```css
@custom-variant theme-midnight
  (&:where([data-theme="midnight"] *));
```

Then:

```text
theme-midnight:bg-black
```

Design language becomes semantic.

---

# 47. Custom variant namespace

Future core variants can grow.

For published design systems consider names:

```text
ds-density-compact:
app-authenticated:
```

if collision risk matters.

---

# 48. `@variant` [V4.3]

Inside custom CSS:

```css
.button {
  @variant hover:focus {
    ...
  }
}
```

Compound:

```css
@variant hover, focus {
  ...
}
```

Use when selector is custom CSS but you want Tailwind variant behavior.

---

# 49. `@reference` [MASTER]

Separate Vue/Svelte/CSS Module stylesheet may not know custom theme/utilities/variants from main Tailwind CSS context.

```css
@reference "../../app.css";

h1 {
  @apply text-2xl;
}
```

Reference:
- makes definitions available,
- doesn't duplicate referenced CSS output.

---

# 50. Subpath import for reference

`package.json`:

```json
{
  "imports": {
    "#app.css": "./src/styles/app.css"
  }
}
```

Then:

```css
@reference "#app.css";
```

More stable than deep relative paths in component trees.

---

# 51. Prefer CSS variable over `@apply` if simple

Instead of:

```css
@reference "../../app.css";

.title {
  @apply text-red-500;
}
```

Use:

```css
.title {
  color:
    var(--color-red-500);
}
```

Reasons:
- direct CSS,
- no utility resolution needed,
- potentially less build work.

---

# 52. `@apply` architecture

Good:
- third-party selector,
- uncontrolled markup,
- legacy integration.

Questionable:
- every application component,
- simple local rule,
- hiding 30 utilities inside semantic class without structural abstraction.

---

# 53. CSS layers [MASTER]

Tailwind uses:

```text
theme
base
components
utilities
```

Native CSS cascade layer rules apply.

Normal declarations:
later layer wins over earlier layer when origin/importance context matches.

---

# 54. Unlayered CSS caution

Native CSS unlayered author styles can outrank layered author styles in normal cascade.

Therefore a random unlayered custom stylesheet may override Tailwind utilities unexpectedly.

Place custom CSS intentionally in layer when desired.

---

# 55. `@layer components` purpose

```css
@layer components {
  .card { ... }
}
```

Good:
- semantic reusable custom style,
- third-party integration.

Utilities can override it cleanly.

---

# 56. Preflight as dependency [ARCH]

Preflight is not invisible reset.

It changes:
- headings,
- list,
- border,
- margins,
- replaced elements.

When embedding Tailwind into legacy app:
test Preflight first.

---

# 57. Disable Preflight strategy

Import lower-level Tailwind parts and omit preflight.

Use:
- legacy host,
- microfrontend,
- widget,
- app with existing reset.

Don't globally patch dozens of Preflight effects if you actually don't want Preflight.

---

# 58. Prefixing [ARCH]

Lower-level Tailwind imports support `prefix(...)` option for theme/utilities.

Use:
- embedded widget,
- multiple Tailwind systems,
- collision avoidance.

Cost:
- longer classes,
- examples/docs require prefix,
- package contract becomes prefix-aware.

---

# 59. Global important option

Tailwind utilities import can be marked important at import level.

Use only in hostile legacy cascade where migration requires.

Cost:
- hard overrides,
- integration complexity,
- less flexible component styling.

Prefer layer architecture first.

---

# 60. Important modifier

Per utility:

```text
bg-red-500!
```

Use targeted exception.

Not a conflict-resolution default.

---

# 61. HTML class order ≠ CSS source order [MASTER]

```html
<div class="px-2 px-4">
```

Text order in `class` attribute does not automatically mean `px-4` wins.

Cascade uses generated CSS source/layer/specificity.

This is why dynamic class merge needs controlled logic.

---

# 62. Conflict-aware composition

Component helpers may combine:
- base classes,
- variant,
- caller class.

Potential:

```text
px-4
px-2
```

Conflict merge libraries can normalize Tailwind utility groups.

Use at reusable component boundary.

---

# 63. Class sorting is readability

Prettier Tailwind class sorting:
- stable diffs,
- readable grouping.

It is not intended as behavior mechanism.

If formatting changes behavior, investigate real conflict.

---

# 64. Runtime dynamic values [MASTER]

Server/API gives:

```text
width=73%
```

Don't create:

```jsx
`w-[${width}%]`
```

because scanner/build/runtime mismatch.

Use:

```jsx
<div
  style={{ "--width": `${width}%` }}
  className="w-(--width)"
/>
```

Static candidate + runtime value.

---

# 65. Runtime colors

```jsx
<button
  style={{
    "--bg": buttonColor,
    "--hover-bg": hoverColor,
  }}
  className="
    bg-(--bg)
    hover:bg-(--hover-bg)
  "
>
```

This is a clean CSS-variable bridge.

---

# 66. Arbitrary type hint in component API

For ambiguous namespace:

```text
text-(color:--text)
text-(length:--size)
```

Use explicit hint in library code so Tailwind parser intent is stable.

---

# 67. Dark mode architecture

Simple app:
```text
dark:bg-gray-950
```

Large multi-theme design system:
```text
bg-(--surface)
```

with root semantic variables.

Choose based on scale.

---

# 68. Theme explosion

Bad:

```text
dark:
brand-a:
brand-b:
holiday:
high-contrast:
```

repeated on every component.

Better:
states set semantic CSS vars at root.

Components consume stable tokens.

---

# 69. FOUC in manual theme

Tailwind class itself isn't the cause.

Cause:
root `.dark`/`data-theme` set after first paint.

Fix:
- SSR theme state,
- early initialization,
- system fallback.

---

# 70. ARIA vs data variants [ARCH]

Use:

```text
aria-expanded
aria-selected
aria-pressed
```

when state has true accessibility semantics.

Use:

```text
data-state
data-density
data-loading
```

for app/presentation state without matching ARIA meaning.

Don't lie to assistive technology to get a styling selector.

---

# 71. `group` ownership

Nested groups:

```text
group/card
group/menu
```

prevent wrong ancestor state from triggering descendant.

Named groups are an architecture tool, not just syntax convenience.

---

# 72. `in-*` caution

Implicit ancestor match can trigger from any matching parent.

Good for shallow content.

For complex nested interactive UI:
prefer explicit/named group.

---

# 73. `peer` direction

Peer target follows peer due CSS subsequent sibling selector.

If target is before input:
- reorder markup,
- use parent `has-*`,
- lift state to parent.

Don't fight selector direction.

---

# 74. `has-*` vs JS state

If state already in DOM:

```text
checked
invalid
focus
child existence
```

`:has()`/Tailwind `has-*` can eliminate redundant JS class toggles.

If state is business/data state:
still belongs in app logic.

---

# 75. Child variants specificity pitfall

Parent:

```text
*:bg-gray-100
```

child:

```text
bg-red-100
```

may not override as intuitively expected because generated child selector/order has same/higher effective cascade position.

If child needs exceptions:
put style ownership on child or avoid blanket child variant.

---

# 76. Arbitrary selector complexity budget

If you see:

```text
dark:lg:[&>div:nth-child(2)_a:hover]:...
```

stop and ask:
- custom CSS clearer?
- custom variant reusable?
- DOM/component boundary wrong?

Utility-first is not “all CSS must fit in one attribute”.

---

# 77. Third-party integration pattern

One-off:

```text
[&_.vendor-item]:p-2
```

Large integration:

```text
styles/integrations/editor.css
```

Use `@layer components` and explicit selectors.

---

# 78. Tailwind + native dialog/popover

Tailwind only styles.

Native/platform primitive handles:
- semantics,
- top layer,
- some keyboard/dismiss behavior.

Example:

```html
<dialog
  class="
    rounded-xl
    backdrop:bg-black/50
  "
>
```

Do not reinvent behavior with div just because utilities make visuals easy.

---

# 79. Browser support boundary

Tailwind generates modern CSS but doesn't polyfill every feature.

Example utilities can rely on:
- container queries,
- masks,
- field sizing,
- zoom,
- modern color,
- scrollbar standards.

Project browser support policy still applies.

---

# 80. `supports-*` progressive enhancement

```html
<div
  class="
    flex
    supports-[display:grid]:grid
  "
>
```

Great for simple fallback.

Complex fallback:
plain `@supports` CSS may be clearer.

---

# 81. v4.3 scrollbar utilities [MASTER]

Core now includes:
- `scrollbar-auto/thin/none`,
- thumb colors,
- track colors,
- alpha modifiers,
- gutter auto/stable/both.

Still platform-dependent visually.

Avoid promising pixel-identical scrollbars cross-platform.

---

# 82. `scrollbar-none` UX

Hidden scrollbar can make scroll region undiscoverable.

Only use when:
- carousel has clear affordance,
- keyboard/touch works,
- scrollbar isn't only clue.

---

# 83. `zoom-*` [V4.3]

Maps to CSS `zoom`.

Do not confuse with browser user zoom.

Never use CSS zoom to fight accessibility/browser zoom.

Good:
- preview pane,
- document miniature.

---

# 84. Logical utility expansion [V4.2+]

Current vocabulary includes:
- `mbs-*`, `mbe-*`,
- `pbs-*`, `pbe-*`,
- logical border start/end,
- `inline-*`, `block-*`,
- logical inset,
- logical scroll padding/margin.

Use when direction/writing mode matters.

---

# 85. Deprecated start/end inset naming direction

v4.3 release notes state old `start-*`/`end-*` inset utilities remain but are deprecated toward:

```text
inset-s-*
inset-e-*
```

aligned with:

```text
inset-bs-*
inset-be-*
```

Use current naming in new code.

---

# 86. `font-features-*` [V4.2+]

Low-level OpenType:

```text
font-features-["tnum"]
```

Prefer high-level:

```text
tabular-nums
```

when equivalent.

Low-level utility is escape hatch for font-specific feature tags.

---

# 87. `tab-*` [V4.3]

Tailwind core now exposes `tab-size`.

Example:

```text
tab-2
tab-8
tab-[12px]
tab-(--tab-size)
```

Useful code viewers/editors.

---

# 88. Build integration selection

Use first-party integration matching stack:
- `@tailwindcss/vite`,
- `@tailwindcss/postcss`,
- `@tailwindcss/cli`,
- `@tailwindcss/webpack`.

Avoid unnecessary processing layers.

---

# 89. Webpack plugin [V4.2+]

Tailwind introduced first-party webpack loader to avoid extra PostCSS detour in webpack-centric stacks and improve build speed.

If stack is Next/Turbopack with webpack-loader compatibility, evaluate current recommended integration.

---

# 90. PostCSS role

PostCSS may still host:
- other transforms,
- project tooling.

But don't add legacy plugin pipeline because old Tailwind tutorial did.

V4 setup should start from current framework guide.

---

# 91. Tailwind + SCSS architecture

Danger:

```text
Sass token map
Tailwind @theme
CSS :root tokens
```

all independently authoritative.

Pick one source of truth.

Possible architecture:

```text
external token source
→ generates @theme + CSS vars
```

or:

```text
Sass source
→ emits CSS vars
→ Tailwind uses var shorthand
```

---

# 92. Tailwind + CSS Modules

Potential complexity stack:

```text
CSS Module
→ @reference
→ @apply
→ utility
→ theme token
```

If one declaration:
use CSS variable directly.

Use CSS Modules for scoped complex CSS, not as mandatory wrapper around Tailwind.

---

# 93. Tailwind + Shadow DOM

Document stylesheet doesn't automatically style shadow internals.

Strategies:
- adopt compiled CSS inside shadow root,
- local component CSS,
- CSS custom property theming,
- `::part`.

Tailwind obeys Shadow DOM boundaries because it is normal CSS.

---

# 94. Embedded widget [ARCH]

Host page unknown.

Recommended:
- disable Preflight,
- prefix utilities,
- scoped source detection,
- no global base styles,
- optional Shadow DOM.

Goal:
no host/widget style collision.

---

# 95. Microfrontend strategy

Three common approaches:

```text
1. shared Tailwind/theme/build
2. independent prefixed bundles
3. Shadow DOM isolation
```

Main danger:
multiple Preflights/global layers.

---

# 96. CSS layer contract across apps

If microfrontends share document:
define cascade layer ordering intentionally.

Tailwind layers interact with:
- vendor,
- app base,
- legacy,
- overrides.

Layer contract belongs architecture docs.

---

# 97. Tailwind package options

Design system can ship:

```text
compiled CSS
source components
theme CSS
custom utility CSS
```

Each creates different coupling.

---

# 98. Source components package

Pros:
- consumer Tailwind generates only used classes.

Requirements:
- consumer scans package via `@source`,
- compatible Tailwind utility/theme expectations.

---

# 99. Compiled CSS package

Pros:
- consumer doesn't scan package classes.

Cons:
- potential duplicate Tailwind/reset,
- theme coupling,
- larger static CSS,
- layer/order integration.

---

# 100. Theme-only package

Great v4 pattern:

```text
@company/theme.css
```

contains `@theme`.

Apps import same vocabulary.

Version theme changes semantically.

---

# 101. Runtime external design tokens

Enterprise may keep token JSON/DTCG elsewhere.

Pipeline:

```text
token source
→ generated Tailwind @theme
→ generated semantic CSS vars
→ components
```

Tailwind can be consumer of tokens, not source of truth.

---

# 102. v3 → v4 config migration

Move:

```text
theme.extend
screens
colors
fonts
spacing
```

toward CSS `@theme`.

Keep JS config via `@config` only while needed.

---

# 103. v3 content migration

Old:

```js
content: [...]
```

New:
- automatic detection,
- `source()`,
- `@source`.

Still make source ownership explicit for monorepos/packages.

---

# 104. v3 custom utility migration

Old:

```css
@layer utilities {
  .tab-4 { ... }
}
```

V4:

```css
@utility tab-4 {
  tab-size:4;
}
```

Reason:
v4 respects native CSS `@layer`; utility registration is explicit.

---

# 105. v3 safelist migration

Old JS safelist does not map directly to v4 architecture.

Use:
```text
@source inline()
```

for explicit candidates.

---

# 106. v3 important syntax

Legacy:
```text
!flex
```

V4 preferred:
```text
flex!
```

Use trailing `!` in new code.

---

# 107. `@config` compatibility

```css
@config "../../tailwind.config.js";
```

Useful incremental migration.

Some old config options do not carry over exactly.

Target architecture should move to CSS-first where practical.

---

# 108. `@plugin` compatibility

```css
@plugin "@tailwindcss/typography";
```

Loads legacy JS plugin.

Keep for ecosystem packages that need it.

Project-owned simple utilities/variants should prefer CSS APIs.

---

# 109. Deprecated `theme()` function

Legacy:

```css
margin: theme(spacing.12);
```

Current v4 direction:
use CSS theme variables or Tailwind build functions.

Don't build new code around `theme()`.

---

# 110. `--spacing()` [V4]

```css
.my-element {
  margin:
    --spacing(4);
}
```

Tailwind compiles to spacing variable calculation.

This is build-time Tailwind syntax, not normal browser CSS function.

---

# 111. `--alpha()` [V4]

```css
color:
  --alpha(
    var(--color-lime-300) / 50%
  );
```

Tailwind compiles to modern CSS color mix/alpha equivalent.

Good in custom CSS while staying aligned with theme colors.

---

# 112. Build-time vs browser-time

Tailwind functions:

```text
--spacing()
--alpha()
--value()
--modifier()
```

are build-time processing concepts.

Browser receives compiled CSS.

CSS functions like:

```text
calc()
var()
color-mix()
```

are browser-time.

---

# 113. V4 dynamic scale tension

V4 lets:

```text
p-13
w-73
grid-cols-15
```

work more flexibly.

Engineering convenience can weaken design discipline.

Teams may enforce allowed design scales through lint/review even if compiler accepts more.

---

# 114. Arbitrary value governance

Possible policy:

```text
arbitrary colors: banned
arbitrary font sizes: discouraged
arbitrary grid templates: allowed
arbitrary z-index: reviewed
CSS variable arbitrary values: allowed
```

Tailwind itself won't enforce product design governance.

---

# 115. CMS styling policy

Don't let CMS save raw:

```text
bg-red-500
```

as uncontrolled presentation API.

Better:

```text
CMS value: "danger"
→ static app mapping
→ Tailwind class
```

Benefits:
- scanner-safe,
- secure,
- redesignable.

---

# 116. Untrusted arbitrary values

Do not build class strings from user input:

```text
[background:url(...)]
```

Tailwind is not sanitizer.

Whitelist semantic values or use validated CSS variable data.

---

# 117. CSP consideration

Dynamic inline `style` CSS variables may be constrained by Content Security Policy.

If strict CSP:
- predefined classes,
- safe style injection policy,
- nonce/hash architecture
may be needed.

Tailwind doesn't bypass CSP.

---

# 118. SSR/hydration

Tailwind itself is static.

Hydration mismatch/FOUC can come from:
- server vs client conditional classes,
- theme root state,
- browser-only preference.

Keep server/client state consistent.

---

# 119. RSC/server components

Static class maps work well in server components.

Important remains:
complete literal candidates must exist in scanned codebase.

---

# 120. Performance — source scanning

Avoid scanning:
- generated dist,
- unrelated repo,
- vendored source,
- giant docs cache.

Use:
- source base,
- `@source not`,
- `source(none)`.

---

# 121. Performance — unique arbitrary values

This is fine:

```text
w-[37rem]
```

one time.

This can grow CSS:

```text
w-[1px]
w-[2px]
...
w-[1000px]
```

Each unique candidate may generate rule.

---

# 122. Performance — `@theme static`

Static emits more vars.

Measure:
- raw CSS,
- gzip/Brotli.

Use when external access benefits justify.

---

# 123. Performance — `@apply` in many style blocks

Thousands of component-scoped styles using:
- `@reference`,
- `@apply`

can increase processing work.

If only consuming color/spacing token:
use CSS var directly.

---

# 124. Performance — duplicate Tailwind builds

Symptoms:
- duplicate Preflight,
- duplicate theme variables,
- duplicate utilities.

Check:
- CSS entrypoints,
- framework imports,
- microfrontend bundles.

---

# 125. Performance — custom candidate explosion

A functional utility itself doesn't output every possible value; discovered/safelisted candidates matter.

But broad inline sources can force huge generation.

---

# 126. Output budget [ARCH]

Set project-specific targets:

```text
main CSS raw
gzip CSS
route CSS
theme vars
build time
incremental rebuild time
```

Measure before/after major utility/theme generator changes.

---

# 127. Debug missing utility [MASTER]

Checklist:

```text
1. candidate complete?
2. source scanned?
3. source ignored?
4. package needs @source?
5. utility family exists?
6. theme token exists?
7. custom @utility registered?
8. correct v4 syntax?
9. style context needs @reference?
10. generated CSS inspected?
```

---

# 128. Debug rule exists but no effect

Now debug CSS:

```text
computed declaration
→ cascade layer
→ specificity
→ inheritance
→ display/layout context
→ min/max sizing
→ overflow
→ stacking context
→ browser support
```

Tailwind is no longer primary issue.

---

# 129. Debug responsive variant

Check:
- breakpoint token value,
- media direction mobile-first,
- max/min range,
- viewport actual width.

For container:
- ancestor has `@container`,
- correct named container,
- actual container inline size.

---

# 130. Debug peer/group

Group:
- marker on correct ancestor?
- nested group name correct?

Peer:
- peer comes before target?
- correct state?
- sibling relation valid?

---

# 131. Debug arbitrary syntax

Check:
- balanced brackets,
- `_` whitespace,
- escaped underscore,
- JSX backslash stripping,
- type hint,
- CSS value validity.

---

# 132. Debug class conflict

Do not inspect class attribute order only.

Inspect browser computed styles:
- which generated rule wins,
- layer,
- selector,
- media/state active.

---

# 133. Testing pyramid

## Static
- invalid utility,
- deprecated naming,
- dynamic synthesis.

## Component
- props/states.

## Visual regression
- screenshots.

## Browser
- Chromium,
- Firefox,
- Safari.

## Accessibility
- keyboard,
- reduced motion,
- forced colors,
- zoom.

---

# 134. Visual regression matrix

At minimum representative:

```text
320px
768px
1440px
light
dark
focus
long text
RTL
```

For component library also:
- disabled,
- loading,
- error,
- empty.

---

# 135. Don't snapshot whole class string blindly

Exact class-string snapshots make harmless refactors noisy.

Prefer test:
- semantic component state,
- rendered behavior,
- visual result.

Class string only when intentionally public contract.

---

# 136. Stylelint/ESLint governance

Possible checks:
- no dynamic candidate concatenation,
- no deprecated utility name,
- arbitrary-value policy,
- no raw palette in semantic components,
- class conflict detection.

Tailwind editor tooling handles many local errors; organization-specific rules need custom tooling.

---

# 137. Accessibility matrix

Check:
- `focus-visible`,
- semantic disabled,
- aria/data correctness,
- `motion-reduce`,
- forced colors,
- 200% browser zoom,
- keyboard traversal,
- touch target.

Tailwind makes styles concise, not accessible by default.

---

# 138. `appearance-none` responsibility

If remove native appearance:
you must style:
- focus,
- checked,
- disabled,
- forced colors,
- high contrast.

Prefer native control styling when possible.

---

# 139. `scrollbar-none` responsibility

Invisible scrollbar may hurt discoverability.

Use with:
- obvious scroll affordance,
- touch drag,
- keyboard support,
- snap/navigation cues.

---

# 140. `zoom-*` responsibility

CSS `zoom` can affect:
- layout,
- sizing,
- interaction.

Good for preview.
Bad for shrinking full app instead of responsive design.

---

# 141. Logical utilities and RTL

Test:

```html
<html dir="rtl">
```

Logical properties fix geometry direction, but content/design can still require:
- icon mirroring,
- alignment changes,
- semantic order review.

---

# 142. Tailwind + localization

Long translated text exposes:
- fixed widths,
- truncate misuse,
- button sizing,
- grid min-content.

Use utilities:
```text
min-w-0
min-h-0
break-words
text-wrap
flex-wrap
```
with actual localized fixtures.

---

# 143. Tailwind senior component contract

Reusable component should define:

```text
semantic props
slots
state attributes
theme hooks
className override policy
responsive ownership
accessibility behavior
```

Tailwind class list is implementation.

---

# 144. Slot API pattern

Markup:

```html
<div data-slot="title">
```

Can target via arbitrary/data descendant variants when needed.

But if external consumers rely on slot:
document it as public styling API.

---

# 145. Override hook design

Options:
- `className`,
- CSS custom properties,
- data attributes,
- slots,
- component variants.

Avoid forcing consumer to target:
```text
div > span:nth-child(2)
```

---

# 146. Semantic variants + class escape hatch

Good API:

```tsx
<Button
  variant="primary"
  size="md"
  className="w-full"
/>
```

Semantic base behavior + controlled local utility override.

---

# 147. Merge policy for `className`

If consumer `className` can conflict:
- decide precedence,
- use merge helper if needed,
- document whether internal or caller wins.

Don't rely on class text order.

---

# 148. Design-system public Tailwind dependency

If consumers import source components with Tailwind classes:
Tailwind version can become peer/build dependency.

If you don't want that coupling:
ship compiled CSS.

Trade-off must be intentional.

---

# 149. Version compatibility

Document:

```text
Design System v3
→ Tailwind >= 4.3
```

when package relies on:
- v4.3 scrollbar,
- `@container-size`,
- new logical utilities,
- functional utility defaults.

---

# 150. Upgrade Tailwind safely

On version upgrade:

```text
compile
warnings
generated CSS diff
bundle size
visual regression
browser tests
deprecated class search
```

Minor releases can add/adjust utility APIs.

---

# 151. v4.3 current additions

Current baseline includes:
- new scrollbar utilities,
- `@container-size`,
- `zoom-*`,
- `tab-*`,
- stacked + compound `@variant`,
- default values for functional utilities.

V4.2 additions in current baseline:
- `mauve`, `olive`, `mist`, `taupe`,
- first-party webpack plugin,
- expanded logical properties,
- `font-features-*`.

---

# 152. Migration anti-pattern: keep v3 forever inside v4

Possible to keep:
- `@config`,
- `@plugin`.

But project new features then split across:
- JS config,
- CSS theme,
- plugin,
- custom CSS.

Migrate ownership gradually to avoid two configuration systems forever.

---

# 153. Migration anti-pattern: rewrite all custom CSS into utilities

V4 gives stronger CSS APIs, but custom CSS still valid.

Don't convert readable complex CSS into unreadable arbitrary variants solely for purity.

---

# 154. Migration anti-pattern: convert every token to semantic utility

Sometimes primitive utilities:
```text
gap-4
rounded-lg
```
are exactly right.

Semantic token layer should solve real theming/design governance, not add names for every primitive.

---

# 155. Master decision matrix

Use normal utility:
- core atomic property.

Use arbitrary value:
- one-off exact value.

Use CSS variable shorthand:
- runtime value.

Use `@theme`:
- design token should create utility API.

Use `@utility`:
- reusable atomic/custom utility family.

Use `@custom-variant`:
- reusable state/selector condition.

Use `@layer components`:
- semantic custom CSS/component integration.

Use component abstraction:
- structure + style + state repeat.

Use plain CSS:
- selector/behavior clearer than class expression.

Use `@source`:
- source ownership/scanner needs explicit control.

---

# 156. Master anti-pattern checklist

```text
[ ] runtime class interpolation?
[ ] raw arbitrary values repeated?
[ ] 40-class copy-paste repeated?
[ ] @apply used as reflex?
[ ] viewport breakpoint used for component-local layout?
[ ] ARIA attribute abused as CSS hook?
[ ] nested group ownership ambiguous?
[ ] broad safelist?
[ ] source scan entire monorepo unnecessarily?
[ ] multiple Preflights?
[ ] Sass/Tailwind/CSS tokens duplicated?
[ ] global important without migration reason?
[ ] arbitrary selector unreadable?
[ ] component public API exposes Tailwind internals?
```

---

# 157. Master Labs

## Lab 1 — Scanner
Compare:
- static class,
- dynamic interpolation,
- static map,
- external package source.

## Lab 2 — Strict theme
Reset color namespace and create only project palette.

## Lab 3 — Functional utility
Build `tab-*` with:
- theme,
- bare,
- arbitrary,
- default.

## Lab 4 — Negative utility
Create custom positive/negative inset-like utility.

## Lab 5 — Modifier
Build value/modifier custom utility.

## Lab 6 — Custom variant
Create `density-compact:` based on data attribute.

## Lab 7 — Source split
Admin/storefront with `source(none)`.

## Lab 8 — Shared theme package
Two apps consume same `@theme`.

## Lab 9 — Runtime color
API color through CSS variable + static utility.

## Lab 10 — Container-first card
Use same component in sidebar/main/modal.

## Lab 11 — Legacy integration
Disable Preflight + prefix widget.

## Lab 12 — Third-party widget
Compare arbitrary variant vs component CSS.

## Lab 13 — v3 migration
Move config/content/custom utility/safelist to v4.

## Lab 14 — Dark strategy
Compare `dark:*` vs semantic runtime variables.

## Lab 15 — Bundle budget
Measure broad safelist vs real static candidates.

---

# 158. Master self-test

1. Candidate scanning khác runtime evaluation?
2. `@source` ảnh hưởng build ownership ra sao?
3. `source(none)` phù hợp multi-bundle thế nào?
4. Broad safelist gây CSS growth ra sao?
5. `@theme` có hai role nào?
6. Normal var khác theme var?
7. Theme token rename có breaking không?
8. `inline` giải quyết scope issue gì?
9. `static` cost gì?
10. Breakpoint token có phải cosmetic token?
11. Container thresholds có nên copy viewport?
12. `@container-size` side effect gì?
13. Functional utility matching flow?
14. Theme resolver khác bare resolver?
15. Arbitrary resolver grammar?
16. `--default()` dùng khi nào?
17. Negative utility design ra sao?
18. Modifier là gì?
19. Custom utility sort có implication gì?
20. `@utility` khác component?
21. Variant thực chất transform gì?
22. Custom variant khi nào promote?
23. `@reference` khác import?
24. Direct CSS var vs @apply?
25. Tailwind layer order?
26. Unlayered CSS tại sao nguy hiểm?
27. HTML class order có quyết định cascade?
28. Merge helper giải quyết gì?
29. Runtime dynamic value bridge thế nào?
30. Semantic props vs Tailwind props?
31. ARIA vs data selector?
32. Named group giải quyết gì?
33. Peer structural limitation?
34. Child variant override pitfall?
35. Browser support có được Tailwind polyfill không?
36. Scrollbar-none UX risk?
37. zoom utility khác browser zoom?
38. Logical utility cần test gì?
39. Preflight disable case?
40. Prefix use case?
41. Multiple bundles risk?
42. Tailwind + Shadow DOM?
43. Source component package cần gì?
44. Compiled CSS package trade-off?
45. Theme-only package lợi gì?
46. v3 custom utility migrate thế nào?
47. `theme()` deprecated thay bằng gì?
48. Tailwind function build-time vs CSS function?
49. Performance bottleneck nào?
50. Khi nào plain CSS tốt hơn Tailwind?

---

# 159. Production reference architecture

```text
External token source (optional)
        │
        ▼
      @theme
        │
        ├── Tailwind utility vocabulary
        └── CSS theme variables
                 │
                 ▼
         Components/templates
          │      │       │
          │      │       └── data/ARIA states
          │      └── viewport/container variants
          └── static utility candidates
                 │
                 ▼
          source detection
                 │
                 ▼
           generated CSS
                 │
                 ▼
              browser
```

---

# 160. Official references

- https://tailwindcss.com/docs
- https://tailwindcss.com/blog/tailwindcss-v4-3
- https://tailwindcss.com/docs/theme
- https://tailwindcss.com/docs/adding-custom-styles
- https://tailwindcss.com/docs/detecting-classes-in-source-files
- https://tailwindcss.com/docs/functions-and-directives
- https://tailwindcss.com/docs/hover-focus-and-other-states
- https://tailwindcss.com/docs/responsive-design
- https://tailwindcss.com/docs/dark-mode
- https://tailwindcss.com/docs/preflight
- https://tailwindcss.com/docs/upgrade-guide

---

# Kết luận

Tailwind Senior:

```text
utility fluency
+ CSS understanding
+ components
+ tokens
+ accessibility
```

Tailwind Master:

```text
candidate detection
+ CSS-first v4 APIs
+ functional utilities
+ source/build architecture
+ package/design-system contracts
+ migration
+ performance
+ browser cascade
```

Nguyên tắc cuối:

```text
Tailwind is the authoring system.
CSS is still the execution model.
```

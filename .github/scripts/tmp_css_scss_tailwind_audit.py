from pathlib import Path

root = Path('.')
files = {
    'css': root/'10_frontend/css/CSS_Beginner_to_Senior_2026_v2.md',
    'css_master': root/'10_frontend/css/CSS_Master_Supplement_2026.md',
    'scss': root/'10_frontend/scss/SCSS_Beginner_to_Senior_2026.md',
    'scss_master': root/'10_frontend/scss/SCSS_Master_Supplement_2026.md',
    'tailwind': root/'10_frontend/tailwind/TailwindCSS_Beginner_to_Senior_2026_REWRITTEN.md',
    'tailwind_master': root/'10_frontend/tailwind/TailwindCSS_Master_Supplement_2026_REWRITTEN.md',
}


def insert_after(path: Path, marker: str, block: str) -> None:
    text = path.read_text(encoding='utf-8')
    signature = block.strip().splitlines()[0]
    if signature in text:
        return
    index = text.find(marker)
    if index < 0:
        raise RuntimeError(f'Marker not found in {path}: {marker}')
    index += len(marker)
    text = text[:index] + '\n\n' + block.strip() + '\n' + text[index:]
    path.write_text(text, encoding='utf-8')


css_spine = r'''# 0A. Mental model xuyên suốt: từ declaration tới pixel trên màn hình

CSS dễ bị học thành một danh sách property rời rạc, nhưng browser không xử lý CSS theo cách đó. Khi HTML và stylesheet được load, browser trước tiên phải xác định selector nào match element. Sau đó cascade chọn declaration thắng cho từng property. Chỉ sau khi cascade/defaulting hoàn tất, inheritance mới cung cấp value cho những property có cơ chế thừa hưởng. Browser tiếp tục tạo box, xác định normal flow và formatting context, resolve containing block, intrinsic/available size và positioning, chạy layout algorithm như Flexbox/Grid, rồi mới paint và composite.

Trục học canonical của CSS vì vậy là:

```text
selector matching
→ cascade
→ specificity / scope proximity / source order
→ inheritance + initial/defaulting
→ box model + sizing
→ normal flow
→ formatting context
→ positioning + containing block
→ Flexbox / Grid / other layout algorithms
→ responsive conditions
→ paint / composite / performance
```

Khi CSS “không chạy”, hãy truy theo đúng trục này thay vì đổi property ngẫu nhiên. Ví dụ `.card { width: 100% }` có thể không cho kết quả mong muốn vì selector không match, rule ở layer khác thắng, percentage resolve theo containing block khác, flex item bị automatic minimum size chặn co, hoặc parent tạo overflow/formatting context khác với assumption. Thêm `!important` chỉ giải quyết một nhánh rất nhỏ của cây nguyên nhân.

## Cascade trước, specificity sau

Specificity không phải luật đầu tiên của CSS. Cascade trước tiên xét relevance, origin/importance và cascade layer. Specificity chỉ được so giữa những declaration vẫn còn cạnh tranh trong cùng context precedence. Nếu specificity bằng nhau, `@scope` có thể đưa scoping proximity vào quyết định; source order là tie-breaker cuối. Vì thế architecture với `@layer`, selector nhẹ và component boundary thường bền hơn specificity war.

## Inheritance không phải “specificity của parent truyền xuống con”

Một `color` trên parent thường truyền xuống child vì `color` là inherited property; `padding` thì không. Nếu child có rule trực tiếp target nó, direct value thắng inherited value bất kể selector của parent mạnh đến đâu. Khi debug typography, custom property hoặc theme, hãy luôn phân biệt declaration thắng trên chính element với value inherited từ ancestor.

## Box model phải được đặt trong formatting context

`content`, `padding`, `border`, `margin` chỉ mô tả box. Cách box được đặt phụ thuộc formatting context. Block formatting context có rules về block flow, floats và margin interaction; inline formatting context tạo line boxes và baseline; Flexbox/Grid chạy sizing/placement algorithm riêng. Đây là lý do cùng `width`, `margin:auto` hay alignment property có thể hành xử khác ở các context khác nhau.

## Normal flow là baseline của positioning

Trước `absolute`, `fixed`, `sticky`, cần hiểu normal flow. `position: relative` vẫn giữ slot trong flow rồi offset visual box. `absolute` rời normal flow và tìm containing block. `fixed` thường liên hệ viewport/top-level containing context. `sticky` vẫn tham gia flow nhưng bị ràng buộc bởi scroll container, inset và scroll range. Khi positioning sai, câu hỏi đúng là “containing block/scroll container là ai?” trước khi hỏi “top bao nhiêu px?”.

## Responsive chỉ đổi điều kiện; layout engine vẫn là CSS layout

Media query bật/tắt declarations theo viewport, input capability, motion preference hoặc color scheme. Container query làm điều tương tự nhưng query container thay vì viewport. Bên trong điều kiện đó, layout vẫn do normal flow, Flexbox, Grid và sizing algorithms thực thi. Responsive tốt thường bắt đầu bằng fluid/intrinsic constraints, rồi breakpoint chỉ xuất hiện ở nơi behavior thực sự cần đổi.

## Rendering/performance là phần cuối của cùng mental model

Sau layout, browser paint text, background, border, shadow/effects rồi composite. Thay đổi geometry như `width` hoặc font metrics có thể kéo theo style/layout/paint; `transform` và `opacity` thường thuận lợi hơn cho compositor animation nhưng không miễn phí. Blur/backdrop-filter lớn, quá nhiều compositing layers hoặc `will-change` bừa bãi có thể tăng memory/render cost. Performance phải được đo theo rendering pipeline, không tối ưu bằng mẹo truyền miệng.

Khi debug production, trace chuẩn là: selector match → declaration valid → cascade/layer/specificity → computed value → inheritance/defaulting → formatting context/containing block → intrinsic/min/max/overflow → stacking/paint/composite. Đây là xương sống nối mọi chapter còn lại.'''
insert_after(files['css'], '# 0. Bản đồ học CSS', css_spine)

css_master = r'''# 0A. Master trace: từ selector matching đến rendering

Ở mức master, CSS là một pipeline có dependency chứ không phải một bộ property. Browser xây DOM/CSSOM, match selector, áp cascade để tìm specified values, default/inherit những phần còn thiếu, tính computed/used values, tạo formatting tree và boxes, chạy layout algorithm, sau đó paint và composite. Một bug ở mỗi tầng có biểu hiện khác nhau: declaration bị crossed-out là cascade problem; computed value đúng nhưng geometry sai thường là sizing/layout problem; geometry đúng nhưng element bị che liên quan stacking/top layer/clip; frame chậm cần đo style/layout/paint/composite.

Performance cũng nên được hiểu theo invalidation scope. Thay class ở ancestor có thể làm style recalculation cho descendants liên quan; font metrics có thể thay intrinsic size và kéo layout; geometry changes có thể reflow; shadow/filter lớn có thể tăng paint cost. `transform`/`opacity` thường phù hợp cho animation vì có thể tránh layout trong nhiều trường hợp, nhưng layer promotion không miễn phí. `contain` và `content-visibility` có thể giảm work khi subtree thật sự độc lập, đồng thời chúng cũng thay đổi layout/containment semantics nên không nên dùng như một “performance class” mặc định.

Khi review CSS production, hãy trả lời được bốn câu: declaration nào thắng, box/formatting context nào được tạo, layout algorithm nào quyết định geometry, và thay đổi này invalidate phần nào của rendering pipeline. Khi bốn câu đó rõ, phần lớn CSS edge case trở thành behavior có thể dự đoán.'''
insert_after(files['css_master'], '# 0. V2 đã đủ đến đâu?', css_master)

scss_path = files['scss']
scss_text = scss_path.read_text(encoding='utf-8')
scss_text = scss_text.replace(
    '> Baseline:\n> - Dùng **Dart Sass**.',
    '> Baseline (audit 2026-09):\n> - Dùng **Dart Sass 1.104.1** làm mốc tài liệu hiện tại.'
)
scss_path.write_text(scss_text, encoding='utf-8')

scss_spine = r'''# 0A. Mental model xuyên suốt: SCSS là chương trình chạy trước CSS

SCSS phải được học như một compile-time language dùng để author/generate CSS. `$variables`, maps, loops, mixins, functions và module graph được Dart Sass xử lý trước khi browser nhìn thấy trang. Kết quả cuối cùng chỉ là CSS. Vì vậy Sass variable không cascade, không inherit và không thay đổi runtime; CSS custom property thì có thể tham gia cascade, inheritance và runtime overrides.

Trục học canonical của SCSS là:

```text
Sass values / variables
→ nesting + selector generation
→ mixins / functions như compile-time abstraction
→ lists / maps / control flow để generate CSS
→ @use / @forward tạo module graph
→ partials + entry points tổ chức source
→ @extend như selector unification, không phải OOP inheritance
→ architecture + public API
→ compiler deprecations / migration
→ CSS output quality + compile performance
```

Khi đọc SCSS, luôn hỏi compiler sẽ emit CSS gì, bao nhiêu rule, selector nào và ở vị trí nào. Mixin include nhiều lần có thể duplicate declarations. Loop có thể tạo hàng nghìn rules. Nesting sâu có thể sinh selector specificity cao và coupling với DOM. Source ngắn hơn không đồng nghĩa output tốt hơn.

Variables phù hợp với compile-time calculation/generation. CSS custom properties phù hợp với runtime theme, cascade-based component contracts và values cần override trong DevTools/runtime. Mixins nên mô tả declaration set hoặc content wrapper có parameterization rõ. Functions nên trả value và tránh side effect. Maps hữu ích khi thực sự biểu diễn structured configuration; map lồng sâu chỉ để “gom mọi thứ” thường biến API thành khó dùng.

Modern module system là `@use` và `@forward`. `@use` tạo namespace, scope members trong file dùng và load module một lần. `@forward` tạo facade/public surface. Partials chỉ là tổ chức source; chúng không tự tạo module architecture nếu code vẫn nối bằng legacy `@import`. Sass `@import` và global built-ins đã deprecated từ Dart Sass 1.80.0 nên code mới không nên xây trên global namespace cũ.

`@extend` cũng không phải inheritance kiểu Java. Sass thực hiện selector unification để các selector mở rộng cùng nhận rules, vì thế output có thể xuất hiện xa nơi gọi và khó dự đoán. Placeholder `%foo` có use case, nhưng mixin, utility/composition hoặc CSS architecture thường explicit hơn. SCSS tốt phải làm CSS output dễ hiểu hơn, không che CSS đi.'''
insert_after(files['scss'], '# 0. SCSS thực sự là gì?', scss_spine)

scss_master = r'''# 0A. Modern Sass status — audit 2026-09

Canonical notes này lấy **Dart Sass 1.104.1** làm implementation/reference hiện tại. LibSass và Ruby Sass không còn là target cho code mới. Modern Sass đang chủ động tiến gần CSS platform: Sass `@import` và global built-in functions đã deprecated từ 1.80.0; code mới dùng `@use`, `@forward` và built-in modules như `sass:math`, `sass:map`, `sass:color`. Legacy `if()` cũng đang trên lộ trình deprecation để tránh xung đột với CSS `if()` mới.

Module graph là phần architecture cốt lõi. Mỗi `@use` load module một lần theo canonical URL, members được namespaced và private members không rò ra ngoài. `@forward` cho phép package tách implementation thành nhiều partial/module nhưng xuất một facade ổn định. Khi audit library, hãy phân biệt tool module không emit CSS, style module có side effect CSS và entry/facade module quyết định public surface/dependency order.

Mọi abstraction Sass cuối cùng phải được đánh giá bằng generated CSS. Compile-time cleverness không được phép tạo selector explosion, duplicate declarations, specificity escalation hoặc bundle vượt budget. Sass mastery là biết khi nào compile-time abstraction có giá trị và khi nào native CSS/custom properties/container queries/cascade layers đã là công cụ phù hợp hơn.'''
insert_after(files['scss_master'], '# 0. Mastery Boundary', scss_master)

tailwind_path = files['tailwind']
tw_text = tailwind_path.read_text(encoding='utf-8')
tw_text = tw_text.replace(
    '> Baseline của tài liệu là **Tailwind CSS v4.3**.',
    '> Baseline của tài liệu là **Tailwind CSS v4.3** — vẫn là release Tailwind CSS mới nhất được Tailwind công bố tính đến audit 2026-09-21.'
)
tailwind_path.write_text(tw_text, encoding='utf-8')

tailwind_spine = r'''## 1A. Cách đọc Tailwind mà không cần nhớ CSS notes trước đó

Tài liệu luôn liên hệ Tailwind với CSS nhưng không giả định bạn còn nhớ định nghĩa từ CSS library. Với mỗi utility, hãy hỏi bốn câu: utility generate property/mechanism CSS nào; property đó tác động lên chính element hay quan hệ parent/children; layout context nào phải tồn tại để property có ý nghĩa; và variant phía trước class biến selector hay thêm media/container condition nào.

Ví dụ `items-center` không có nghĩa chung chung là “căn giữa”. Nó generate `align-items: center` và chỉ có behavior mong đợi khi element là Flex/Grid container. Trong `flex-row`, cross axis thường theo chiều block/dọc; trong `flex-col`, trục đổi. Vì vậy phải hiểu container algorithm + axis + generated CSS, không học `items-center = center`.

`absolute` tương tự: utility generate `position: absolute`, đưa box ra khỏi normal flow và position theo containing block. `top-0` chỉ đặt inset sau khi containing block đã được xác định. Nếu containing block sai, thêm nhiều inset class không sửa root cause.

Responsive utility cũng chỉ tạo conditional CSS. `md:grid-cols-2` đặt Grid utility trong viewport media condition; `@md:flex-row` dùng container query condition. Browser vẫn chạy Grid/Flexbox bình thường. `hover:*` biến interaction selector; `group-hover:*` tạo ancestor relationship; `peer-invalid:*` dựa sibling relationship.

Trace debug canonical là:

```text
complete class candidate có tồn tại trong source?
→ Tailwind có generate rule không?
→ variant condition có active không?
→ rule có thắng cascade không?
→ generated CSS đang ở layout context nào?
→ sizing / overflow / containing block / stacking có đúng không?
```

Hai bước đầu thường là Tailwind/build problem. Các bước sau là browser behavior, nhưng mỗi section trong file phải giải thích behavior đó tại chỗ. Đây là cách học utility-first mà không biến class names thành magic.'''
insert_after(files['tailwind'], '## 1. Tailwind CSS thực sự là gì?', tailwind_spine)

tailwind_master = r'''## 1A. Master diagnosis: utility → generated CSS → browser behavior

Ở level master, một utility phải trace được theo hai chiều. Chiều xuôi bắt đầu từ class candidate, qua source scanner, variant/theme resolver, tới generated CSS rồi browser layout/rendering. Chiều ngược bắt đầu từ UI bug trong DevTools, truy computed style và layout context để tìm candidate/build rule gây behavior.

Ví dụ `min-w-0` resolve thành `min-width: 0`; browser dùng value này khi tính minimum inline size của flex/grid item, cho phép item co nhỏ hơn intrinsic content width. Nếu ellipsis hoạt động sau khi thêm `min-w-0`, nguyên nhân là layout constraint thay đổi chứ không phải Tailwind có truncate magic. `md:hover:bg-brand` cũng phải tách thành breakpoint condition + hover selector + theme color token. Nếu rule không được generate, debug source/theme; nếu rule có nhưng inactive, debug conditions; nếu apply nhưng visual vẫn sai, debug cascade/blending/browser CSS.

Version baseline vẫn là **Tailwind CSS v4.3** tại audit 2026-09-21. Khi migrate v3/early-v4, hãy xem đây là architecture change: JS config-first → CSS-first `@theme`; `content` globs → automatic detection/`@source`; simple custom plugin utility → `@utility`; repeated selector state → `@custom-variant` khi phù hợp. Migration cần diff generated CSS, browser baseline và visual regression, không chỉ search/replace syntax.'''
insert_after(files['tailwind_master'], '## 1. Tại sao cần một Master Supplement riêng?', tailwind_master)

css = (files['css'].read_text(encoding='utf-8') + files['css_master'].read_text(encoding='utf-8')).lower()
css_terms = [
    'selectors', 'cascade', 'specificity', 'inheritance', 'units', 'box model',
    'normal flow', 'formatting context', 'position', 'flexbox', 'grid', 'typography',
    'color', 'background', 'border', 'responsive', 'media queries', 'container queries',
    'transitions', 'animations', 'transforms', 'custom properties', 'accessibility',
    'architecture', 'performance', 'rendering pipeline'
]
missing_css = [x for x in css_terms if x not in css]

scss = (files['scss'].read_text(encoding='utf-8') + files['scss_master'].read_text(encoding='utf-8')).lower()
scss_terms = [
    'variables', 'nesting', 'mixins', 'functions', 'modules', 'partials', '@extend',
    'architecture', '@use', '@forward', '@import', 'dart sass 1.104.1'
]
missing_scss = [x for x in scss_terms if x not in scss]

tw = (files['tailwind'].read_text(encoding='utf-8') + files['tailwind_master'].read_text(encoding='utf-8')).lower()
tw_terms = [
    'utility-first', 'generated css', 'responsive', 'state variants', '@theme',
    'arbitrary values', 'layout', 'typography', 'configuration', 'component',
    'v4.3', 'migration', '@source', '@utility', '@custom-variant'
]
missing_tw = [x for x in tw_terms if x not in tw]

if missing_css or missing_scss or missing_tw:
    raise SystemExit(f'Coverage failed: CSS={missing_css}, SCSS={missing_scss}, Tailwind={missing_tw}')

for name, path in files.items():
    text = path.read_text(encoding='utf-8')
    print(f'{name}: {len(text.splitlines())} lines, {len(text)} chars')

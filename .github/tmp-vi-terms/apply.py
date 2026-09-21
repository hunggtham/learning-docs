from pathlib import Path
import re
import hashlib

FILES = [
    Path('10_frontend/css/CSS_Beginner_to_Senior_2026.md'),
    Path('10_frontend/css/CSS_Master_Supplement_2026.md'),
    Path('10_frontend/scss/SCSS_Beginner_to_Senior_2026.md'),
    Path('10_frontend/scss/SCSS_Master_Supplement_2026.md'),
    Path('10_frontend/tailwind/TailwindCSS_Beginner_to_Senior_2026_REWRITTEN.md'),
    Path('10_frontend/tailwind/TailwindCSS_Master_Supplement_2026_REWRITTEN.md'),
]

GLOSSARIES = {
    'css': '''\n## Quy ước thuật ngữ Việt–Anh\n\nTrong tài liệu này, thuật ngữ chuyên môn được ưu tiên diễn đạt bằng tiếng Việt tự nhiên và giữ thuật ngữ gốc bên cạnh để dễ đối chiếu. Ví dụ: **cơ chế phân tầng (cascade)**, **độ đặc hiệu (specificity)**, **kế thừa (inheritance)**, **mô hình hộp (box model)**, **luồng bố cục thông thường (normal flow)**, **ngữ cảnh định dạng (formatting context)**, **khối chứa tham chiếu (containing block)**, **định cỡ nội tại (intrinsic sizing)** và **ngữ cảnh xếp chồng (stacking context)**. Tên property, value, selector, at-rule và API khi xuất hiện dưới dạng mã vẫn được giữ nguyên để không làm sai cú pháp.\n\n''',
    'scss': '''\n## Quy ước thuật ngữ Việt–Anh\n\nTrong tài liệu này, thuật ngữ Sass/SCSS được viết theo hướng tiếng Việt dễ hiểu nhưng vẫn giữ từ gốc để tra cứu. Ví dụ: **thời điểm biên dịch (compile-time)**, **thời gian chạy (runtime)**, **phạm vi (scope)**, **không gian tên (namespace)**, **đồ thị mô-đun (module graph)**, **nội suy (interpolation)**, **che khuất biến (shadowing)**, **luồng điều khiển (control flow)** và **hợp nhất bộ chọn (selector unification)**. Những tên directive, function, module và cú pháp Sass nằm trong mã vẫn được giữ nguyên.\n\n''',
    'tailwind': '''\n## Quy ước thuật ngữ Việt–Anh\n\nTrong tài liệu này, thuật ngữ Tailwind được diễn đạt bằng tiếng Việt trước rồi giữ từ gốc bên cạnh khi cần đối chiếu. Ví dụ: **mô hình ưu tiên tiện ích (utility-first)**, **tiện ích (utility)**, **biến thể trạng thái (state variant)**, **giá trị tùy ý (arbitrary value)**, **điểm ngắt (breakpoint)**, **truy vấn vùng chứa (container query)**, **phát hiện nguồn (source detection)**, **biên dịch tức thời (JIT, just-in-time)** và **cấu hình ưu tiên CSS (CSS-first configuration)**. Tên class, directive và utility literal trong code luôn được giữ nguyên.\n\n''',
}

TERMS = {
    'automatic minimum size': 'kích thước tối thiểu tự động (automatic minimum size)',
    'automatic minimum': 'mức tối thiểu tự động (automatic minimum)',
    'available space': 'không gian khả dụng (available space)',
    'intrinsic sizing': 'định cỡ nội tại (intrinsic sizing)',
    'intrinsic size': 'kích thước nội tại (intrinsic size)',
    'intrinsic dimensions': 'kích thước nội tại (intrinsic dimensions)',
    'intrinsic dimension': 'kích thước nội tại (intrinsic dimension)',
    'extrinsic sizing': 'định cỡ ngoại tại (extrinsic sizing)',
    'definite size': 'kích thước xác định (definite size)',
    'indefinite size': 'kích thước chưa xác định (indefinite size)',
    'visual formatting model': 'mô hình định dạng trực quan (visual formatting model)',
    'formatting context': 'ngữ cảnh định dạng (formatting context)',
    'formatting contexts': 'các ngữ cảnh định dạng (formatting contexts)',
    'block formatting context': 'ngữ cảnh định dạng khối (block formatting context)',
    'inline formatting context': 'ngữ cảnh định dạng nội dòng (inline formatting context)',
    'containing block': 'khối chứa tham chiếu (containing block)',
    'containing blocks': 'các khối chứa tham chiếu (containing blocks)',
    'stacking context': 'ngữ cảnh xếp chồng (stacking context)',
    'stacking contexts': 'các ngữ cảnh xếp chồng (stacking contexts)',
    'normal flow': 'luồng bố cục thông thường (normal flow)',
    'line box': 'hộp dòng (line box)',
    'line boxes': 'các hộp dòng (line boxes)',
    'baseline': 'đường cơ sở (baseline)',
    'replaced element': 'phần tử thay thế (replaced element)',
    'replaced elements': 'các phần tử thay thế (replaced elements)',
    'margin collapsing': 'gộp lề (margin collapsing)',
    'margin collapse': 'gộp lề (margin collapse)',
    'free space': 'không gian dư (free space)',
    'track sizing': 'định cỡ dải lưới (track sizing)',
    'grid track': 'dải lưới (grid track)',
    'grid tracks': 'các dải lưới (grid tracks)',
    'flex item': 'phần tử Flex (flex item)',
    'flex items': 'các phần tử Flex (flex items)',
    'grid item': 'phần tử Grid (grid item)',
    'grid items': 'các phần tử Grid (grid items)',
    'main axis': 'trục chính (main axis)',
    'cross axis': 'trục chéo (cross axis)',
    'layout algorithm': 'thuật toán bố cục (layout algorithm)',
    'layout algorithms': 'các thuật toán bố cục (layout algorithms)',
    'layout engine': 'bộ máy bố cục (layout engine)',
    'rendering pipeline': 'chuỗi xử lý kết xuất (rendering pipeline)',
    'rendering model': 'mô hình kết xuất (rendering model)',
    'rendering cost': 'chi phí kết xuất (rendering cost)',
    'style recalculation': 'tính lại style (style recalculation)',
    'layout thrashing': 'dao động bố cục do đọc/ghi xen kẽ (layout thrashing)',
    'layout shift': 'dịch chuyển bố cục (layout shift)',
    'paint cost': 'chi phí vẽ (paint cost)',
    'compositing layer': 'lớp tổng hợp (compositing layer)',
    'compositing layers': 'các lớp tổng hợp (compositing layers)',
    'scroll container': 'vùng chứa cuộn (scroll container)',
    'scroll containers': 'các vùng chứa cuộn (scroll containers)',
    'scroll anchoring': 'neo vị trí cuộn (scroll anchoring)',
    'scroll chaining': 'truyền chuỗi cuộn (scroll chaining)',
    'top layer': 'lớp trên cùng (top layer)',
    'safe area': 'vùng an toàn (safe area)',
    'motion path': 'đường chuyển động (motion path)',
    'additive animation': 'hoạt ảnh cộng dồn (additive animation)',
    'entry transition': 'chuyển tiếp khi xuất hiện (entry transition)',
    'exit transition': 'chuyển tiếp khi rời đi (exit transition)',
    'view transition': 'chuyển cảnh giao diện (view transition)',
    'view transitions': 'chuyển cảnh giao diện (view transitions)',
    'scroll-driven animation': 'hoạt ảnh điều khiển bằng cuộn (scroll-driven animation)',
    'scroll-driven animations': 'hoạt ảnh điều khiển bằng cuộn (scroll-driven animations)',
    'anchor positioning': 'định vị theo điểm neo (anchor positioning)',
    'container query': 'truy vấn vùng chứa (container query)',
    'container queries': 'các truy vấn vùng chứa (container queries)',
    'media query': 'truy vấn môi trường (media query)',
    'media queries': 'các truy vấn môi trường (media queries)',
    'feature query': 'truy vấn hỗ trợ tính năng (feature query)',
    'feature queries': 'các truy vấn hỗ trợ tính năng (feature queries)',
    'responsive design': 'thiết kế đáp ứng (responsive design)',
    'responsive ownership': 'quyền sở hữu hành vi đáp ứng (responsive ownership)',
    'constraint-driven layout': 'bố cục theo ràng buộc (constraint-driven layout)',
    'intrinsic layout': 'bố cục nội tại (intrinsic layout)',
    'fluid layout': 'bố cục linh hoạt (fluid layout)',
    'box model': 'mô hình hộp (box model)',
    'logical properties': 'thuộc tính logic (logical properties)',
    'writing mode': 'chế độ viết (writing mode)',
    'forced colors': 'màu cưỡng bức (forced colors)',
    'high contrast': 'độ tương phản cao (high contrast)',
    'reduced motion': 'giảm chuyển động (reduced motion)',
    'progressive enhancement': 'cải tiến lũy tiến (progressive enhancement)',
    'graceful degradation': 'suy giảm có kiểm soát (graceful degradation)',
    'visual regression': 'hồi quy giao diện (visual regression)',
    'cross-browser': 'đa trình duyệt (cross-browser)',
    'browser compatibility': 'tương thích trình duyệt (browser compatibility)',
    'browser support': 'mức hỗ trợ trình duyệt (browser support)',
    'focus management': 'quản lý tiêu điểm (focus management)',
    'focus indicator': 'chỉ báo tiêu điểm (focus indicator)',
    'design tokens': 'token thiết kế (design tokens)',
    'design token': 'token thiết kế (design token)',
    'token hierarchy': 'phân cấp token (token hierarchy)',
    'semantic token': 'token ngữ nghĩa (semantic token)',
    'component token': 'token thành phần (component token)',
    'public api': 'giao diện công khai (public API)',
    'component api': 'giao diện thành phần (component API)',
    'component contract': 'hợp đồng thành phần (component contract)',
    'style boundary': 'ranh giới style (style boundary)',
    'shadow dom': 'Shadow DOM (cây DOM đóng gói)',
    'constructable stylesheet': 'stylesheet có thể khởi tạo (constructable stylesheet)',
    'constructable stylesheets': 'các stylesheet có thể khởi tạo (constructable stylesheets)',
    'typed om': 'Typed OM (mô hình đối tượng CSS có kiểu)',
    'custom highlight api': 'API tô sáng tùy chỉnh (Custom Highlight API)',
    'cssom view': 'CSSOM View (mô hình API quan sát hình học/viewport)',
    'cascade layer': 'lớp phân tầng (cascade layer)',
    'cascade layers': 'các lớp phân tầng (cascade layers)',
    'scope proximity': 'độ gần phạm vi (scope proximity)',
    'source order': 'thứ tự nguồn (source order)',
    'origin/importance': 'nguồn và mức quan trọng (origin/importance)',
    'specificity war': 'cuộc chiến độ đặc hiệu (specificity war)',
    'specificity': 'độ đặc hiệu (specificity)',
    'inheritance': 'kế thừa (inheritance)',
    'cascade': 'cơ chế phân tầng (cascade)',
    'selectors': 'các bộ chọn (selectors)',
    'selector': 'bộ chọn (selector)',
    'declarations': 'các khai báo (declarations)',
    'declaration': 'khai báo (declaration)',
    'properties': 'các thuộc tính (properties)',
    'property': 'thuộc tính (property)',
    'values': 'các giá trị (values)',
    'value': 'giá trị (value)',
    'pseudo-class': 'lớp giả (pseudo-class)',
    'pseudo-classes': 'các lớp giả (pseudo-classes)',
    'pseudo-element': 'phần tử giả (pseudo-element)',
    'pseudo-elements': 'các phần tử giả (pseudo-elements)',
    'accessibility': 'khả năng tiếp cận (accessibility)',
    'performance': 'hiệu năng (performance)',
    'debugging': 'gỡ lỗi (debugging)',
    'debug': 'gỡ lỗi (debug)',
    'fallback': 'phương án dự phòng (fallback)',
    'architecture': 'kiến trúc (architecture)',
    'design pattern': 'mẫu thiết kế (design pattern)',
    'design patterns': 'các mẫu thiết kế (design patterns)',
    'coding pattern': 'mẫu lập trình (coding pattern)',
    'coding patterns': 'các mẫu lập trình (coding patterns)',
    'language idiom': 'lối viết quen dùng của ngôn ngữ (language idiom)',
    'mental model': 'mô hình tư duy (mental model)',
    'anti-pattern': 'phản mẫu (anti-pattern)',
    'anti-patterns': 'các phản mẫu (anti-patterns)',
    'encapsulation': 'đóng gói (encapsulation)',
    'isolation': 'cô lập (isolation)',
    'semantics': 'ngữ nghĩa (semantics)',
    'semantic': 'mang tính ngữ nghĩa (semantic)',
    'state machine': 'máy trạng thái (state machine)',
    'state': 'trạng thái (state)',
    'states': 'các trạng thái (states)',
    'variant': 'biến thể (variant)',
    'variants': 'các biến thể (variants)',
    'breakpoint': 'điểm ngắt (breakpoint)',
    'breakpoints': 'các điểm ngắt (breakpoints)',
    'viewport': 'vùng nhìn (viewport)',
    'compile-time': 'thời điểm biên dịch (compile-time)',
    'runtime': 'thời gian chạy (runtime)',
    'module graph': 'đồ thị mô-đun (module graph)',
    'module system': 'hệ mô-đun (module system)',
    'module architecture': 'kiến trúc mô-đun (module architecture)',
    'module namespace': 'không gian tên mô-đun (module namespace)',
    'namespaces': 'các không gian tên (namespaces)',
    'namespace': 'không gian tên (namespace)',
    'selector unification': 'hợp nhất bộ chọn (selector unification)',
    'control flow': 'luồng điều khiển (control flow)',
    'side effect': 'tác dụng phụ (side effect)',
    'side effects': 'các tác dụng phụ (side effects)',
    'public surface': 'bề mặt công khai (public surface)',
    'public member': 'thành viên công khai (public member)',
    'private member': 'thành viên riêng tư (private member)',
    'deprecation': 'trạng thái ngừng khuyến nghị (deprecation)',
    'deprecated': 'đã ngừng khuyến nghị (deprecated)',
    'migration': 'chuyển đổi (migration)',
    'shadowing': 'che khuất biến (shadowing)',
    'interpolation': 'nội suy (interpolation)',
    'mutable state': 'trạng thái có thể thay đổi (mutable state)',
    'global mutable state': 'trạng thái toàn cục có thể thay đổi (global mutable state)',
    'compiler': 'trình biên dịch (compiler)',
    'source map': 'bản đồ mã nguồn (source map)',
    'source maps': 'các bản đồ mã nguồn (source maps)',
    'build pipeline': 'quy trình build (build pipeline)',
    'build tool': 'công cụ build (build tool)',
    'partials': 'các file thành phần (partials)',
    'partial': 'file thành phần (partial)',
    'mixins': 'các khối trộn tái sử dụng (mixins)',
    'mixin': 'khối trộn tái sử dụng (mixin)',
    'functions': 'các hàm (functions)',
    'function': 'hàm (function)',
    'variables': 'các biến (variables)',
    'variable': 'biến (variable)',
    'nesting': 'lồng cú pháp (nesting)',
    'scope': 'phạm vi (scope)',
    'maps': 'các map khóa–giá trị (maps)',
    'map': 'map khóa–giá trị (map)',
    'lists': 'các danh sách (lists)',
    'list': 'danh sách (list)',
    'utility-first mental model': 'mô hình tư duy ưu tiên tiện ích (utility-first mental model)',
    'utility-first': 'ưu tiên tiện ích (utility-first)',
    'candidate detection': 'phát hiện ứng viên lớp (candidate detection)',
    'source detection': 'phát hiện nguồn (source detection)',
    'content detection': 'phát hiện nội dung nguồn (content detection)',
    'state variant': 'biến thể trạng thái (state variant)',
    'state variants': 'các biến thể trạng thái (state variants)',
    'arbitrary value': 'giá trị tùy ý (arbitrary value)',
    'arbitrary values': 'các giá trị tùy ý (arbitrary values)',
    'arbitrary property': 'thuộc tính tùy ý (arbitrary property)',
    'arbitrary properties': 'các thuộc tính tùy ý (arbitrary properties)',
    'arbitrary variant': 'biến thể tùy ý (arbitrary variant)',
    'arbitrary variants': 'các biến thể tùy ý (arbitrary variants)',
    'theme variable': 'biến chủ đề (theme variable)',
    'theme variables': 'các biến chủ đề (theme variables)',
    'theme namespace': 'không gian tên chủ đề (theme namespace)',
    'theme contract': 'hợp đồng chủ đề (theme contract)',
    'css-first configuration': 'cấu hình ưu tiên CSS (CSS-first configuration)',
    'css-first': 'ưu tiên CSS (CSS-first)',
    'just-in-time': 'biên dịch tức thời (just-in-time)',
    'jit compiler': 'trình biên dịch tức thời (JIT compiler)',
    'jit': 'JIT (biên dịch tức thời)',
    'configuration': 'cấu hình (configuration)',
    'utilities': 'các tiện ích (utilities)',
    'utility': 'tiện ích (utility)',
    'safelist': 'danh sách ép giữ (safelist)',
    'preflight': 'Preflight (lớp reset nền của Tailwind)',
    'design system': 'hệ thống thiết kế (design system)',
    'component pattern': 'mẫu thành phần (component pattern)',
    'component patterns': 'các mẫu thành phần (component patterns)',
    'production pattern': 'mẫu dùng trong production (production pattern)',
    'production patterns': 'các mẫu dùng trong production (production patterns)',
}

ORDERED = sorted(TERMS.items(), key=lambda kv: len(kv[0]), reverse=True)
TOKEN_RE = re.compile('|'.join(r'(?<![\w-])' + re.escape(k) + r'(?![\w-])' for k, _ in ORDERED), re.IGNORECASE)
MAP = {k.lower(): v for k, v in ORDERED}
INLINE_CODE_RE = re.compile(r'(`+[^`]*?`+)')


def protect_inline_and_replace(line: str, counters: dict[str, int]) -> str:
    if 'http://' in line or 'https://' in line:
        return line
    parts = INLINE_CODE_RE.split(line)
    for i in range(0, len(parts), 2):
        segment = parts[i]
        placeholders: dict[str, str] = {}
        idx = 0
        def repl(m: re.Match[str]) -> str:
            nonlocal idx
            src = m.group(0)
            left = segment[:m.start()]
            right = segment[m.end():]
            if left.rfind('(') > left.rfind(')') and (')' in right and (right.find(')') < right.find('(') if '(' in right else True)):
                return src
            key = src.lower()
            replacement = MAP.get(key)
            if replacement is None:
                replacement = next(v for k, v in ORDERED if k.lower() == key)
            marker = f'§§TERM{idx}§§'
            idx += 1
            placeholders[marker] = replacement
            counters[key] = counters.get(key, 0) + 1
            return marker
        segment = TOKEN_RE.sub(repl, segment)
        for marker, replacement in placeholders.items():
            segment = segment.replace(marker, replacement)
        parts[i] = segment
    return ''.join(parts)


def fenced_blocks(text: str) -> list[str]:
    blocks = []
    lines = text.splitlines(keepends=True)
    inside = False
    buf = []
    marker = None
    for line in lines:
        stripped = line.lstrip()
        if not inside and (stripped.startswith('```') or stripped.startswith('~~~')):
            inside = True
            marker = stripped[:3]
            buf = [line]
        elif inside:
            buf.append(line)
            if stripped.startswith(marker):
                blocks.append(''.join(buf))
                inside = False
                buf = []
                marker = None
    return blocks


def insert_glossary(text: str, domain: str) -> str:
    if '## Quy ước thuật ngữ Việt–Anh' in text:
        return text
    lines = text.splitlines(keepends=True)
    pos = None
    for i, line in enumerate(lines[:80]):
        if line.strip() == '---':
            pos = i + 1
            break
    if pos is None:
        pos = 1
    lines.insert(pos, GLOSSARIES[domain])
    return ''.join(lines)


def transform(text: str, domain: str) -> tuple[str, dict[str, int]]:
    before_blocks = fenced_blocks(text)
    counters: dict[str, int] = {}
    out = []
    inside_fence = False
    fence_marker = None
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if not inside_fence and (stripped.startswith('```') or stripped.startswith('~~~')):
            inside_fence = True
            fence_marker = stripped[:3]
            out.append(line)
            continue
        if inside_fence:
            out.append(line)
            if stripped.startswith(fence_marker):
                inside_fence = False
                fence_marker = None
            continue
        out.append(protect_inline_and_replace(line, counters))
    result = insert_glossary(''.join(out), domain)
    after_blocks = fenced_blocks(result)
    if before_blocks != after_blocks:
        raise AssertionError('Fenced code blocks changed')
    if result.count('```') % 2 != 0:
        raise AssertionError('Unbalanced backtick fences')
    return result, counters


def domain_for(path: Path) -> str:
    s = str(path)
    if '/scss/' in s:
        return 'scss'
    if '/tailwind/' in s:
        return 'tailwind'
    return 'css'

summary = []
for path in FILES:
    if not path.exists():
        raise FileNotFoundError(path)
    original = path.read_text(encoding='utf-8')
    updated, counts = transform(original, domain_for(path))
    total = sum(counts.values())
    if total < 20:
        raise AssertionError(f'Too few terminology replacements in {path}: {total}')
    if updated == original:
        raise AssertionError(f'No changes in {path}')
    if '_v2.md' in updated or 'bản V2' in updated:
        raise AssertionError(f'Legacy V2 reference reintroduced in {path}')
    path.write_text(updated, encoding='utf-8')
    top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:8]
    summary.append((str(path), total, top))

print('VI-TERM-AUDIT: OK')
for path, total, top in summary:
    print(f'{path}: {total} replacements')
    print('  top:', ', '.join(f'{k}={v}' for k, v in top))

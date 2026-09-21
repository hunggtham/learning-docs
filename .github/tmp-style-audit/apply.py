from pathlib import Path
import base64, json, zlib

ROOT = Path('.')
CSS = ROOT / '10_frontend/css'
SCSS = ROOT / '10_frontend/scss'
TW = ROOT / '10_frontend/tailwind'
PAY = ROOT / '.github/tmp-style-audit'

def load(name):
    data = (PAY / f'{name}.b64').read_text().strip()
    return json.loads(zlib.decompress(base64.b64decode(data)).decode('utf-8'))

def insert_before(path, marker, block, signature):
    text = path.read_text(encoding='utf-8')
    if signature in text:
        return
    i = text.find(marker)
    if i < 0:
        raise RuntimeError(f'marker not found in {path}: {marker}')
    text = text[:i].rstrip() + '\n\n---\n\n' + block.strip() + '\n\n---\n\n' + text[i:].lstrip()
    path.write_text(text, encoding='utf-8')

css_data = (PAY/'css1.b64').read_text().strip() + (PAY/'css2.b64').read_text().strip()
cssb = json.loads(zlib.decompress(base64.b64decode(css_data)).decode('utf-8'))
scssb = load('scss')
twb = load('tailwind')

# CSS canonical rename and no document-version suffix.
old = CSS / 'CSS_Beginner_to_Senior_2026_v2.md'
new = CSS / 'CSS_Beginner_to_Senior_2026.md'
if old.exists() and not new.exists():
    old.rename(new)
elif old.exists() and new.exists():
    raise RuntimeError('Both old and new CSS canonical files exist')
if not new.exists():
    raise RuntimeError('CSS canonical file missing')

text = new.read_text(encoding='utf-8')
text = text.replace('# Cách đọc từng phần trong bản V2', '# Cách đọc tài liệu canonical')
text = text.replace('Từ bản này, mỗi nhóm kiến thức quan trọng được bổ sung theo 4 tầng tư duy:', 'Mỗi nhóm kiến thức quan trọng được đọc theo 4 tầng tư duy:')
text = text.replace('.special-card-v2', '.special-card-special')
text = text.replace('# 124. Cheat Sheet cực ngắn', '# 124. Appendix — syntax recap cực ngắn')
text = text.replace('Đây là index để review nhanh. Không cần học thuộc tất cả trong một lần.', 'Đây chỉ là appendix để tra cứu sau khi đã hiểu mental model ở các phần trước. Không dùng section này như learning path và không học thuộc property theo kiểu danh sách.')
new.write_text(text, encoding='utf-8')
insert_before(new, '# Kết luận', cssb['deep'], '# 132. Cascade & Specificity — trace quyết định declaration thắng')

cm = CSS / 'CSS_Master_Supplement_2026.md'
text = cm.read_text(encoding='utf-8')
repls = {
    '## Những phần còn thiếu sau `CSS_Beginner_to_Senior_2026_v2.md`': '## Những phần chuyên sâu sau `CSS_Beginner_to_Senior_2026.md`',
    '> **Mục tiêu:** file này **không lặp lại** handbook V2.': '> **Mục tiêu:** file này **không lặp lại** handbook canonical Beginner → Senior.',
    '> Hãy đọc file này **sau** `CSS_Beginner_to_Senior_2026_v2.md`.': '> Hãy đọc file này **sau** `CSS_Beginner_to_Senior_2026.md`.',
    '> V2\n': '> Canonical Beginner → Senior\n',
    '# 0. V2 đã đủ đến đâu?': '# 0. Canonical Beginner → Senior đã đủ đến đâu?',
    '## V2 đã cover rất tốt': '## Canonical Beginner → Senior đã cover rất tốt',
    'V2 nói cascade nhưng master cần hiểu': 'Canonical note đã giải thích cascade; ở mức master cần hiểu',
    'V2 đã có `min-width:0`.': 'Canonical note đã có `min-width:0`.',
    'Ngoài V2:': 'Ngoài canonical Beginner → Senior:',
    'V2 giới thiệu anchor positioning.': 'Canonical note giới thiệu anchor positioning.',
    'V2 có `@supports` nhưng master cần function query.': 'Canonical note có `@supports`; ở mức master cần hiểu function query.',
    '1. `CSS_Beginner_to_Senior_2026_v2.md`': '1. `CSS_Beginner_to_Senior_2026.md`',
    'Nếu chỉ đọc V2:': 'Nếu chỉ đọc canonical Beginner → Senior:',
    'V2 + Supplement + 20–30 advanced labs + project thật': 'Canonical Beginner → Senior + Supplement + 20–30 advanced labs + project thật',
    'V2 + Supplement': 'Canonical Beginner → Senior + Supplement',
}
for a, b in repls.items():
    text = text.replace(a, b)
text = text.replace('V2', 'Canonical Beginner → Senior')
cm.write_text(text, encoding='utf-8')
insert_before(cm, '# 1. Property Value Lifecycle [MUST][DEEP]', cssb['master'], '# 0B. Priority order của Master Supplement')

# SCSS canonical architecture.
s = SCSS / 'SCSS_Beginner_to_Senior_2026.md'
text = s.read_text(encoding='utf-8').replace('CSS_Beginner_to_Senior_2026_v2.md', 'CSS_Beginner_to_Senior_2026.md')
s.write_text(text, encoding='utf-8')
insert_before(s, '# Kết luận', scssb['arch'], '# 156. SCSS Architecture — thiết kế module graph')
sm = SCSS / 'SCSS_Master_Supplement_2026.md'
insert_before(sm, '# Kết luận', scssb['master'], '# 161. Module Graph Review')

# Tailwind mapping + version evolution.
t = TW / 'TailwindCSS_Beginner_to_Senior_2026_REWRITTEN.md'
insert_before(t, '# KẾT LUẬN', twb['deep'], '# PHẦN XXVIII — UNDERLYING CSS MAPPING VÀ VERSION EVOLUTION')
tm = TW / 'TailwindCSS_Master_Supplement_2026_REWRITTEN.md'
insert_before(tm, '# KẾT LUẬN', twb['master'], '# PHẦN XXVIII — VERSION BOUNDARIES VÀ CSS MAPPING Ở MỨC MASTER')

# Coverage / integrity validation.
css = (new.read_text(encoding='utf-8') + cm.read_text(encoding='utf-8')).lower()
scss = (s.read_text(encoding='utf-8') + sm.read_text(encoding='utf-8')).lower()
tw = (t.read_text(encoding='utf-8') + tm.read_text(encoding='utf-8')).lower()
all_text = css + scss + tw
assert 'css_beginner_to_senior_2026_v2.md' not in all_text
assert 'bản v2' not in css and 'handbook v2' not in css
for term in ['cascade & specificity', 'layout mental model', 'flexbox', 'grid', 'responsive', 'modern css', 'performance', 'accessibility', 'production patterns']:
    assert term in css, term
for term in ['scss architecture', 'module graph', '@use', '@forward', 'public api', 'generated css']:
    assert term in scss, term
for term in ['underlying css mapping', 'version evolution', 'tailwind v3', 'tailwind v4', 'v4.3', 'generated css', 'production pattern']:
    assert term in tw, term
for p in [new, cm, s, sm, t, tm]:
    fences = sum(1 for line in p.read_text(encoding='utf-8').splitlines() if line.startswith('```'))
    assert fences % 2 == 0, (p, fences)
    print(p, len(p.read_text(encoding='utf-8').splitlines()))

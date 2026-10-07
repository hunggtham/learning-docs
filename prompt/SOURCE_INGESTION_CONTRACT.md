# SOURCE INGESTION CONTRACT — raw, provenance and derived Markdown

Mục tiêu là đưa nguồn vào repository mà vẫn phân biệt được bản gốc, bản trích xuất, bản OCR, reference do AI tìm thêm và learning output.

## Layout chuẩn cho một corpus

\`\`\`text
<corpus>/
  raw/
    original/
    extracted/
    ocr/
    derived/
    _catalog/
    SOURCE_MANIFEST.yaml
  research/
    source-ledger.md
    unresolved-claims.md
  planning/
    semantic-map.tsv
    outline.md
  output/
  audit/
\`\`\`

## Quy tắc raw

1. \`raw/original/\` không được rewrite, translate hoặc format lại.
2. Mọi file trong \`raw/extracted/\`, \`raw/ocr/\` và \`raw/derived/\` phải ghi phương pháp tạo và source file gốc.
3. Markdown do AI nghiên cứu hoặc tổng hợp không được đặt ngang hàng với source; đặt trong \`research/\` hoặc \`raw/_catalog/\` với banner \`NOT CANONICAL SOURCE\`.
4. Cùng một source dùng cho nhiều corpus phải có \`source_id\` ổn định và provenance, không tạo các bản copy không thể phân biệt.
5. Không tạo output learning trước khi source quality và semantic coverage được ghi nhận.

## Source manifest tối thiểu

\`\`\`yaml
source_id:
path:
source_type: pdf | html | docx | image | markdown | url
origin:
source_url:
retrieved_at:
published_at:
language:
sha256:
extraction_method:
ocr_status: not_needed | pending | reviewed | failed
source_state: historical | current | unknown
trust_level: primary | secondary | unverified
notes:
\`\`\`

## Acceptance cho ingestion

- bản gốc mở được hoặc có lý do rõ nếu không mở được;
- hash và source path có trong manifest;
- OCR/extraction status không bị ghi \`reviewed\` nếu chưa kiểm tra đại diện;
- source/current-state ambiguity được ghi riêng;
- không có learning prose lẫn trong raw;
- downstream agent có thể biết file nào là input và file nào là derived.

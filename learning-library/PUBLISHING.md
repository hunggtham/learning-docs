# Publishing checklist

`library.config.json` is the only publication manifest. The Pages workflow copies only files under reviewed `allowedPrefixes` or explicit `allowedDocuments`; adding a file to the repository does not publish it.

Before adding a Markdown or PDF file, confirm one of these in your own records:

- you wrote it yourself;
- you have written permission to redistribute it; or
- it is public domain/openly licensed and the licence permits redistribution.

The build runs `scripts/audit-library.mjs` and fails closed when a path is inside a raw/imported folder or when Markdown contains common book-copyright notices. This is a safety check, not a legal determination.

## Current audit decision

- Published: the author-confirmed technical notes listed in the manifest.
- Published exception: `정보처리기사/output/` is exposed in the web library under the virtual `cert/` folder after the owner confirmed permission to publish that output. Its source captures remain held back.
- Held back: Korean source captures and intermediate material, including `raw`, `raw_md`, `notion`, `generated_markdown*`, `final*`, `merged_subjects`, and PDF/DOCX captures. These contain source quotations and provenance notes and are not published.
- Held back: `pmp/raw` and `pmp/workflow-output` because the cleaned text includes a publisher copyright notice and “all rights reserved”.
- English-language study materials are maintained in the separate `language-docs` repository; this repository does not store or publish English study Markdown files.
- Held back: imported SQL books and OCR/translation files, including `input/*`, `sql/raw*`, and the SQL lessons that explicitly say they closely follow a source PDF.

Official documentation links (for example MDN, W3C, Sass, Tailwind, IELTS.org or ETS) may remain as citations. A link is not a licence to republish the linked text, so do not copy passages, screenshots, test questions, or book pages into a published file.

To publish an approved file, add one object to `allowedDocuments`:

```json
{
  "path": "path/to/your-note.md",
  "title": "Readable title",
  "category": "Technical",
  "language": "vi-en",
  "rights": "author-confirmed"
}
```

For an approved folder that should appear under a different web location, an
`allowedPrefixes` entry may also set `displayPrefix`. This changes only the
published navigation path; it does not move or duplicate the source files.

Use `npm run audit:library` before `npm run build:library`. The site supports both `.md` and `.pdf`; Markdown under an approved prefix is discovered automatically, while PDFs remain explicit per-file entries after redistribution rights are confirmed. `raw` and `raw_md` are always skipped, and `output` is flattened only for display.

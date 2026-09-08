# Publishing checklist

`library.config.json` is the only publication manifest. The Pages workflow copies only the files listed there; adding a file to the repository does not publish it.

Before adding a Markdown or PDF file, confirm one of these in your own records:

- you wrote it yourself;
- you have written permission to redistribute it; or
- it is public domain/openly licensed and the licence permits redistribution.

The build runs `scripts/audit-library.mjs` and fails closed when a path is inside a raw/imported folder or when Markdown contains common book-copyright notices. This is a safety check, not a legal determination.

## Current audit decision

- Published: the author-confirmed technical notes and English grammar/exam guides listed in the manifest.
- Held back: all Korean material for now, including `raw`, `raw_md`, `notion`, `generated_markdown*`, `final*`, `merged_subjects`, and PDF/DOCX captures. The generated Korean lessons contain source quotations and provenance notes, so they need a separate rights review and rewriting pass before publication.
- Held back: `pmp/raw` and `pmp/workflow-output` because the cleaned text includes a publisher copyright notice and “all rights reserved”.
- Held back: imported IELTS/SQL books and OCR/translation files, including `ielts_docs/raw*`, `input/*`, `sql/raw*`, and the SQL lessons that explicitly say they closely follow a source PDF.

Official documentation links (for example MDN, W3C, Sass, Tailwind, IELTS.org or ETS) may remain as citations. A link is not a licence to republish the linked text, so do not copy passages, screenshots, test questions, or book pages into a published file.

To publish an approved file, add one object to `allowedDocuments`:

```json
{
  "path": "path/to/your-note.md",
  "title": "Readable title",
  "category": "English",
  "language": "en-vi",
  "rights": "author-confirmed"
}
```

Use `npm run audit:library` before `npm run build:library`. The site supports both `.md` and `.pdf`; a PDF should only be added after its redistribution rights are confirmed.

# Study Shelf

A lightweight GitHub Pages reader for the Markdown and PDF files stored in this workspace.

## What it does

- Builds a searchable document catalogue from safe folder prefixes plus explicit `.md`/`.pdf` entries.
- Renders Markdown in a clean reading layout with a table of contents.
- Opens PDFs in the browser's native PDF reader.
- Lets readers filter by Markdown/PDF and open or download the original file.
- Shows subfolders and files; `raw`/`raw_md` are hidden, and `output` is flattened in the displayed path.
- Runs a fail-closed publication audit before copying anything into the Pages artifact.
- Works as a static site: no account, database, or server is required.

## Local preview

From this directory:

```bash
npm run build:library
npm run serve
```

Then open `http://localhost:4173`.

## Add a document safely

Only files under reviewed prefixes or explicit paths in `library.config.json` are copied into the published site. Add a path/prefix **only after confirming you own it, have redistribution permission, or it has a compatible open licence/public-domain status**. Audit first:

```bash
npm run audit:library
```

Use `allowedPrefixes` for reviewed Markdown folders. The `output` segment is removed only from the display path; files are still copied and readable. PDFs remain per-file opt-in:

```json
{
  "allowedPrefixes": [
    { "path": "10_frontend", "category": "Frontend", "language": "vi-en", "rights": "author-confirmed" }
  ],
  "allowedDocuments": [
    {
      "path": "dev_everyday/everyday.md",
      "title": "Everyday notes",
      "category": "Personal",
      "language": "vi",
      "rights": "author-confirmed"
    }
  ]
}
```

See [PUBLISHING.md](PUBLISHING.md) for the current Korean/English source review and the paths intentionally held back.

## GitHub Pages setup

This project expects **the workspace root** (`00.my-learning`) to be the Git repository, because the build scans the folders beside `learning-library`.

1. Create a GitHub repository and push this workspace root to its `main` branch.
2. In GitHub, open **Settings → Pages** and set the source to **GitHub Actions**.
3. Push a change. The included workflow builds and deploys the site automatically.

### Important publishing note

The deployment artifact contains copies of every allow-listed file. Do not deploy publicly unless you have permission to publish every included document.

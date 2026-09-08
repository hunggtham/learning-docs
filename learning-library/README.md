# Study Shelf

A lightweight GitHub Pages reader for the Markdown and PDF files stored in this workspace.

## What it does

- Builds a searchable document catalogue from an explicit allow-list of `.md` and `.pdf` files.
- Renders Markdown in a clean reading layout with a table of contents.
- Opens PDFs in the browser's native PDF reader.
- Lets readers filter by Markdown/PDF and open or download the original file.
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

Only files named in `library.config.json` are copied into the published site. Add a path **only after confirming you own it, have redistribution permission, or it has a compatible open licence/public-domain status**. Audit first:

```bash
npm run audit:library
```

Then add an object so the title/category/language shown in the catalogue are explicit:

```json
{
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

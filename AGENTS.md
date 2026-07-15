# Codex repository instructions

## Rendered research documents only

Markdown is an internal authoring and storage format in this repository. It must never be exposed as the reader experience.

- Never add a user-facing **Raw**, **Raw .md**, **Open raw**, **Open file**, or Markdown-download control.
- Never use a `.md` file as the final destination of a reader-facing link. Register research documents in the appropriate topic viewer; route other Markdown through `markdown-viewer.html` and `site-router.js`.
- A document-loading failure must offer served-site/retry guidance only. It must not reveal, link to, or recommend opening the underlying Markdown file.
- Source Markdown filenames may exist in code or hidden routing metadata, but they must not be interactive or visible as a raw-document option.
- Preserve PDFs, datasets, images, and archived source captures as direct-file links when appropriate; this rule is specifically about Markdown research pages.
- Keep `site-documents.js` current by running `python3 tools/build_embedded_documents.py` after regenerating `site-router.js`. This embedded source bundle lets rendered viewers work when the archive is opened directly from disk as well as from a web server.
- Before handing off site work, run `python3 tools/check_rendered_document_policy.py`, regenerate `site-router.js`, rebuild `site-documents.js`, run the whole-site audit, and verify that new documents open in their rendered viewer on both desktop and mobile.

This repository rule is stricter than any general tooling convention that permits an explicitly labeled raw Markdown link.

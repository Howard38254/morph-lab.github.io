# Morph Lab Site

Academic research lab website for **Morph Lab** — built with [Jekyll](https://jekyllrb.com/) + [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) and deployed via GitHub Pages.

---

## Quick Start (local development)

```bash
# Install Ruby dependencies
bundle install

# Serve locally
bundle exec jekyll serve --livereload
# → open http://localhost:4000
```

---

## Site Structure

```
morph-lab.github.io/
├── _config.yml          # Site configuration (title, author, theme settings)
├── index.md             # Home page
├── _pages/
│   ├── research.md      # Research overview (auto-lists _research/ collection)
│   ├── people.md        # People page (renders _data/people.yml)
│   ├── publications.md  # Publications (ORCID sync + outputs)
│   └── showcase.md      # Poster gallery (auto-lists _showcase/ collection)
├── _data/
│   ├── navigation.yml   # Top navigation links
│   ├── people.yml       # Lab members — edit to add/remove people
│   ├── publications.json# Auto-synced from ORCID (do not edit manually)
│   └── outputs.yml      # Manual lab outputs (preprints, theses, etc.)
├── _research/           # One .md file per research project
├── _showcase/           # One .md file per poster entry
├── assets/
│   ├── images/
│   │   └── people/      # Profile photos (filename matches people.yml)
│   └── showcase/        # Poster PDFs and preview images
└── scripts/
    └── sync_orcid.py    # ORCID sync script (run by GitHub Action)
```

---

## Common Edits

### Add a lab member

Edit `_data/people.yml`. Add an entry to the appropriate section
(`pi`, `grad_students`, `postdocs`, `undergrads`). Place a square photo in
`assets/images/people/` and reference it in the `photo:` field.

### Add a research project

Create `_research/project-slug.md` using the existing example as a template.

### Add a publication output (non-ORCID)

Add an entry to `_data/outputs.yml`. These appear in the "Lab Outputs" section
of the Publications page.

### Add a poster (student PR workflow)

1. Add poster PDF + optional preview image to `assets/showcase/`:
   ```
   assets/showcase/your-name-conference-year.pdf
   assets/showcase/your-name-conference-year-preview.jpg
   ```
2. Create `_showcase/your-name-conference-year.md`:
   ```markdown
   ---
   title: "Poster Title"
   author: "Your Name"
   event: "Conference Name 2025"
   year: 2025
   pdf: /assets/showcase/your-name-conference-year.pdf
   image: /assets/showcase/your-name-conference-year-preview.jpg
   ---
   Brief description of the poster.
   ```
3. Open a Pull Request — a maintainer will review and merge.

---

## Publications — ORCID Sync

Publications are automatically synced from ORCID `0000-0002-8219-8983` via a
GitHub Action that runs every Sunday.

**Manually trigger a sync:**

1. Go to **Actions → Sync ORCID Publications → Run workflow**

**Sync script:** `scripts/sync_orcid.py`  
**Output:** `_data/publications.json` (committed automatically by the Action)

---

## Permissions & Contributing

| Role | Access |
|------|--------|
| PI / core maintainers | Write access (direct push to `main`) |
| Lab members | Fork → PR workflow |
| External contributors | Fork → PR workflow |

To request write access, contact the PI or open an issue.

---

## Deployment

The site deploys automatically to GitHub Pages via the
[jekyll.yml](.github/workflows/jekyll.yml) workflow on every push to `main`.

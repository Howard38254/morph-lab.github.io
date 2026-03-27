# Website Update Cheat Sheet

This guide explains how to update the Morph Lab website. The site is built with **Jekyll**, which separates content into **Markdown (.md)** and **Data (.yml)**.

---

## 📄 Use `.md` (Markdown) for Narrative Content
Use these files for free-form text, detailed descriptions, and creating new pages.

*   **Examples:** `index.md`, `_research/project-name.md`, `_showcase/poster.md`.
*   **Rule of Thumb:** If it feels like a "document" with paragraphs and headers, it belongs in a `.md` file.
*   **Front Matter:** The section at the top between `---` markers is the settings for that page (title, layout, permalink, etc.).

---

## 📊 Use `.yml` (YAML) for Structured Data
Use these files for lists of similar items that are automatically formatted by the website.

*   **Examples:** `_data/people.yml`, `_data/outputs.yml`, `_data/navigation.yml`.
*   **Rule of Thumb:** If you are adding a name, a link, or a year to a list, edit the `.yml` file.
*   **Syntax:** Use `key: value` pairs. Be careful with indentation (spaces only, no tabs!).

---

## ⚙️ The Global Control Panel: `_config.yml`
This file controls the **entire site**. Only change this when you want to:
*   Update the lab's official name or subtitle.
*   Update Dr. Haughn's (PI) bio, location, or social links in the sidebar.
*   Change the overall theme colors or site plugins.

---

## 🚀 Quick Reference Table

| Goal | File Type | Path/File |
| :--- | :--- | :--- |
| **Change the text on the Home page** | `.md` | `index.md` |
| **Add a new student or researcher** | `.yml` | `_data/people.yml` |
| **Add a detailed research project** | `.md` | `_research/project-slug.md` |
| **Add a non-ORCID publication** | `.yml` | `_data/outputs.yml` |
| **Change the top navigation menu** | `.yml` | `_data/navigation.yml` |
| **Change the site's title or subtitle** | `.yml` | `_config.yml` |
| **Adjust Site Width/Bio layout** | `.scss` | `assets/css/main.scss` |
| **Change People card size/grid** | `.md` | `_pages/people.md` |

---

## 🛠️ Testing Locally
To see changes before pushing to GitHub:
1. Open terminal in project folder.
2. Run `bundle exec jekyll serve --livereload`.
3. Open `http://localhost:4000` in your browser.
4. **ORCID Sync:** Run `python scripts/sync_orcid.py` to update publications data.

---

## ☁️ Deploying Changes
Simply **commit and push** your changes to the `main` branch. GitHub Actions will automatically rebuild and deploy the site.

---
title: "Poster Showcase"
layout: single
permalink: /showcase/
---

Posters presented at conferences, symposia, and lab open houses.

> **Want to add your poster?**
> See the [contribution guide](#how-to-add-your-poster) below.

---

<style>
.showcase-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}
.showcase-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.06);
  transition: box-shadow 0.2s;
}
.showcase-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.12); }
.showcase-card-img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  background: #f0f4f8;
  display: flex;
  align-items: center;
  justify-content: center;
}
.showcase-card-img img { width: 100%; height: 180px; object-fit: cover; }
.showcase-card-img .no-image {
  width: 100%;
  height: 180px;
  background: linear-gradient(135deg, #2e6da4 0%, #5a9fd4 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 2rem;
}
.showcase-card-body { padding: 0.9rem; }
.showcase-card-body h3 { margin: 0 0 0.3rem; font-size: 1rem; }
.showcase-card-body .meta { font-size: 0.82rem; color: #666; margin-bottom: 0.5rem; }
.showcase-card-body .links a { margin-right: 0.5rem; font-size: 0.85rem; }
</style>

{% assign posters = site.showcase | sort: "year" | reverse %}
{% if posters.size > 0 %}
<div class="showcase-grid">
{% for poster in posters %}
<div class="showcase-card">
  <div class="showcase-card-img">
    {% if poster.image %}
    <img src="{{ poster.image | relative_url }}" alt="{{ poster.title }}">
    {% else %}
    <div class="no-image">📄</div>
    {% endif %}
  </div>
  <div class="showcase-card-body">
    <h3>{{ poster.title }}</h3>
    <div class="meta">
      {{ poster.author }}{% if poster.event %} · {{ poster.event }}{% endif %}{% if poster.year %} ({{ poster.year }}){% endif %}
    </div>
    {% if poster.content != "" %}
    <p style="font-size:0.85rem; color:#444;">{{ poster.content | strip_html | truncatewords: 20 }}</p>
    {% endif %}
    <div class="links">
      {% if poster.pdf %}<a href="{{ poster.pdf | relative_url }}" target="_blank">📥 PDF</a>{% endif %}
      <a href="{{ poster.url | relative_url }}">Details →</a>
    </div>
  </div>
</div>
{% endfor %}
</div>
{% else %}
*No posters yet. Be the first to [add yours](#how-to-add-your-poster)!*
{% endif %}

---

## How to Add Your Poster

Contributing a poster is a **two-file PR**:

### 1. Upload your files to `assets/showcase/`

```
assets/showcase/your-name-conference-year.pdf          ← required
assets/showcase/your-name-conference-year-preview.jpg  ← recommended
```

### 2. Create a markdown entry in `_showcase/`

Create `_showcase/your-name-conference-year.md`:

```markdown
---
title: "Your Poster Title"
author: "Your Name"
event: "Conference Name 2025"
year: 2025
pdf: /assets/showcase/your-name-conference-year.pdf
image: /assets/showcase/your-name-conference-year-preview.jpg
---

One or two sentences describing the work presented on this poster.
```

### 3. Open a Pull Request

Submit the PR to `main`. A maintainer will review and merge it, and the site will update automatically.

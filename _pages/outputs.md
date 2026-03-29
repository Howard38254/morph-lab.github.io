---
title: "Lab Outputs & Showcase"
layout: single
permalink: /outputs/
toc: true
toc_label: "Sections"
toc_sticky: true
---

A collection of posters, preprints, theses, and other research outputs from the lab.

> **Peer-reviewed publications** are on the [Publications page](/publications/), synced automatically from ORCID.

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

## Poster Showcase

Posters presented at conferences, symposia, and lab open houses.

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
*No posters yet. See the contribution guide at the bottom of this page to add yours!*
{% endif %}

---

{% assign outputs = site.data.outputs %}
{% if outputs and outputs.size > 0 %}

{% assign preprints = outputs | where: "type", "preprint" %}
{% assign theses = outputs | where: "type", "thesis" %}
{% assign reports = outputs | where: "type", "report" %}
{% assign datasets = outputs | where: "type", "dataset" %}
{% assign software = outputs | where: "type", "software" %}
{% assign other_outputs = outputs | where: "type", "other" %}

{% if preprints.size > 0 %}
## Preprints

{% for item in preprints %}
- {% if item.url %}**[{{ item.title }}]({{ item.url }}){:target="_blank"}**{% else %}**{{ item.title }}**{% endif %}
  *{{ item.authors }}* · {{ item.venue | default: "" }} · {{ item.year }}
  {% if item.description %}{{ item.description }}{% endif %}

{% endfor %}
{% endif %}

{% if theses.size > 0 %}
## Theses

{% for item in theses %}
- {% if item.url %}**[{{ item.title }}]({{ item.url }}){:target="_blank"}**{% else %}**{{ item.title }}**{% endif %}
  *{{ item.authors }}* · {{ item.venue | default: "" }} · {{ item.year }}
  {% if item.description %}{{ item.description }}{% endif %}

{% endfor %}
{% endif %}

{% if reports.size > 0 %}
## Reports

{% for item in reports %}
- {% if item.url %}**[{{ item.title }}]({{ item.url }}){:target="_blank"}**{% else %}**{{ item.title }}**{% endif %}
  *{{ item.authors }}* · {{ item.venue | default: "" }} · {{ item.year }}

{% endfor %}
{% endif %}

{% if datasets.size > 0 %}
## Datasets

{% for item in datasets %}
- {% if item.url %}**[{{ item.title }}]({{ item.url }}){:target="_blank"}**{% else %}**{{ item.title }}**{% endif %}
  *{{ item.authors }}* · {{ item.venue | default: "" }} · {{ item.year }}

{% endfor %}
{% endif %}

{% if software.size > 0 %}
## Software

{% for item in software %}
- {% if item.url %}**[{{ item.title }}]({{ item.url }}){:target="_blank"}**{% else %}**{{ item.title }}**{% endif %}
  *{{ item.authors }}* · {{ item.venue | default: "" }} · {{ item.year }}

{% endfor %}
{% endif %}

{% if other_outputs.size > 0 %}
## Other

{% for item in other_outputs %}
- {% if item.url %}**[{{ item.title }}]({{ item.url }}){:target="_blank"}**{% else %}**{{ item.title }}**{% endif %}
  *{{ item.authors }}* · {{ item.venue | default: "" }} · {{ item.year }}

{% endfor %}
{% endif %}

{% else %}
*No other outputs listed yet. Add entries to `_data/outputs.yml` to populate this section.*
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

---
title: "Publications"
layout: single
permalink: /publications/
toc: true
toc_label: "Sections"
toc_sticky: true
---

## Publications (synced from ORCID)

<a href="https://scholar.google.com/citations?user=waDZzkAAAAAJ&hl=en" class="btn btn--primary" target="_blank">
  <i class="fas fa-graduation-cap"></i> Google Scholar Profile
</a>
<a href="https://orcid.org/0000-0002-8219-8983" class="btn btn--info" target="_blank">
  <i class="fab fa-orcid"></i> ORCID Profile
</a>

*Automatically synced from ORCID `0000-0002-8219-8983`. Updated weekly via GitHub Actions.*

---

{% assign pubs = site.data.publications %}
{% if pubs and pubs.size > 0 %}
{% assign pubs_by_year = pubs | group_by: "year" | sort: "name" | reverse %}
{% for year_group in pubs_by_year %}

### {{ year_group.name }}

{% for pub in year_group.items %}
- **{{ pub.title }}**
  {% if pub.authors %}*{{ pub.authors }}*{% endif %}
  {% if pub.journal %}{{ pub.journal }}.{% endif %}
  {% if pub.year %}{{ pub.year }}.{% endif %}
  {% if pub.doi %}<a href="https://doi.org/{{ pub.doi }}" target="_blank">DOI: {{ pub.doi }}</a>{% elsif pub.url %}<a href="{{ pub.url }}" target="_blank">Link</a>{% endif %}

{% endfor %}
{% endfor %}
{% else %}
*No publications loaded yet. [Run the ORCID sync action](https://github.com/haughn-morph-lab/morph-lab.github.io/actions/workflows/orcid-sync.yml) to populate this list, or check back after the weekly automated sync.*
{% endif %}

---

## Lab Outputs (non-peer-reviewed / internal / in-progress)

{% assign outputs = site.data.outputs %}
{% if outputs and outputs.size > 0 %}

| Year | Title | Type | Venue |
|------|-------|------|-------|
{% for item in outputs %}
| {{ item.year }} | {% if item.url %}[{{ item.title }}]({{ item.url }}){:target="_blank"}{% else %}{{ item.title }}{% endif %} | {{ item.type | capitalize }} | {{ item.venue | default: "—" }} |
{% endfor %}

{% else %}
*No outputs listed yet. Add entries to `_data/outputs.yml`.*
{% endif %}

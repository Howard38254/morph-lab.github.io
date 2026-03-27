---
title: "Research"
layout: single
permalink: /research/
toc: true
toc_label: "Projects"
toc_sticky: true
---

Our multidisciplinary lab draws inspiration from biological systems to investigate
the interactions between sensing, morphology, and control to develop novel intelligent
systems.

---

## Active Projects

{% assign sorted_projects = site.research | sort: "order" %}
{% for project in sorted_projects %}
### [{{ project.title }}]({{ project.url | relative_url }})

{{ project.excerpt | default: project.content | strip_html | truncatewords: 50 }}

{% if project.tags %}
**Keywords:** {{ project.tags | join: " · " }}
{% endif %}

---
{% endfor %}

{% if site.research.size == 0 %}
*Research project pages coming soon. Add files to `_research/` to populate this section.*
{% endif %}

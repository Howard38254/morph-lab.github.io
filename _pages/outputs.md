---
title: "Lab Outputs"
layout: single
permalink: /outputs/
toc: true
toc_label: "By Type"
toc_sticky: true
---

Non-peer-reviewed work, internal reports, theses, datasets, and in-progress manuscripts from the lab.

> **Peer-reviewed publications** are on the [Publications page](/publications/), synced automatically from ORCID.

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
*No outputs listed yet. Add entries to `_data/outputs.yml` to populate this page.*
{% endif %}

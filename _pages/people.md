---
title: "People"
layout: single
permalink: /people/
---

<style>
.person-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}
.person-card {
  text-align: center;
  padding: 1rem;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background: #fafafa;
}
.person-card img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 0.75rem;
}
.person-card img.placeholder {
  background: #ccc;
}
.person-card h3 { margin: 0.25rem 0; font-size: 1.05rem; }
.person-card .role { color: #555; font-size: 0.9rem; margin-bottom: 0.4rem; }
.person-card .bio { font-size: 0.85rem; color: #444; }
.person-links a { margin: 0 0.25rem; font-size: 0.85rem; }
</style>

## Principal Investigator

{% assign pi = site.data.people.pi %}
<div class="person-grid">
{% for person in pi %}
<div class="person-card">
  {% if person.photo %}
  <img src="{{ person.photo | relative_url }}" alt="{{ person.name }}" onerror="this.style.display='none'">
  {% endif %}
  <h3>{{ person.name }}</h3>
  <div class="role">{{ person.role }}</div>
  {% if person.bio %}<div class="bio">{{ person.bio }}</div>{% endif %}
  <div class="person-links">
    {% if person.email %}<a href="mailto:{{ person.email }}">Email</a>{% endif %}
    {% if person.orcid %}<a href="{{ person.orcid }}" target="_blank">ORCID</a>{% endif %}
    {% if person.scholar %}<a href="{{ person.scholar }}" target="_blank">Scholar</a>{% endif %}
    {% if person.website %}<a href="{{ person.website }}" target="_blank">Website</a>{% endif %}
  </div>
</div>
{% endfor %}
</div>

---

## Graduate Students

{% assign grads = site.data.people.grad_students %}
{% if grads and grads.size > 0 %}
<div class="person-grid">
{% for person in grads %}
<div class="person-card">
  {% if person.photo %}<img src="{{ person.photo | relative_url }}" alt="{{ person.name }}" onerror="this.style.display='none'">{% endif %}
  <h3>{{ person.name }}</h3>
  <div class="role">{{ person.role }}</div>
  {% if person.bio %}<div class="bio">{{ person.bio }}</div>{% endif %}
  <div class="person-links">
    {% if person.email %}<a href="mailto:{{ person.email }}">Email</a>{% endif %}
    {% if person.orcid %}<a href="{{ person.orcid }}" target="_blank">ORCID</a>{% endif %}
    {% if person.website %}<a href="{{ person.website }}" target="_blank">Website</a>{% endif %}
  </div>
</div>
{% endfor %}
</div>
{% else %}
*No graduate students listed yet.*
{% endif %}

---

## Postdoctoral Researchers

{% assign postdocs = site.data.people.postdocs %}
{% if postdocs and postdocs.size > 0 %}
<div class="person-grid">
{% for person in postdocs %}
<div class="person-card">
  {% if person.photo %}<img src="{{ person.photo | relative_url }}" alt="{{ person.name }}" onerror="this.style.display='none'">{% endif %}
  <h3>{{ person.name }}</h3>
  <div class="role">{{ person.role }}</div>
  {% if person.bio %}<div class="bio">{{ person.bio }}</div>{% endif %}
</div>
{% endfor %}
</div>
{% else %}
*No postdoctoral researchers listed yet.*
{% endif %}

---

## Undergraduate Researchers

{% assign undergrads = site.data.people.undergrads %}
{% if undergrads and undergrads.size > 0 %}
<div class="person-grid">
{% for person in undergrads %}
<div class="person-card">
  {% if person.photo %}<img src="{{ person.photo | relative_url }}" alt="{{ person.name }}" onerror="this.style.display='none'">{% endif %}
  <h3>{{ person.name }}</h3>
  <div class="role">{{ person.role }}</div>
  {% if person.bio %}<div class="bio">{{ person.bio }}</div>{% endif %}
</div>
{% endfor %}
</div>
{% else %}
*No undergraduate researchers listed yet.*
{% endif %}

---

## Alumni

{% assign alumni = site.data.people.alumni %}
{% if alumni and alumni.size > 0 %}
| Name | Role | Year Left | Current Position |
|------|------|-----------|-----------------|
{% for person in alumni %}
| {{ person.name }} | {{ person.role }} | {{ person.year_left }} | {{ person.current_position | default: "—" }} |
{% endfor %}
{% else %}
*No alumni listed yet.*
{% endif %}

---
layout: default
title: About us
---

# About Us

## OJC Technologies. Bringing your system to life.

OJC Technologies was founded in June 2011 by Oliver Clarke after working at a large multinational systems integrator. Oliver formed OJC Technologies in order to provide its customers with a flexible capability to support the growing demand for software development services.

OJC Technologies continues to grow in this area and has since been able to supplement our capabilities with comprehensive systems engineering in order to support our customers and continue to provide high quality software and systems services.

# The Team

## Meet the team

{% for member in site.data.team %}

### {{ member.name }}
<small>{{member.position}}</small>

{{ member.bio }}

[linkedIn]({{ member.linkedin }})


{% endfor %}

---
layout: cover
title: About us
---

# About Us

## OJC Technologies. Bringing your system to life.

OJC Technologies was founded in June 2011 by Oliver Clarke after working at a large multinational systems integrator. Oliver formed OJC Technologies in order to provide its customers with a flexible capability to support the growing demand for software development services.

OJC Technologies continues to grow in this area and has since been able to supplement our capabilities with comprehensive systems engineering in order to support our customers and continue to provide high quality software and systems services.

# The Team

## Meet the team


<div class="row">
{% for member in site.data.team %}

  <div class="col-lg-6">
    <img class="img-circle" src="https://unsplash.it/140?random" alt="Generic placeholder image" width="140" height="140">
    <h2>{{ member.name }}</h2>
    <small>{{member.position}}</small>
    <p>{{ member.bio }}</p>
    <p><a class="btn btn-default" href="{{member.linkedin}}" role="button">linkedIn</a></p>
  </div><!-- /.col-lg-6 -->

{% endfor %}

</div>

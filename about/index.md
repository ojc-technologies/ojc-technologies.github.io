---
layout: pure-simple
title: Meet the team
banner: OJC Technologies. Bringing your system to life.
---

<h2 class="content-head is-centre">Meet the team</h2>

OJC Technologies was founded in June 2011 by Oliver Clarke after working at a large multinational systems integrator. Oliver formed OJC Technologies in order to provide its customers with a flexible capability to support the growing demand for software development services.

OJC Technologies continues to grow in this area and has since been able to supplement our capabilities with comprehensive systems engineering in order to support our customers and continue to provide high quality software and systems services.

<div class="pure-g">
{% for member in site.data.team %}
    <div class="pure-u-1 pure-u-md-1-2 pure-u-lg-1-2 is-centre">
      <div class="box">
        <img class="img-circle" style="display:block;margin:0 auto;" src="https://unsplash.it/140?random" alt="Generic placeholder image" width="140" height="140">
        <h3 class="content-subhead">
            {{ member.name }}
        </h3>
        <small>{{member.position}}</small>
        <p>
            {{ member.bio }}
        </p>
        <p><a class="pure-button" href="{{member.linkedin}}"><i class="fa fa-linkedin"></i></a></p>
      </div>
    </div>
{% endfor %}
</div>

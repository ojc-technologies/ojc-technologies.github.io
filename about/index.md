---
title: Meet the team
banner: OJC Technologies. Bringing your system to life.
---

# Meet the team

OJC Technologies was founded in June 2011 by Oliver Clarke after working at a large multinational systems integrator. Oliver formed OJC Technologies in order to provide its customers with a flexible capability to support the growing demand for software development services.

OJC Technologies continues to grow in this area and has since been able to supplement our capabilities with comprehensive systems engineering in order to support our customers and continue to provide high quality software and systems services.

<div class="grid-x grid-margin-x">
{% for person in site.data.team %}
  <!-- User card example #1 -->
  <div class="cell large-auto card-user-container">

    <!--card's image-->
    <div class="card-user-avatar">
      <img src="{{person.picture}}" alt="" class="user-image">
    </div>

    <div class="card-user-social">
      <ul class="menu">
        <li class="fa fa-twitter"></li>
        <li class="fa fa-linkedin"></li>
        <li class="fa fa-github"></li>
      </ul>
    </div>

    <div class="card-user-bio">
      <h4>{{ person.name }}</h4>
      <p>{{ person.bio }}</p>
      <span class="location-text">{{person.position}}</span>
    </div>



    <!--card's follow button-->
    <div class="card-user-button">
      <a href="#" class="hollow button">FOLLOW</a>
    </div>
  </div>
{% endfor %}
</div>

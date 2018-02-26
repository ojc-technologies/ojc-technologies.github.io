---
layout: post
title: First foray into Jekyll
author: Oliver
date: 2017-03-07
category: development
image: /assets/img/jekyll-post.jpg
tags: development markdown
---

We've just relanched our website, taking advantage of [Jekyll](http://jekyllrb.com/) as a replacement for traditional content management systems such as Wordpress. Jekyll is a Ruby framework that lets you write templates for pages and build websites using static Markdown files for your content.

## Why use static website generation and why is it different?
Many websites these days utilise

### Less Complexity

Jekyll sites are basically static sites with an extra templating language called Liquid so it’s a small step to learn if you already know HTML, CSS and JavaScript. We can actually start with a static site and then introduce Jekyll functionality as it’s needed.

### You can use Markdown to write content

As a software development company and an avid user of [Markdown](https://daringfireball.net/projects/markdown/syntax) and [CommonMark](http://commonmark.org) it seemed a good fit that we utilise GitHub to write, version control and host our website.

Writing in Markdown allows for not only a nice clean syntax which is easily readable in its [raw form](https://github.com/ojc-technologies/ojc-technologies.github.io/blob/master/_posts/2017-03-07-foray-into-jekyll.md), but also provides a mechanism to output using [multiple](https://pandoc.org/) [different](https://www.npmjs.com/package/markdown) [rendering](https://github.com/webpro/reveal-md) [engines](https://www.markdowntopdf.com/). You can even write and edit on the fly using one of the many [online editors](http://spec.commonmark.org/dingus/).
This gives us a really neat way to reuse the same [version controlled content](https://github.com/ojc-technologies/ojc-technologies.github.io/) for presentations, marketing collateral and our [blog](/blog).

## Running Jekyll locally using Docker

`docker run --rm --volume="${PWD}:/srv/jekyll" -it jekyll/builder jekyll build`


## Hosting on GitHub

Whilst the plan was to take advantage of [GitHub Pages hosting](https://pages.github.io/). It looks as though it might be lacking a little bit due to an absence of full end-to-end HTTPS support for custom domains. The
provided GitHub pages site [does support](https://github.com/blog/2186-https-for-github-pages/) `*.github.io` pages which is great because you get the benefits of HTTP/2 when using a github.io domain, but you either have to front with a CDN such as [CloudFare](https://www.cloudfare.com/) and accept that the TLS will be terminated at each hop (i.e. at CloudFare, then re-established to the github.io host) or concede that users have to add an exception to their browser which trusts `*.github.io` as a host for the custom domain - this is bad!

Not using Markdown yet? What are you waiting for [get started](http://commonmark.org/help/) with the [10 minute tutorial](http://commonmark.org/help/tutorial/)

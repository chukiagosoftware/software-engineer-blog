---
title: "Intro" 
date: 2026-02-01
draft: false
---


{{< emoji sunrise >}}


## About Me {{< emoji mage_man >}}

Officially a Computer and Electrical Engineer, B.Sc. (nice!). I've also been a Network and Security, then Devops,
Site Reliability and more recently an AI, AWS and Go engineer. This is my blog, not a portfolio. Just some notes and
my most recent CI/CD and programming language which is Github Actions and Go. I've also used Jenkins, ArgoCD, Cloudbuild,
Python, Javascript but, I'm not going to talk about those.

My speciality du jour is building, deploying apps written in Go and Python and handling AWS, Kubernetes, OpenTelemetry or Prometheus metrics 
for an end to end system such as for Generative AI (Large Language Models) applications.

While I am solely responsible for all this crap- I mean, content- I do have to thank Grok and Claude for helping make the
conversion fast and mostly painless. Also, thanks to my friends and family for supporting me and my wife.

<!--more-->


### The Icons {{< emoji shipit >}}

~~The site runs on Python 3.10 with the Pelican 4.8.0 microblog software and my custom Python Markdown 3.4.1 extension
for the Github Emojis. These are just the publicly available emojis which you can see around the pages. I find that
there are some really, really cool ones and thus without further ado.~~

Actually, this is no longer true. This is now a Go Hugo site. Which is why you don't see most emojis yet.

At some point I will figure out what/how to get sweet Github Emojis or a better alternative going.

For now, we have Hugo's emojis which are not bad.

### The Platform {{< emoji godmode >}}

The code is deployed based on Git ops. In other words, the Python code which generates html, is pushed to a main branch
integrated with Ci/Cd service [Netlify](https://www.netlify.com)

I use Jetbrains Pycharm, so this is done either by typing *git push* in the Terminal or Cmd-K in the IDE window. I
highly recommend it.

Other options considered for deployment were Google App Engine, [Render](https://www.render.com) and a VM on Digital
Ocean or a [free Oracle VM](https://docs.oracle.com/es-ww/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm).
We settled on Netlify because it works very nicely, can scale to a fullblown app with CDN and content managment and
more imporantly [Netlify had Python 3.10]({{< ref "posts/netlify.md" >}})  compatible images at the time.

This is a static HTML with some Javascript and a Pelican template. So, there is only one contributor, no
merging, PRs and other differences with a production distributed microservice or hybrid service
architecture. Netlify has a nice build image for Python and static sites. This is not a static site generator
like Jekyll or Hugo, but rather a microblog.

Again, the above is not true. This is a Go Hugo static microblog which is published via Github Actions to a Github Pages.

The conversion was done with the help of Grok to provide some handy Python scripts.


### The Future {{< emoji crystal_ball >}}

I plan to add more content, add Github emojis back in using the proper Go templating.

~~I also plan to migrate to Hugo or another
static site generator.~~

Actually, this migration is done. This is now a Go Hugo site. Did I mention that?

### The Links {{< emoji link >}}

Here are some useful links:

* [Github](https://github.com/edamsoft-sre/software-engineer-blog)
* [LinkedIn](https://www.linkedin.com/in/eric-arellano-martinez/)
* [X](https://x.com/)


---
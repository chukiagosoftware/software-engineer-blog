---
title: "Intro" 
date: 2026-02-01
draft: false
---


## About Me {{< emoji mage_man >}}

Officially a Computer and Electrical Engineer, B.Sc. (nice!). I've mostly been a Network and Security, then Devops,
Site Reliability and more recently an AI, AWS/GCP and Go engineer. This is my blog, not really a portfolio and not too serious. 

Just some notes and musings on my journey as a software engineer. {{< emoji sun >}}

My passion is building fun applications, staying at the cutting edge of Cloud, Kubernetes, 
OpenTelemetry and AI of course. {{< emoji horse >}} 

{{< emoji engineering >}}


I've built and helped to scale and observe a variety of SaaS, Webex Videoconferencing, Jitsi videoconference,
SIP/WebRTC VoIP and IP Telephony Contact Center, Big Data parallel processing, Machine Learning neural network models, 
Large Language Generative Pretrained Transformer Models, Confluent Kafka event streaming, Postgre/MySQL/Redshift/Auror database
modeling, data ingestion, processing, LLM model finetuning.

Recently I've worked on vectorizing data with Go for RAG, modelling input data with AWS Glue, Athena and Redshift
implementing performant AI-based systems in AWS Kubernetes with
OpenTelemetry, Prometheus and/or Datadog for real time metrics and analytics.

My most recent CI/CD and programming language are Github Actions and Go. I've also worked heavily with Jenkins (I know), ArgoCD, Google Cloudbuild,
Python, Javascript, Ansible but, I'm not going to talk about those.

My speciality du jour is building, deploying apps written in Go and Python and handling AWS, Kubernetes, OpenTelemetry or Prometheus metrics 
for an end to end system such as for Generative AI (Large Language Models) applications.

I'm somewhat of a nerd and I am {{< emoji nerd_face >}} really good with Terraform. Like stupid good.

While I am solely responsible for all this crap- I mean, content- I do have to thank Grok and Claude for helping make the
conversion fast and mostly painless. Also, thanks to my friends and family for supporting me and my wife.

<!--more-->


### The Icons {{< emoji shipit >}}

~~The site runs on Python 3.10 with the Pelican 4.8.0 microblog software and my custom Python Markdown 3.4.1 extension
for the Github Emojis. These are just the publicly available emojis which you can see around the pages. I find that
there are some really, really cool ones and thus without further ado.~~

Actually, this is no longer true. This is now a Go Hugo site.

Hugo is really cool, has Go templating engine, emojis and others are
a breeze to add using shortcodes and will allow me to delve more into the Go ecosystem as I develop my Hotel Recommendations
Rag application. 



### The Platform {{< emoji godmode >}}

The blog code is deployed based on Git ops. 

~~In other words, the Python code which generates html, is pushed to a main branch
integrated with Ci/Cd service [Netlify](https://www.netlify.com)~~

~~I use Jetbrains Pycharm, so this is done either by typing *git push* in the Terminal or Cmd-K in the IDE window. I
highly recommend it.~~

Other options I considered for deployment over the years were Google App Engine, [Render](https://www.render.com) and a VM on Digital
Ocean or a [free Oracle VM](https://docs.oracle.com/es-ww/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm).

After running off a Google Bucket with local-only Pelican html generation, I settled on Netlify a few years back because 
it works very nicely, can scale to a full-blown app with CDN and content managment and
more importantly [Netlify had Python 3.10]({{< ref "posts/netlify.md" >}})  compatible images at the time.

~~This is a static HTML with some Javascript and a Pelican template. So, there is only one contributor, no
merging, PRs and other differences with a production distributed microservice or hybrid service
architecture. Netlify has a nice build image for Python and static sites.~~ 


Again, the above is no longer true. This is now a Hugo static microblog which is published via Github Actions to Github Pages. 

The conversion from Python (Pelican) to Go (Hugo) was done with the help of Grok to provide some handy Python scripts. Github Pages
is now very mature and Github Actions allows me to build the suite upon pushes to Main, then deploy off a special branch all without leaving Github.


### The Future {{< emoji crystal_ball >}}

I suppose I plan to add more content, enable searching and make the text and appearance more professional looking. 

Also, once completed we will have a widget with my Hotel Recommendation assistant.

~~I also plan to migrate to Hugo or another
static site generator.~~

As noted a bunch of times (sorry) this migration is now done. This is now a Go Hugo site. Did I mention that?

### The Links {{< emoji link >}}

Here are some useful links:

* [My Data Engineering Professional Cert](https://www.coursera.org/account/accomplishments/professional-cert/CL02KD2ZFW8A)
* [My Cisco Gen AI Blue Belt](https://www.credly.com/badges/91dbaf61-46b0-4d9c-9703-0ed47259000a/public_url)
* [My Github](https://github.com/edamsoft-sre)
* [My LinkedIn](https://www.linkedin.com/in/eric-arellano-martinez)
* [News](https://x.com/)
* [Kubernetes](https://www.k8s.io)
* [Go](https://goloang.org)
* [Terraform](https://registry.terraform.io)


---
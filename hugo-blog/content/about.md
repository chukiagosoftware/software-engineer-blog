---
title: "Intro" 
date: 2026-02-01
draft: false
---


## About Me {{< emoji mage_man >}}

Hey! A while ago I received my degree as a Computer and Electrical Engineer, B.Sc. (2005, U. Texas at Austin). 

Throughout my career I've learned many aspects of modern Software Engineering, including Development, Network Security, Enterprise Autonomics, Web SaaS,
Contact Centers, Go, Python, Javascript, Java, and Bash shell scripting. I've held roles across small, medium-sized, and large companies.

In the last 7 years my work has focused on AI and Machine Learning operations and product development, Devops, Site Reliability, and Clouds.

I am very knowledgeable in helping to scale new products and services using AWS/GCP, Kubernetes, Terraform, Ci/Cd, and 
proper telemetry or observability. I can also help to certify for SOC2, FedRAMP and generally maintain security best practices
for cloud infrastructure, data, and applications.

This is my personal blog, not really a portfolio and not too serious. Just some notes and musings on my journey as a software engineer. {{< emoji bubble_tea >}}

My passion is building fun applications, staying at the cutting edge of Go, Cloud, Kubernetes, 
OpenTelemetry, and AI of course. {{< emoji bearded_person >}} 


{{< emoji computer >}}


I've built and helped to scale and observe a variety of services providing from Web SaaS, Webex Video, Jitsi video, IP Telephony Contact Center,
Big Data processing, Machine Learning with NN and LLM Gen AI models.Confluent Kafka event streaming, Postgres/MySQL/Redshift/Aurora database

I am experienced at building, integrating, and scaling Confluent Kafka, Postgres/RDS, AWS SQS, Redis and several other
message queues, databases en data engineering tools such as AWS Athena and Redshift or Google BigQuery.



I am about equally useful with AWS, EKS, Sagemaker and GCP, GKE, Vertex AI, for example.  {{< emoji biohazard }}

Recently I've worked on gathering inputs from HTML, PDF, and SQL data with Go and generating vectorized embeddings to implement
Retrieval-Augmented Generation (RAG) on top of OpenAI, Anthropic, Google, and Open Source models.  {{< emoji bookmark }}

{{< emoji compass }}

I hold a DeepLearning.AI Professional Data Engineer certification from 2024, multiple Cisco networking certs in the 2000's and 2010's,
and enjoy keeping up with new programming languages and frameworks, the latest being Go.

{{< emoji construction_worker_man }}

I'm definitely a nerd. {{< emoji nerd_face >}} and am real good using Terraform from ground up to deploying pipelines with 
Github Actions, or Terraform Cloud.

I have worked extensively in building telemetry with Go and Python and ML teams with end to end observability and
distributed tracing into Datadog or Tempo using OpenTelemetry, Prometheus, or Datadog native metrics.

While I am solely responsible for all this content- I do have to thank Grok and Claude for helping make the
most recent Python-to-Go conversion fast and painless. Also, thanks to my friends and family for supporting me and my wife.

<!--more-->


### The Icons {{< emoji shipit >}}

~~The site runs on Python 3.10 with the Pelican 4.8.0 microblog software and my custom Python Markdown 3.4.1 extension
for the Github Emojis. These are just the publicly available emojis which you can see around the pages. I find that
there are some really, really cool ones and thus without further ado.~~

Actually, this is no longer true. This is now a Go Hugo site.  A moment of silence for Python {{< emoji snake }}
and Pelican, which served me well for years.


{{< emoji swimmer }}

Hugo is really cool, has a built-in Go templating engine, allows emojis and other HTML features easily using shortcodes.  I'm looking forward to 
adding on to the site with Go's ecosystem as I develop my Hotel Recommendations RAG/LLM application. 

I resisted updating this blog- and learning more Go-for several years mainly because I loved Python and the Pelican microblogging
framework worked out. But I've since found that Go is my new favorite language and am thrilled with the power and simplicity of
the standard library and tools. Python Async and FastAPI can't really hold a candle to Go routines and net/http (sorry!).

### The Platform {{< emoji godmode >}}

The blog HTML and Javascript/CSS code is deployed based on simple Git ops with Github Actions. 

~~In other words, the Python code which generates html, is pushed to a main branch
integrated with Ci/Cd service [Netlify](https://www.netlify.com)~~

~~I use Jetbrains Pycharm, so this is done either by typing *git push* in the Terminal or Cmd-K in the IDE window. I
highly recommend it.~~


{{< emoji thinking }}
Other options I considered for deployment over the years were Google App Engine, [Render](https://www.render.com) and a VM on Digital
Ocean or a [free Oracle VM](https://docs.oracle.com/es-ww/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm).

After running off a Google Bucket with local-only Pelican html generation, I settled on Netlify a few years back because 
it works very nicely, can scale to a full-blown app with CDN and content management, and
more importantly [Netlify had Python 3.10]({{< ref "posts/netlify.md" >}}) compatible images at the time.

~~This is a static HTML with some Javascript and a Pelican template. So, there is only one contributor, no
merging, PRs, and other differences with a production distributed microservice or hybrid service
architecture. Netlify has a nice build image for Python and static sites.~~ 


The above is no longer true (again). This is now a Hugo static microblog, which is published via Github Actions to Github Pages. 

The conversion from Python (Pelican) to Go (Hugo) was done with the help of Grok to provide some handy Python scripts. Github Pages
is now very mature and Github Actions allows me to build the suite upon pushes to Main, then deploy off a special branch all without leaving Github.


### The Future {{< emoji crystal_ball >}}

Someday, this blog may undergo its next conversion using Rust, unless another cooler language comes along first.

Also, once work on [Alpaca](https://github.com/chukiagosoftware/alpaca) is complete, we will have a widget with my Hotel Recommendation assistant, or some nice tables
and graphs with Hotel Review data, or both.

{{< emoji congratulations }}

Thanks for reading! 


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
* [Python](https://www.python.org)



---
---
title: "Intro" 
date: 2026-02-01
draft: false
---


### About Me {{< emoji mage_man >}}

Hey! A while ago I received my degree as a Computer and Electrical Engineer, B.Sc. (2005, U. Texas at Austin). 

Throughout my career I've learned many aspects of modern Software Engineering, including AI, Software Development, Network Security, Enterprise Autonomics, SaaS, and Contact Centers. Wherein I've coded, deployed, and operated services written in Go, Python, JavaScript, Java, as well as Bash shell script. 

I've held roles across small, medium-sized, and large companies.

In the last 7 years my work focused on AI and Machine Learning operations and product development leveraging Devops, Site Reliability, and Clouds.

#### Startups {{< emoji dna >}}
Regarding startups, I'm very knowledgeable in helping to scale new products and services using AWS/GCP/Azure, Kubernetes, Terraform, ArgoCD, Jenkins, and implementing proper telemetry for metrics, traces, and logs.

I can help to certify software and platform for SOC2 and FedRAMP and maintain security best practices for cloud infrastructure and data.

#### {{< emoji bearded_person >}} Not production! {{< emoji bubble_tea >}}
Although, this is just a personal blog mostly containing random notes and musings on my journey as a software engineer. 

My passion is building fun applications, and currently staying at the cutting edge of Go, Cloud, Kubernetes, OpenTelemetry, and Machine Learning.



#### Experience {{< emoji computer >}}
I've built and helped to scale and observe a variety of services providing from Web SaaS, Webex Video, Jitsi video, IP Telephony Contact Center, Big Data processing, Machine Learning with NN, and LLM Gen AI models.

As part of this I helped to deploy, integrate, and operate Confluent Kafka, Postgres on RDS, AWS SQS, Redis on Elastic Cache, ActiveMQ/RabbitMQ, MySQL, Microsoft SQL Server in addition to cloud data engineering tools such as AWS Athena and Redshift or Google BigQuery and Cloud SQL.


#### Clouds {{< emoji biohazard >}}
I am equally useful with AWS running EKS and Sagemaker and GCP running GKE and Vertex AI.  For example, I've deployed both extensively with Terraform, Pulumi, Ansible, Python, and workflow/automation tools such as ArgoCD and Stackstorm.

In the realm of Kubernetes I have expert-level experience with Helm, Kustomize, controllers, Prometheus, Grafana, Load Balancing Controllers such as AWS LB, Nginx, and application gateway layers from AWS, Google, and Istio.

As far as building AWS or GCP cloud infrastructure, I love using Terraform and Pulumi or Ansible and Stackstorm for automation.


#### Projects {{< emoji construction_worker_man >}}
Recently I helped to code and deploy a Go service with API endpoints for gathering document inputs as HTML, PDF, and SQL data and processing them with Go for Weaviate and Google AI Search. This allowed the data to be stored as embeddings in vector tables and correspondingly allowed vector similarity searches to build a set of documents as input for a final LLM completion.

Furthermore, I've helped to deploy this service on Kubernetes as part of a complete Retrieval-Augmented Generation (RAG) system on top of OpenAI GPT 3/4, Anthropic Claude, Google Gemini, and other LLM and NN models for prompt completion as well as question classification, security guardrails and policy enforcement.


#### Other Skills {{< emoji brain >}}
As of November 2024, I hold a DeepLearning.AI Professional Data Engineer certification covering Python, Jupyter and production data analysis, design, schema transformation, and other aspects of ETL and ELT data pipelines.

In the past, I held a Cisco CCNA networking certification, and SIP Schools SSCA and SSCVVP VoIP certifications.

I always enjoy keeping up with new programming languages and frameworks, the latest being Go and some dabbling in Rust.

Yes, I'm most definitely a nerd {{< emoji nerd_face >}}!!


<!--more-->


### This microblog {{< emoji swimmer >}}

It's written in Go Hugo. Which is a really cool static site generator. It includes a powerful Go templating engine and allows emojis and other HTML features easily using shortcodes. I'm looking forward to adding on to the site with Go's ecosystem as I develop my Hotel Recommendations RAG/LLM application. 

Suffice to say that Go is my new favorite language. Especially am thrilled with the power and simplicity of the standard library and tools. Python Async and FastAPI/AIOHttp can't really hold a candle to Go routines and net/http (sorry!).


#### The Icons {{< emoji shipit >}}

~~The site runs on Python 3.10 with the Pelican 4.8.0 microblog software and my custom Python Markdown 3.4.1 extension
for the Github Emojis. These are just the publicly available emojis which you can see around the pages. I find that
there are some really, really cool ones and thus without further ado.~~

Actually, the above is no longer true. A moment of silence for Python {{< emoji snake >}} and Pelican, which served me well for years, and my custom Markdown extension for Github Emojis which is superseded by Hugo's built-in support for shortcodes.


#### The Platform {{< emoji godmode >}}

The blog HTML and JavaScript/CSS code is deployed based on simple GitOps with GitHub Actions. The HTML is stored in a separate branch, and each push to the main branch triggers a build and deployment to GitHub Pages. DNS is handled by another provider with CNAM records, nothing fancy.

#### Alternatives {{< emoji thinking >}}
Other options I had tested for deployment over the years were Google App Engine, [Render](https://www.render.com) and a VM on Digital Ocean or a [free Oracle VM](https://docs.oracle.com/es-ww/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm).

After running off a Google Bucket with local-only Pelican html generation, I settled on Netlify a few years back because it worked very nicely, can scale to a full-blown app with CDN and content management, and more importantly [Netlify had Python 3.10]({{< ref "posts/netlify.md" >}}) compatible images at the time.

The conversion from Python (Pelican) to Go (Hugo) was done with the help of Grok to provide some handy Python scripts. GitHub Pages is now very mature, and Github Actions allows me to build the suite upon pushes to Main, then deploy off a special branch all without leaving GitHub.


#### The Future {{< emoji crystal_ball >}}

Someday, this blog may undergo its next conversion using Rust, unless another cooler language or Go framework comes along first.

Also, once my work on [Alpaca](https://github.com/chukiagosoftware/alpaca) is complete, we will have a widget with my Hotel Recommendation assistant and maybe even some nice tables with Hotel Review data analysis.


##### Thanks for reading! {{< emoji dollar >}}


#### Some Links {{< emoji link >}}

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
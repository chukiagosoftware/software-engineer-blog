Title: The Stacks
URL:
save_as: index.html



:sunrise:  

## Welcome :trollface: 

This is my software engineering microblog focusing on Infrastructure as Code, DevOps and Site Reliability 
Engineering (SRE). I am a Computer and Electrical Engineer (B.Sc. University of Texas, 2005), Cisco Network and VoIP 
Expert, Staff System Reliability Engineer and DevOps / Kubernetes / Cloud practitioner with 18 years of experience.

Here you will find some neat how-tos and how-nots on Terraform, Kubernetes, Python, FastAPI, AsyncIO and 
system automation.

### The Icons :shipit:

We are running on Python 3.10 with the Pelican 4.8.0 microblogging framework, and our custom Python Markdown 3.4.1 
extension for the Github Emojis. 

While I've done a lot of HTML/Jquery/CSS work in the past, this is about the crux of my UI skills today. I do love 
[good theater](https://hamiltonmusical.com/) but am not much of a frontend guru. My deal is the backend, lol.



### The Platform :feelsgood:

This site is deployed based on Git-ops. The Python code is pushed to a main branch integrated with [Netlify](https://www.netlify.com)
I use Jetbrains Pycharm, so this is done either by typing *git push* or Cmd-K. I highly recommend it. 

Other options considered for deployment were Google App Engine, [Render](https://www.render.com) and a VM on Digital 
Ocean or a [free Oracle VM](https://docs.oracle.com/es-ww/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm). 
We settled on Netlify because it works very nicely, can scale to a full blown app with CDN and content managment and 
more imporantly [Netlify had Python 3.10]({filename}../netlify.md)  compatible images at the time.



## Infrastructure as Code :bridge_at_night:

IaC is a bridge between fear, uncertainty, doubt (FUD) and paradise. It can be pretty fun to work on 
IaC and get away from all that FUD.

Plus, Infrastructure as Code (whatever that means) is a vital component of deploying successful highly performant 
data intensive distributed applications. To be serious for half a moment, we can use IaC to meet stringent 
timelines and the highest standards of quality and also to have a whopping good time.

I have worked on the following Stacks, and I use the term loosely in this sentence, because it was a somewhat random 
though in retrospect very rewarding software path. 

In the beginning was the Internet.  We had Cisco routers and switches and Apache2 server racks connected with 
FastEthernet, then GigabitEthernet. Servers had power supplies and NICs and HPE ILO. And manual internet routes.

Then we learned to abstract and deployed OVMs on VMware ESXi and vSphere integrated with Network Load Balancers and App 
Firewalls. 


:cloud:

### And then, we beheld the Cloud


:umbrella: 

The Cloud was good for a while, but then it became too much. 

* Multiple clouds. 
* Unclear and changing APIs
* Climbing cloud costs. 
* Outages
* Growing Customer Acquisition Cost.
* Team multiplication - DevOps, delivery, qa, sre, infrastructure, platform, support...


:chart_with_upwards_trend:

Enter IaC.

:moneybag: :money_with_wings: :dollar:


####  My FIFO Stack :tanabata_tree:

* Linux Apache MySQL PHP (**LAMP**)
* Ruby on Rails
* Cisco Router, Communications Manager, Unified Contact Center
* OpenSIPS, Freeswitch (Voice Over IP)
* Jquery/JqueryUI
* Java Tomcat, Spring Boot
* Python FastAPI
* Debian/Ubuntu
* Redhat/Fedora/CentOS
* Docker/BuildKit
* Confluent Kafka
* ActiveMQ/RabbitMQ
* Postgres, Microsoft SQL
* Ansible, Jenkins, Python, Kubernetes
* AWS, GCP, Azure
* Terraform Cloud




##### IaC Glossary :fu:


If any of those sound new, check out the [opinionated IaC Glossary]({filename}../sre_devops_glossary.md) 
(si lees español, si no, jódete)


### SRE Toolkit

* [Terraform](#terraform)
* [Ansible](#ansible) 
* [Nomad](#nomad)
* [Kubernetes](#kubernetes)
* [Python](#python) 

---

#### Python Code Snippets :snake:
<a name="python"a></a>

Python is really versatile and has our back even when we don't know it such as with Ansible, and most cloud tools 
including **gcloud** and **az** CLI. Lately Python has become hot and apps that a few years ago would have been 
built in Java and then Go are now using AsyncIO and ASGI based libraries like FastAPI and Uvicorn to rival execution 
times and provide a smoother bridge to the Data Science Python ecosystem.

I've recently designed, written and helped to scale and monitor FastAPI and AioHTTP based Python microservices 
including linting, package management, build, deploy and observability with industry standard Telemetry, Tracing, 
APM with both open source and proprietary systems. In addition, I help to build backend automation and CLI tooliong 
for Ops and Support teams as well as build platforms and sandboxes for Engineering teams.


#### Faster small file downloads with aiohttp :potable_water:

[aiohttp]({filename}../async_requests.md) 

#### Github emoji extension :necktie:

This [pelican_github_emojis]({filename}../pelican_github_emojis.md) is a simple [Python Markdown extension]
(https://github.com/edamsoft-sre/python_markdown_github_emoji_extension) which 
allows one to add Github Emojis and make things more formal [Pelican](https://docs.getpelican.com)! 


#### Twitter AsyncIO Library :signal_strength:

[A twitter](https://github.com/edamsoft-sre/twitter-async-python) httpx and [Pydantic](http://www.google.com?q=pydantic) 
library for use with FastAPI. Provides GetMutualFollowers, GetTweets, GetLists.

#### httpx.AsyncClient workers with download AsyncIO Queue :children_crossing:

[httx wordpress](https://gist.github.com/edamsoft-sre/ee55e865f5f4a0615149b93da994ba46)


### Terraform :rocket:
<a name="terraform"></a>

I have designed and architected secure, scaleable cloud infrastructure on Google Cloud Platform, Amazon Web Services, 
Microsoft Azure and Oracle Cloud using Terraform. The TFE provider even allows meta-Terraform Cloud setup.

Terraform can also be used in addition to Infra for monitoring, alerting and application performance with Datadog, 
Prometheus, Grafana, ElasticSearch, Logstash, Kibana, Splunk

Don't forget Terraform Cloud and Terraform Enterprise automation, policy and audit validation and cost management

Terraform grows on you, I promise

---

###  Kubernetes :ship:    
<a name="kubernetes"></a>

Learning Kubernetes? Besides the excellent [K8S docs](https://kubernetes.io) I would recommend these Udemy courses:

* [Certified Kubernetes Administrator](https://www.udemy.com/topic/certified-kubernetes-administrator-cka/)
* [Developer](https://www.udemy.com/topic/certified-kubernetes-application-developer-ckad/) 

But the best way to learn Kubernetes is by deploying a cluster. If you will be using GCP, you can use my GKE 
Terraform modules to deploy a fully secure Private GKE cluster. This is important for SOC2 and other security 
audits that are industry-standards for most global apps.

[https://github.com/edamsoft-sre/DevOpsDeNoche/tree/main/3_infraestructura_escalable/kubernetes](https://github.com/edamsoft-sre/DevOpsDeNoche/tree/main/3_infraestructura_escalable/kubernetes)

---
### Nomad  :speedboat: 
<a name="nomad"></a>

Hashicorp Nomad is a great alternative to Kubernetes for self-contained projects. It is also based on YAML manifests 
but is implemented as a single binary which runs on almost any GNU/Linux system and schedules workloads directly onto 
Nomad worker nodes with nearly the same orchestration abilities. 

Hashicorp Consul provides service mesh and high availability features and tightly integrates well with Nomad. While 
the Nomad ecosystem is smaller, it is a readily viable option to scale down compute and memory costs and unecessary 
YAML / Helm bloat.

---

### DevOps :factory:

Generally while working in the cloud we will want to implement Agile strategies and the DevOps philosophy of treating 
Operations as software development. This does mean using a stack such as Git, ArgoCD, Observability tools, Docker and 
Kubernetes but it's much more than this. 

DevOps means truly operating, developing and scaling applications using a software engineering first approach while 
integrating with teams such as SRE, QA, Platform, Product, Sales, Customer Support and Stakeholders at all levels.

As such, there is much more we could write about DevOps.


---

#### Ansible :airplane:
<a name="ansible"></a>

Ansible is the best tool for automating servers and cloud resources. It's based on Python, so 
you can make your own modules or patch existing ones very easily.

In traditional light client mode, Ansible is running Python requests or a built-in version of the paramiko-ssh client. 
And then it is running Python modules and actions on the remote hosts. There are also Ansible collections for common 
Kubernetes and other systems.

The Ansible standard collection provides a one-to-one mapping for 90% of typical operational commands and remediation 
steps  from standard GNU/Linux. The syntax is YAML, but somehow beautiful anyway. 


---

#### SaaS :roller_coaster:

Here are some clouds and some things that we never talk about

* Amazon Web Services
* Google Cloud Platform 
* Microsoft Azure
* Netlify
* Agile, Jira, Confluence, Slack
* Pagerduty, Opsgenie


Stay tuned! 

:beach_umbrella:

Peace



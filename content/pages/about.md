Title: The Stacks
URL:
save_as: index.html



:sunrise:  

## Welcome :tiger2:

This is my software engineering microblog focusing on Infrastructure as Code, DevOps and Site Reliability 
Engineering (SRE). I am a Computer and Electrical Engineer (B.Sc. University of Texas, 2005), Cisco Network and VoIP 
veteran, Staff System Reliability Engineer, DevOps, Kubernetes, Cloud practitioner with 18 years of experience overall.

Here you will find some neat how-tos and how-nots on Terraform, Kubernetes, Python, FastAPI, AsyncIO and 
system automation. This is more of a notes for me to come back to type thing, so without further ado.

### The Icons :shipit:

We are running on Python 3.10 with the Pelican 4.8.0 microblogging framework, and our custom Python Markdown 3.4.1 
extension for the Github Emojis. 

While I've done a lot of HTML/Jquery/CSS work in the past (pre-2010) this is about the crux of my UI skills today. I do 
love [good theater](https://hamiltonmusical.com/) but am not much of a frontend guru. My home is the backend, lol.

I wrote and collaborated on a number of LAMP and Ruby on Rails back-office apps in the early 2010's. From 2015 on I 
picked up Python and have not looked back. 

Although I am currently learning [Intermediate Go at Platzi](https://platzi.com/cursos/golang-intermedio/) 
and may be writing more about that soon.



### The Platform :feelsgood:

This site is deployed based on Git-ops. The Python code is pushed to a main branch integrated with [Netlify](https://www.netlify.com)
I use Jetbrains Pycharm, so this is done either by typing *git push* or Cmd-K. I highly recommend it. 

Other options considered for deployment were Google App Engine, [Render](https://www.render.com) and a VM on Digital 
Ocean or a [free Oracle VM](https://docs.oracle.com/es-ww/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm). 
We settled on Netlify because it works very nicely, can scale to a full blown app with CDN and content managment and 
more imporantly [Netlify had Python 3.10]({filename}../netlify.md)  compatible images at the time.

This is a static HTML site with some Javascript and a Pelican template. So, there is only one contributor, no 
merging issues nor PRs and many other differences with a production distributed microservice or hybrid service 
oriented application. Nonetheless the core principle is the same and using Git actually makes publishing this blog a 
breeze.


## Infrastructure as Code :bridge_at_night:

IaC is a bridge between fear, uncertainty, doubt (FUD) and paradise. It can be pretty fun to work on 
IaC and get away from all that FUD.

Infrastructure as Code is a vital component of deploying successful highly performant data intensive distributed 
applications. To be serious for half a moment, we can use IaC to meet stringent timelines and the highest standards 
of quality and also to have a whopping good time.

In the beginning there was the Internet. In the server room we had Cisco routers and switches and Apache2 racks 
connected with FastEthernet, then GigabitEthernet. Servers had power supplies and NICs and HPE ILO.

:crystal_ball:


Then we learned to abstract most of this into a Hypervisor and Virtual Machine images. So we deployed OVMs on VMware 
ESXi and vSphere integrated with Network Load Balancers and App Firewalls. And to manage all this madness, we needed 
Configuration Management. This was the era of Ansible, Puppet, Chef. Kubernetes was kinda there, but only Google was 
using it. 


And then, we beheld the Cloud

:cloud:


The Cloud was good for a while, but then it became a bit much. 

* Multiple clouds. :circus_tent:
* Unclear and changing APIs :trollface: 
* Climbing cloud costs :money_with_wings:
* Outages :shit:
* Growing Customer Acquisition Cost :moneybag:
* Team multiplication :family:
* Dependency chain vulnerabilites :fire:


:chart_with_downwards_trend:



---
### :muscle: Enter IaC :chart_with_upwards_trend:

Infra as code, as noted already, is the solution to these cloud management, scale, cost and visibility problems. 
This is part and parcel of SRE, although SRE also involves software architecture, requirements and capacity and 
operational frameworks.

:books:

>    If any of these sound new, check out the [opinionated IaC Glossary]({filename}../sre_devops_glossary.md) (si 
>    lees español/ in Spanish)



### SRE Toolkit

IaC, automation and observability are some of the things that SRE generally oversee and drive on Agile teams

* [Terraform](#terraform)
* [Ansible](#ansible) 
* [Nomad](#nomad)
* [Kubernetes](#kubernetes)
* [Python](#python) 
* [LMAO](#lmao)

---

<a name="lmao"></a>
##### LMAO :telescope:

I've recently worked with FastAPI and AioHTTP based Python microservices from package management and image builds 
through deployment and instrumentation for LMAO (Logging, Metrics, Alerting, Observability) with Splunk, Datadog, 
Prometheus, Grafana, Google Stackdriver and Cloudwatch.

In the past I have worked on IPsoft's Amelia ML-based enterprise IT automation, observation, service and PaaS 
software with integrated alert handling automata or AI-powered remediation workflows scripted with Python and 
Javascript. These were able to respond to application metrics, logs and service indicators for any resources managed 
through Amelia.

As well as driving optimized On Call rotations, Incident Response planning, High Availability / Disaster Recovery 
planning and SOC2 compliance preparation, audit and stage 2 approval for multiple organizations with a focus on 
Observability.

I have been in the monitoring space before the cloud as well, since Nagios and Icinga through to the current SaaS 
offerings of Datadog, NewRelic, Splunk, AppDynamics and others. 

In the last few years I have successfully deployed global distributed monitoring for Java Spring Boot, Go, and Python 
Monoliths, Hybrid service oriented and Containerized Microservice application systems as well as SQL/NoSQL Databases,
Confluent Kafka, UI/UX monitoring and Real Time multimedia/contact center analytics.


#### Python Code Snippets :snake:
<a name="python"></a>

Python is really versatile and in SRE type projects you will find it under the hood in  Ansible, **gcloud** and 
**az** cli as well as in automation tools like [Stackstorm](http://www.stackstorm.com) or [Fabric](https://www.fabfile.org).

While it has been around since 1992, lately Python has become very popular thanks to AsyncIO and ASGI based libraries 
like FastAPI, AioHTTP, Gunicorn/Uvicorn which can rival compiled/JVM execution times and provide a smoother bridge 
to the Data Science Python ecosystem and ML engineers using Google Vertex and Conda.


#### Faster small file downloads with aiohttp :potable_water:

[aiohttp]({filename}../async_requests.md) 

#### Github emoji extension :necktie:

This [pelican_github_emojis]({filename}../pelican_github_emojis.md) is a simple [Python Markdown extension](https://github.com/edamsoft-sre/python_markdown_github_emoji_extension) which 
allows one to add Github Emojis and make things more formal [Pelican](https://docs.getpelican.com)! 


#### Twitter AsyncIO Library :signal_strength:

[A twitter](https://github.com/edamsoft-sre/twitter-async-python) httpx and [Pydantic](http://www.google.com?q=pydantic) 
library for use with FastAPI. Provides GetMutualFollowers, GetTweets, GetLists.

#### httpx.AsyncClient workers with download AsyncIO Queue :children_crossing:

[httx wordpress](https://gist.github.com/edamsoft-sre/ee55e865f5f4a0615149b93da994ba46)

<a name="terraform"></a>
### Terraform :rocket:

Architected secure, scalable cloud infrastructure on [Google Cloud Platform](https://github.com/edamsoft-sre/DevOpsDeNoche/tree/main/3_infraestructura_escalable/),
Amazon Web Services, Microsoft Azure and Oracle Cloud using Terraform.

Terraform grows on you, I promise. 

---
<a name="kubernetes"></a>
###  Kubernetes :ship:    


Learning Kubernetes? Besides the excellent [K8S docs](https://kubernetes.io) I would recommend these Udemy courses:

* [Certified Kubernetes Administrator](https://www.udemy.com/topic/certified-kubernetes-administrator-cka/)
* [Developer](https://www.udemy.com/topic/certified-kubernetes-application-developer-ckad/) 

But the best way to learn Kubernetes is by deploying a cluster. If you will be using GCP, you can use my GKE 
Terraform modules to deploy a fully secure Private GKE cluster. This is important for SOC2 and other security 
audits that are industry-standards for most global apps.

[DevOpsDeNoche](https://github.com/edamsoft-sre/DevOpsDeNoche/tree/main/3_infraestructura_escalable/kubernetes)

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



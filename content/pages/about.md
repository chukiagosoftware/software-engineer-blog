Title: The Stacks
URL:
save_as: index.html

### Welcome :sunrise:  

To this software engineering microblog focusing on Infrastructure as Code, DevOps and Site Reliability Engineering 
(SRE). Here you will find some neat how-tos and how-nots on Terraform, Kubernetes, Python FastAPI, AsyncIO and 
system automation. 

We are running on Python 3.10, Pelican 4.8.0 microblogging framework, and our custom Python Markdown 3.4.1 extension 
for the Github Emojis. Like cheese.

like  :cheese:

While I've done some HTML/Jquery/CSS work in the past, this is about the crux of my UI skills. I do love [good 
theater](https://hamiltonmusical.com/) but am not much of a UI or frontend engineer, huge surprise huh.

This site is deployed based on Git pushed to main branch using [Netlify](https://www.netlify.com). Highly  
recommended. Other options considered for deployment were Google App Engine, [Render](https://www.render.com) and 
some server on GCP or Digital Ocean or my old shared-webhost from the 90's. We settled on Netlify because it works very 
nicely out of the box, in theory we can run a full blown app with CDN and content managment and more imporantly 
Netlify had Python 3.10 compatible images at the time of writing. More on Netlify if you click on Categories.


### Infrastructure as Code :bridge_at_night:

IaC is a bridge between fear, uncertainty, doubt (FUD) and paradise. It can be pretty fun to work on 
IaC and get away from all that FUD.

Plus, Infrastructure as Code (whatever that means) is a vital component of deploying successful highly performant  
data intensive distributed applications. To be serious for half a moment, we can use IaC to meet stringent 
timelines and the highest standards of quality and also to have a whopping good time.

I have worked on the following Stacks, and I use the term loosely in this sentence, because it was a somewhat random 
though in retrospect very rewarding software path. 

In the beginning was the Internet.  We had Cisco routers and switches and Server racks connected with FastEthernet, 
then GigabitEthernet. Servers had power supplies and NICs and HPE ILO. Then VMware ESXi and vSphere, Load 
Balancers, App Firewalls were the rage. And then, The Cloud

:cloud:

The Cloud was good for a while, but then it became a huge stinking mess :umbrella: 

Enter IaC :chart_with_upwards_trend:

####  Eric's Stacks :tanabata_tree:

* Linux Apache MySQL PHP (**LAMP**)
* Ruby on Rails
* Python Flask
* Cisco Integrated Services Router
* Cisco Communications Manager
* Cisco IP Contact Center
* Jquery/JqueryUI
* Java Tomcat
* Java Spring Boot
* Python FastAPI
* Debian/Ubuntu
* Redhat/Fedora/CentOS
* Docker/BuildKit
* Confluent Kafka
* ActiveMQ/RabbitMQ
* Postgres, Microsoft SQL
* Ansible, Jenkins, Python, Kubernetes
* OpenSIPS, Freeswitch (Voice Over IP)
* AWS, GCP, Azure
* Terraform Cloud




##### IaC Glossary


If any of those were new to you, check out the [opinionated IaC Glossary]({filename}../sre_devops_glossary.md) (español)


### SRE Toolkit

* [Terraform](#terraform)
* [Ansible](#ansible) 
* [Nomad](#nomad)
* [Kubernetes](#kubernetes)
* [Python](#python) 

---

#### Python Code Snippets :snake:
<a name="python"a></a>


##### Faster downloads with aiohttp

[aiohttp]({filename}../async_requests.md) 

##### Github emoji extension

The [pelican_github_emojis]({filename}../pelican_github_emojis.md) is a simple [Python Markdown extension](https://github.com/edamsoft-sre/python_markdown_github_emoji_extension) which 
allows one to add Github Emojis and make things more formal [Pelican](https://docs.getpelican.com)! :necktie:


##### Twitter AsyncIO Library

[twitter](https://github.com/edamsoft-sre/twitter-async-python) httpx and [Pydantic](http://www.google.com?
q=pydantic) library for use with FastAPI. Provides GetMutualFollowers, GetTweets, GetLists.

##### AsyncClient httpx workers with download queue

[httx wordpress](https://gist.github.com/edamsoft-sre/ee55e865f5f4a0615149b93da994ba46)


### Terraform
<a name="terraform"></a>

I have designed and architected secure, scaleable cloud infrastructure on Google Cloud Platform, Amazon Web Services, 
Microsoft Azure and Oracle Cloud using Terraform. The TFE provider even allows meta-Terraform Cloud setup.

Terraform can also be used in addition to Infra for monitoring, alerting and application performance with Datadog, 
Prometheus, Grafana, ElasticSearch, Logstash, Kibana, Splunk

Don't forget Terraform Cloud and Terraform Enterprise automation, policy and audit validation and cost management

:rocket:

Terraform grows on you, I promise

---

###  Kubernetes  :steam_locomotive:    
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

### DevOps :construction:

Generally while working in the cloud we will want to implement Agile strategies and the DevOps philosophy of treating 
Operations as software development. This does mean using a stack such as Git, ArgoCD, Observability tools, Docker and 
Kubernetes but it's much more than this. 

DevOps means truly operating, developing and scaling applications using a software engineering first approach while 
integrating with teams such as SRE, QA, Platform, Product, Sales, Customer Support and Stakeholders at all levels.

As such, there is much more we could write about DevOps.


---

#### Ansible :alien:
<a name="ansible"></a>

Ansible is the best tool for automating servers and cloud resources. It's based on Python, so 
you can make your own modules or patch existing ones very easily.

In traditional client mode, Ansible is running Python requests or a built-in version of the paramiko-ssh client. And 
then it is running Python modules and actions on the remote hosts. There are also Ansible collections for common 
Clouds, Kubernetes and others. If you ask me, Ansible lost to Terraform on hype and UX which is important, but 
technically it's the superior tool and far simpler. Ah well, alas we may yet try [OpenTofu](https://opentofu.org) 
and be swayed. 

Ansible standard collection provides a one-to-one mapping for 90% of typical operational commands and remediation steps 
from standard GNU/Linux. The syntax is YAML, but somehow beautiful anyway. 


---

#### Clouds and Sasses

Here are some clouds and some things that we never talk about

* Amazon Web Services
* Google Cloud Platform 
* Microsofit Azure
* Netlify
* Agile, Jira, Confluence, Slack
* Pagerduty, Opsgenie


Stay tuned! Peace

:beach_umbrella:

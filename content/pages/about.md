Title: The Stacks
URL:
save_as: index.html

### Welcome :sunrise:  

This is a software engineering microblog focusing on Infrastructure as Code with Terraform, ArgoCD and Ansible, DevOps 
and Cloud Infrastructure how-tos and how-nots, Kubernetes wisdom, Python AsyncIO snippets for Ops automation and MLOps 
notes as I complete NLP and Generative AI LLM courses online.

We are running Python 3.10 and the incredible Pelican 4.8.0 microblogging framework, along with our very own Python 
Markdown 3.4.1 extension for Github Emojis. Because, well why not. :question:

Try it yourself! Just add a semi-colon before and after what should be a Github Emoji, like  :software:

This site is deployed using [Netlify](https://www.netlify.com) and all is well and good. Highly recommended. Other 
options considered for deployment were Google App Engine, due to the original blog inspiration for this 
microblog or [Render](https://www.render.com) another Heroku-like platform. We could also toss this HTML pretty much 
anywhere. Hmm, over-engineering, hmmmm.


### Infrastructure as Code :bridge_at_night:

IaC is sort of like the bridge between fear, uncertainty, doubt (FUD) and paradise. It can be pretty fun to work on 
IaC and get away from all that FUD.

Plus, Infrastructure as Code (whatever that means) is a vital component of deploying successful highly  performant 
data intensive distributed applications. Ok to be serious for half a moment, we use IaC to meet some stringent 
regulations and the highest standards of quality and also to have a whopping good time.

I have worked on Infrastructure as Code and DevOps with the following Stacks, and I use these terms loosely in 
this sentence, because this 
is clearly a very subjective and unlikely combination of things. Anyway, this is how I became the person you should 
hire next.

####  Stacks

* Ruby on Rails
* Jquery/JqueryUI
* Linux Apache MySQL PHP (**LAMP**)
* Java Spring Boot
* Java Tomcat
* Python Flask
* Python FastAPI
* Debian/Ubuntu
* Redhat/Fedora/CentOS
* Docker/BuildKit
* Confluent Kafka
* ActiveMQ/RabbitMQ
* Postgres, Microsoft SQL
* Cisco Communications Manager
* Cisco IP Contact Center
* Cisco Integrated Services Router
* OpenSIPS, Freeswitch (Voice Over IP)



##### IaC Glossary


If any of those were completelya new, check out the [opinionated IaC Glossary]({filename}../sre_devops_glossary.md) 
as long as you can read in Spanish it will be of some interest.


##### Somewhat ordered list of IaC Tools you can hire me to kick some buttola with

* [Terraform](#terraform)
* [Ansible](#ansible) 
* [Nomad](#nomad)
* [Kubernetes](#kubernetes)
* [Python](#python) 

---

### Python Stuff :snake:
<a name="python"a></a>


##### Faster downloads with aiohttp

[aiohttp]({filename}../async_requests.md) 

##### Github emoji extension for Python Markdown

[pelican_github_emojis]({filename}../pelican_github_emojis.md) is a simple [Python Markdown extension](https://github.com/edamsoft-sre/python_markdown_github_emoji_extension) which 
allows one to add Github Emojis and make things more formal [Pelican](https://docs.getpelican.com)! :necktie:


##### Twitter AsyncIO Library

[twitter](https://github.com/edamsoft-sre/twitter-async-python) httpx and [Pydantic](http://www.google.com?
q=pydantic) library for use with FastAPI. Provides GetMutualFollowers, GetTweets, GetLists.

##### AsyncClient httpx workers with download queue

[httx wordpress](https://gist.github.com/edamsoft-sre/ee55e865f5f4a0615149b93da994ba46)


### Terraform
<a name="terraform"></a>

Designed and architected secure, scaleable cloud infrastructure on Google Cloud Platform, Amazon Web Services, 
Microsoft Azure and Oracle Cloud.

Monitoring, alerting and application performance with Datadog, Prometheus, Grafana, ElasticSearch, Logstach, Kibana, 
Splunk

Terraform Cloud and Terraform Enterprise automation, policy and audit validation, cost management, CI/CD integration

:rocket:

---

###  Kubernetes  :steam_locomotive:    
<a name="kubernetes"></a>

Learning Kubernetes? Besides the excellent [K8S docs](https://kubernetes.io) I would recommend these Udemy courses:

* [Certified Kubernetes Administrator](https://www.udemy.com/topic/certified-kubernetes-administrator-cka/)
* [Developer](https://www.udemy.com/topic/certified-kubernetes-application-developer-ckad/) 

The best way to learn Kubernetes is by deploying a cluster. If you will be using GCP, you can use Terraform:

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
Kubernetes but it's much more tha this. 

DevOps means truly operating, developing and scaling applications using a software engineering first approach while 
integrating with teams such as SRE, QA, Platform, Product, Sales, Customer Support and Stakeholders at all levels.

As such, there is much more we could write about DevOps.


---

#### Ansible :alien:
<a name="ansible"></a>

Ansible is the best tool for automating servers and cloud resources. It's based on Python, so 
you can make your own modules or patch existing ones very easily.

In traditional client mode, Ansible is running Python requests or a built-in version of the paramiko-ssh client. And 
then it is running Python modules and actions on the remote hosts.

Ansible provides a one-to-one mapping for 90% of typical operational commands and remediation steps from standard 
GNU/Linux. The syntax is YAML, but somehow beautiful anyway.


---

#### Clouds and Sasses

* Amazon Web Services
* Google Cloud Platform 
* Microsofit Azure
* Netlify
* Agile, Jira, Confluence, Slack
* Pagerduty, Opsgenie


Stay tuned! Peace

:beach_umbrella:

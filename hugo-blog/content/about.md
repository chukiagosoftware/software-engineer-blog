---
title: "About"
draft: false
---



:sunrise:  



## A microblog for SRE, DevOps, MLOps :mage_man:

I am a Computer and Electrical Engineer by training that has worked as a Network and Security engineer in the 2000's, 
Web, DevOps and SRE in the 2010s and 2020s. Currently I am a Site Reliability Engineering Technical Lead for AWS 
infra and Generative AI-based distributed applications.

### The Icons :shipit:

The site runs on Python 3.10 with the Pelican 4.8.0 microblog software and my custom Python Markdown 3.4.1 extension 
for the Github Emojis. These are just the publicly available emojis which you can see around the pages. I find that 
there are some really, really cool ones and thus without further ado.


### The Platform :godmode:

The code is deployed based on Git ops. In other words the Python code which generates html, is pushed to a main branch 
integrated with Ci/Cd service [Netlify](https://www.netlify.com)

I use Jetbrains Pycharm, so this is done either by typing *git push* in the Terminal or Cmd-K in the IDE window. I 
highly recommend it. 

Other options considered for deployment were Google App Engine, [Render](https://www.render.com) and a VM on Digital 
Ocean or a [free Oracle VM](https://docs.oracle.com/es-ww/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm). 
We settled on Netlify because it works very nicely, can scale to a fullblown app with CDN and content managment and 
more imporantly [Netlify had Python 3.10]({{< ref "../netlify.md" >}})  compatible images at the time.

This is a static HTML with some Javascript and a Pelican template. So, there is only one contributor, no 
merging, PRs and other differences with a production distributed microservice or hybrid service 
oriented application. Nonetheless, the core principle is the same and using Git actually makes publishing this blog a 
breeze.


## Infrastructure as Code :suspect:

I would describe IaC as a bridge between fear, uncertainty, doubt (FUD) and paradise. It can be pretty fun to work on 
IaC and get away from all that FUD.

Infrastructure as Code is a vital component of deploying successful highly performant data intensive distributed 
applications. To be serious for half a moment, we can use IaC to meet stringent timelines and the highest standards 
of quality and also to have a whopping good time.


:classical_building:

In the beginning there was the Internet. In the server room we had Cisco routers and switches and Apache2 racks 
connected with FastEthernet, then GigabitEthernet. Servers had stuff like power supplies and NICs and HPE ILO. So 
basically everyone had their own cloud in some basement with a few engineers tending the machines. 


:neckbeard:



Then we began to use Virtual Machine images,  deploying OVMs on VMware ESXi and vSphere integrated with Network Load 
Balancers and App Firewalls. And to manage all this madness, we needed Configuration Management. This was the era of 
Ansible, Puppet, Chef. Until.. Kubernetes.


And thus, we beheld the Cloud

:cloud:


The Cloud was good for a while, but then it became a bit much. 

* Multiple clouds. :circus_tent:
* Unclear and changing APIs :man_firefighter: 
* Climbing cloud costs :money_with_wings:
* Outages :shit:
* Growing Customer Acquisition Cost :moneybag:
* Team multiplication :family:
* Dependency chain vulnerabilites :fire:



---
###  Enter IaC :chart_with_upwards_trend:

Infra as code, as noted already, is the solution to these cloud management, scale, cost and visibility problems. 
This is part and parcel of SRE, although SRE also involves software architecture, requirements and capacity and 
operational frameworks.

:mechanical_arm:

>    If any of these sound new, check out the [opinionated IaC Glossary]({{< ref "../sre_devops_glossary.md" >}}) si 
>    lees español (in Spanish)



## Infrastructure Engineering

Infrastructure as code (IaC), automation and observability are some of the things that SRE generally oversee and 
drive on Agile teams, working together with Data Engineers, ML engineers, Architects, Security, Customer Engagement and 
other 
stakeholders.

* [Terraform](#terraform)
* [Ansible](#ansible) 
* [Nomad](#nomad)
* [Kubernetes](#kubernetes)
* [Python](#python) 
* [LMAO](#lmao)

---

<a name="lmao"></a>
### LMAO :telescope:

I've helped design, operate, deploy and scale apps based on Java, Go, Ruby and Python including microservices, 
telecommunications, internal and customer facing SaaS platforms.

SRE work usually involves coordinating builds, scaling infra, connecting data and ML pipelines and setting up 
observability via 
LMAO services - Logging, Metrics, Alerting and Observability with Splunk, Datadog, Newrelic, Prometheus, Grafana, 
Cloudwatch, etc.

In the past I helped design and operate IPsoft's Amelia Machine Learning system for enterprise IT automation, 
observation and remediation.


---


### Python :snake:
<a name="python"></a>

Python is really versatile and in SRE type projects you will find it under the hood in  Ansible, **gcloud** and 
**az** cli as well as in automation tools like [Stackstorm](http://www.stackstorm.com) or [Fabric](https://www.fabfile.org) 
and directly in scripts and microservices.

While it has been around since 1992, lately Python has become very popular thanks to AsyncIO and ASGI based libraries 
like FastAPI, AioHTTP, Gunicorn/Uvicorn which can rival (or approach) compiled Go/JVM execution times and provide a 
smoother bridge to the Data Science Python ecosystem and ML engineers using Google Vertex, Jupyter Notebooks and Conda.

Again with LLMs and Python Langchain and Replit we see the same benefits from using Python for microservice 
prototyping and development.


* Read about fast downloads with [aiohttp]({{< ref "../async_requests.md" >}}) :potable_water:
* [Read about github_emoji]({{< ref "../pelican_github_emojis.md" >}}), a simple [Python Markdown extension](https://github.com/edamsoft-sre/python_markdown_github_emoji_extension) 
which allows one to add Github Emojis to [Pelican](https://docs.getpelican.com) microblogs :necktie:
* Twitter AsyncIO Library :signal_strength: [AsyncIO Twitter client](https://github.com/edamsoft-sre/twitter-async-python) with [httpx](https://www.python-httpx.org/)
and [Pydantic](http://www.google.com?q=pydantic). Provides GetMutualFollowers, GetTweets, GetLists methods. :x:
* httpx AsyncClient with configurable workers and AsyncIO Queue [httx wordpress](https://gist.github.com/edamsoft-sre/ee55e865f5f4a0615149b93da994ba46) :honeybee:

---


<a name="terraform"></a>
### Terraform :rocket:

Architected secure, scalable cloud infrastructure on [Google Cloud Platform](https://github.com/edamsoft-sre/DevOpsDeNoche/tree/main/3_infraestructura_escalable/),
Amazon Web Services, [Microsoft Azure](https://github.com/edamsoft-sre/jitsi-azure-terraform) and Oracle Cloud using Terraform.

Terraform grows on you, I promise. As your attorney, I would strongly advise you to use Terraform Cloud, Terragrunt, 
or one of the lesser known SaaS as this will allow you to focus on policy enforcement, scalability and observability 
feedback loops (tbd) 

---
<a name="kubernetes"></a>
###  Kubernetes :ship:    


Learning Kubernetes? Besides the excellent [K8S docs](https://kubernetes.io) I would recommend these Udemy courses:

* [Certified Kubernetes Administrator](https://www.udemy.com/topic/certified-kubernetes-administrator-cka/)
* [Developer](https://www.udemy.com/topic/certified-kubernetes-application-developer-ckad/) 

But the best way to learn Kubernetes is by deploying a cluster. If you will be using GCP, you can use my GKE 
Terraform modules to deploy a fully secure Private GKE cluster and demo microservices app. This is important for SOC2 
and other security standards or policies such as GDPR.

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



### DevOps :factory:

Generally while working in the cloud we will want to implement Agile strategies and the DevOps philosophy of treating 
Operations as software development. This does mean using a stack such as Git, ArgoCD, Observability tools, Docker and 
Kubernetes but it's much more than this. 

DevOps means truly operating, developing and scaling applications using a software engineering first approach while 
integrating with teams such as SRE, QA, Platform, Product, Sales, Customer Support and Stakeholders at all levels.

As such, there is much more we could write about DevOps.


---

### Ansible :airplane:
<a name="ansible"></a>

Ansible is the best tool for automating servers and cloud resources. It's based on Python, so 
you can make your own modules or patch existing ones very easily.

In traditional light client mode, Ansible is running Python requests or a built-in version of the paramiko-ssh client. 
And then it is running Python modules and actions on the remote hosts. There are also Ansible collections for common 
Kubernetes and other systems.

The Ansible standard collection provides a one-to-one mapping for 90% of typical operational commands and remediation 
steps  from standard GNU/Linux. The syntax is YAML, but somehow beautiful anyway. 


---

## MLOps :llama:

MLops involves setting up repeatable and reliable pipelines for scalable data management, production deployment and 
observability. Generally this involves using tools such as Amazon Sagemaker, Google Vertex or OpenAI and defining 
workflows 
to  streamline training, labelling, deployment, data integrity and low-latency 
inference. Machine learning models require to be monitored for performance, reliability and stability and introduce 
a whole new set of production, development and infrastructure related requirements which can be handled using and 
expanding the SRE toolset.


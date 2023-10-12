Title: The Stack

## :sunrise:  

This is a software engineering microblog focusing on Infrastructure as Code with Terraform and Ansible, DevOps and 
Cloud Infrastructure how-tos and how-nots, Python automation, async and MLOps.

Brought to you by Python 3.10 running the amazing Pelican 4.8.0 microblogging framework and custom Python Markdown 3.
4.1 with Github Emojis. Because, well why not.

I have deployed this using [Netlify](https://www.netlify.com) and all is well and good. Highly recommended but 
haven't tested out many of the web-app oriented features to be quite frank.

Other options considered for deployment were Google App Engine, the original inspiration for this microblog or Render
[Render](https://www.render.com) another Heroku-like platform. 

### Infrastructure as Code :bridge_at_night:

IaC is sort of like the bridge between fear, uncertainty, doubt or paradise. It can be pretty fun to work on IaC. I 
prefer the following tools, which isn't really a stack but hey.


##### Glossary

If any of these are new, check out the [opinionated Glossary]({filename}../sre_devops_glossary.md)


* [Terraform](#terraform)
* [Ansible](#ansible) 
* [Nomad](#nomad)
* [Kubernetes](#kubernetes)
* [Python](#python) 

---

#### Github Emojis

A simply [Python Markdown extension](https://github.com/edamsoft-sre/python_markdown_github_emoji_extension) 
to add Github Emojis [Pelican](https://docs.getpelican.com)! :necktie:


#### Python HTTPX Async

[Simply **httpx** based Python AsyncIO](https://github.com/edamsoft-sre/twitter-async-python) library to download files from Wordpress Webdav very quickly and reliably.



#### Terraform
<a name="terraform"></a>

Designed and architected secure, scaleable cloud infrastructure on Google Cloud Platform, Amazon Web Services, 
Microsoft Azure and Oracle Cloud.

Monitoring, alerting and application performance with Datadog, Prometheus, Grafana, ElasticSearch, Logstach, Kibana, 
Splunk

Terraform Cloud and Terraform Enterprise automation, policy and audit validation, cost management, CI/CD integration

:rocket:

---
####  Kubernetes  :steam_locomotive:    
<a name="kubernetes"></a>

Learning Kubernetes? Besides the excellent [K8S docs](https://kubernetes.io) I would recommend these Udemy courses:

* [Certified Kubernetes Administrator](https://www.udemy.com/topic/certified-kubernetes-administrator-cka/)
* [Developer](https://www.udemy.com/topic/certified-kubernetes-application-developer-ckad/) 

and then deploying an Elastic Kubernetes, Azure Kubernetes Service or Google Kubernetes Engine cluster with Terraform.

If you need real optimization, go with bare metal and run your own Kubernetes but this is not a typical use case.

For infrastructure or cluster-wide services, use Terraform **helm** or **kubernetes** providers.  For applications 
and middleware it is best to use a separate method such as ArgoCD, CloudDeploy, Github Actions or Jenkins.


---
### Nomad  :speedboat: 
<a name="nomad"></a>

Hashicorp Nomad is a really cool alternative to Kubernetes. It is also based on YAML manifests but is a single binary 
which 
runs on any Linux system almost and schedules workloads directly onto Nomad worker nodes with nearly the same 
orchestration 
abilities. Hashicorp Consul provides service mesh and high availability features and tightly integrates well with 
Nomad. While the Nomad ecosystem is smaller, it is a readily viable option to scale down compute and memory costs 
and unecessary YAML / Helm bloat.

---
### Python :snake:
<a name="python"></a>

Python is THE snake. But it's also an amazing programming language which you've never heard of until this blog. I've 
had some good fun with Python over the years, and hopefully I'll find time to write about it here.

* Contact Center automation
* Flask websites
* FastAPI, Httpx, [Aiohttp]({filename}../async_requests.md) 
* Pelican static site
* [Python Markdown Github Emoji extension]({filename}../pelican_github_emojis.md)

 ---
#### Cloud DevOps, CICD :umbrella:

Everything today is "in the cloud"  :cloud:  Cloud are fun. Basically from a user perspective, a cloud is just a 
REST API (or tons of them). You can GET, PUT (update), POST (create), and DELETE resources such as a Google 
Kubernetes Engine cluster, or a Confluent Kafka cluster, a bucket to store some data, or a Project to run things in 
securely. All of this hypothetically can be done using good old Python **requests**, or even **curl** but there are 
even easier ways to automate all of that.  
---

#### Ansible :alien:
<a name="ansible"></a>

Ansible is a really good best in the world tool for automating servers and Cloud resources. It's based on Python, so 
you can make your own modules or fix existing ones if you want very easily.

At the core, Ansible is running Python requests or a built-in version of it with paramiko-ssh client. And then it is 
running Python scripts and commands on the remote hosts. That's it.

But most things, from standard GNU/Linux system operations, to deploying cloud resources 
have a module already. The syntax is YAML, but somehow beautiful anyway.

---

#### Cloud

* Amazon Web Services
* Google Cloud Platform 
* Digital Ocean
* Azure
* Netlify
* Oracle Cloud
* Render
* Serverless
* Agile
* Silicon Valley

I used them and survived. Maybe I'll write about it some more here. Stay tuned!

:beach_umbrella:
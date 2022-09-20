Title: What is This 

## :sunrise:  

Welcome to my Python 3.10, Pelican 4.8.0, Python Markdown 3.4.1 powered blog, running on [Netlify](https://www.netlify.
com) Possibly soon to be running on Render once I migrate my main site over there first, [Render](https://www.render.
com) is a Heroku/Netlify like platform for running your code through automated Git Flows.

***

### Infrastructure as Code :bridge_at_night:

Look at that beautiful bridge! IaC is sort of like the bridge between an angry engineering team and a happy one. 
Cross that bridge!

More about Infra as Code in the [DevOps and SRE Glossary]({filename}../sre_devops_glossary.md) and below! 

* [Terraform](#terraform)
* [Ansible](#ansible) 
* [Nomad](#nomad)
* [Kubernetes](#kubernetes)
* [Python](#python) 

---

### Github Emojis
:necktie: I like Github Emojis a lot. So I wrote a [Python Markdown extension](https://github.
com/edam-software/python_markdown_github_emoji_extension) to easily add them to .md files such as 
those used on this [Pelican](https://docs.getpelican.com) blog! Go me!!  :rotating_light:



[Python Markdown](https://python-markdown.github.io/extensions/api/#inlineprocessors) internals are a pain in 
the ass, but adding extensions is relatively easy. I used the current 3.4.1 version with InlineProcessor and then went for a  :bike:  ride. 

If you realize these Github icons are kind of large by default, 64x64. To fix that, I used some magical CSS, see 
below!  Full details are [right here]({filename}../pelican_github_emojis.md).  This still leaves the question of 
handling spaces around emojis better, which we'll tackle at some point.


     .ghe_emoji img{
        padding: 0;
        margin: 0;
        border:0;
        font-size: 1.25em;
        mix-width: 1ch;
        max-width: 32px;
        line-height: 1;
        font-weight: 400;
        display: inline-block;
        vertical-align:-0.075em;
      }

***

### Terraform
<a name="terraform"></a>

I've been working with Terraform, Ansible and other IaC stuff for a while now. Not 10 years silly, Hashicorp only 
created Terraform about 7 years ago. I'm not such a guru or anything, but I've been around the block a few times. 

Terraform Cloud? No prob. Terraform Enterprise? Sure, if you need Auditing, Teams, dozens of workspaces and modules and 
such. 

Working on custom Terraform pipelines with your own setup?  :rocket:

---
###  Kubernetes  :steam_locomotive:    
<a name="kubernetes"></a>

Alas, Kubernetes is here to stay, so I went ahead and learned it.  I took the excellent Udemy courses [Certified 
Kubernetes Administrator](https://www.udemy.com/topic/certified-kubernetes-administrator-cka/) and [Developer](https://www.udemy.com/topic/certified-kubernetes-application-developer-ckad/), and then I spent a few years running 
production K8S clusters for medium, large and startup scale organizations. Always on a team, because you know, things 
move faster with   steam work.

I would love to work on custom K8S stuff like running optimal bare-metal (or bare-VM) clusters, writing some 
Controllers and refining my Go skills. Just saying.  

What about Helm? Helm is just a bunch of YAML. Sorry folks, nothing to see here, move on. Ok fine, kudos to those 
who write awesome Helm Charts and make installing things like Datadog Agents, Databases and Core services a snap.

---
### Nomad  :speedboat: 
<a name="nomad"></a>

Then, life threw me a curveball and I had to manage dozens of workloads (Java, Python, Go) running Nomad and Consul. 
I have to admit, Nomad beats the socks   off of Kubernetes. It's just a small binary, and pretty much does 
the same thing. You still get some crazy :ferris_wheel: YAML configs, Consul is a full-blown service mesh if you 
want it to be, and it can generate service-check basic and complex alerts for you too. So, there's that.

:circus_tent:  If you're new to them, learn more about these terms in our very own, admittedly random DevOps/SRE 
[glossary]({filename}../sre_devops_glossary.md) 

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

Ansible is a really cool tool for automating clouds. It's based on Python, so you can make your own modules or fix 
existing ones if you want. But most things, from standard GNU/Linux system operations, to deploying cloud resources 
have a module already. The syntax is YAML, but somehow beautiful anyway 

---

#### Cloud

* Amazon Web Services
* Google Cloud Platform 
* Digital Ocean
* Azure
* Netlify
* Oracle Cloud
* Render

I used them and survived. Maybe I'll write about it some more here. Stay tuned!

:beach_umbrella:
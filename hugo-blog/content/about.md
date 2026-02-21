---
title: "About"
draft: false
---



:sunrise:



## Another software engieering blog :mage_man:

Officially a Computer and Electrical Engineer, B.Sc. (nice!). I've also been a Network and Security, then Devops,
Site Reliability and more recently an AI, AWS and Go engineer. This is my blog, not a portfolio. Just some notes and
my most recent CI/CD and programming language which is Github Actions and Go. I've also used Jenkins, ArgoCD, Cloudbuild,
Python, Javascript but, I'm not going to talk about those.

My speciality is building, deploying and whooping ass with Go and Python software, AWS, Kubernetes, OpenTelemetry and Prometheus
end to end for Generative AI (Large Language Models) applications.

While I am solely responsible for all this crap- I mean, content- I do have to thank Grok and Claude for helping make the
conversion fast and mostly painless. Also, thanks to my friends and family for supporting me and my wife.

### The Icons :shipit:

The site runs on Python 3.10 with the Pelican 4.8.0 microblog software and my custom Python Markdown 3.4.1 extension
for the Github Emojis. These are just the publicly available emojis which you can see around the pages. I find that
there are some really, really cool ones and thus without further ado.

Actually, this is no longer true. This is now a Go Hugo site. Which is why you don't see any emojis yet.

At some point I will figure out what/how to get sweet Github Emojis or a better alternative going.

### The Platform :godmode:

The code is deployed based on Git ops. In other words the Python code which generates html, is pushed to a main branch
integrated with Ci/Cd service [Netlify](https://www.netlify.com)

I use Jetbrains Pycharm, so this is done either by typing *git push* in the Terminal or Cmd-K in the IDE window. I
highly recommend it.

Other options considered for deployment were Google App Engine, [Render](https://www.render.com) and a VM on Digital
Ocean or a [free Oracle VM](https://docs.oracle.com/es-ww/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm).
We settled on Netlify because it works very nicely, can scale to a fullblown app with CDN and content managment and
more imporantly [Netlify had Python 3.10]({{< ref "posts/netlify.md" >}})  compatible images at the time.

This is a static HTML with some Javascript and a Pelican template. So, there is only one contributor, no
merging, PRs and other differences with a production distributed microservice or hybrid service
architecture. Netlify has a nice build image for Python and static sites. This is not a static site generator
like Jekyll or Hugo, but rather a microblog.

### The Workflow :factory_worker:

The workflow is simple. I write content in Markdown, push it to Github and Netlify does the rest. For example, I
can push a new post to the blog, and it will be live within a minute. No need to restart servers, manage
infrastructure or worry about scaling. Netlify handles all of that.

The content is stored in the `content/` directory. The `pelicanconf.py` file contains the configuration for the
blog. The `publishconf.py` file is used for production builds. The `fabfile.py` is used for deployment.

Actually, this is no longer true. This is now a Go Hugo site. So, the content is in `hugo-blog/content/`, the config is `hugo-blog/hugo.toml`, and the deployment is via Github Actions.

### The Content :notebook:

The content is written in Markdown. I use a lot of code blocks, so I have syntax highlighting. I also use
tables, lists, and links. The content is stored in the `content/` directory.

For posts, I use the following format:

    Title: My Post
    Date: 2023-01-01
    Category: Python
    Tags: python, programming

    # My Post

    This is my post.

For pages, I use the same format but without the date and category.

Actually, this is no longer true. This is now a Go Hugo site. So, the content is in `hugo-blog/content/`, and the format is YAML front matter.

### The Theme :art:

The theme is custom. I started with the Pelican Blueidea theme and modified it. The theme is stored in the
`themes/` directory.

Actually, this is no longer true. This is now a Go Hugo site. So, the theme is PaperMod.

### The Plugins :gear:

I use the following plugins:

* [pelican-toc](https://github.com/edamsoft-sre/pelican-toc) - Table of Contents
* [python-markdown-github-emoji-extension](https://github.com/edamsoft-sre/python_markdown_github_emoji_extension) - Github Emojis

Actually, this is no longer true. This is no longer Pelican.

### The Search :mag:

The search is powered by Stork. I have a custom script that generates the search index. The search index is
stored in the `output/` directory.

Actually, this is no longer true. This is now a Go Hugo site. So, search is handled by the theme or a future addition.

### The Future :crystal_ball:

I plan to add more content, improve the theme, and add more features. I also plan to migrate to Hugo or another
static site generator.

Actually, this migration is done. This is now a Go Hugo site.

### The Links :link:

Here are some useful links:

* [Github](https://github.com/edamsoft-sre/software-engineer-blog)
* [LinkedIn](https://www.linkedin.com/in/eric-arellano-martinez/)
  * [X](https://x.com/)

### The Posts :memo:

Here are some of my favorite posts:

* Read about [DevOps and SRE]({{< ref "posts/sre_devops_glossary.md" >}}) :man_technologist:
* Read about [Linux Bash]({{< ref "posts/linux_bash.md" >}}) :penguin:
* Read about fast downloads with [aiohttp]({{< ref "posts/async_requests.md" >}}) :potable_water:
* [Read about github_emoji]({{< ref "posts/pelican_github_emojis.md" >}}), a simple [Python Markdown extension](https://github.com/edamsoft-sre/python_markdown_github_emoji_extension)

### The End :wave:

Thanks for reading! If you have any questions or comments, feel free to reach out.

---
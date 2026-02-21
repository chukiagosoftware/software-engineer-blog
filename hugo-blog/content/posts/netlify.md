---
title: "Deploy Pelican on Netlify"
date: June 30, 2020
categories: ["CICD"]
tags: ['PaaS', 'DevOps', 'CICD', 'Pelican', 'Python', 'Pipeline']
draft: false
---

Authors: Eric Arellano

### Netlify

    $ The fastest way to build the fastest sites.

![buildcommand](/images/build_command.png)

Netlify es la plataforma PaaS/CICD/DNS con integración a Git(hub|lab) utilizada para desplegar este sitio web. En 
resumen:

> 1. Connect your repository
> 2. Add your build settings
> 3. Deploy your website

Para ejecutar un app completo en Python o un static site puedes utilizar un número de librerías. Incluso Pelican 
tiene facilidades para usar *Invoke* o *Make* y gestionar diferentes contextos. Pero para este humilde blog en Pelican,
el comando por defecto de Pelican y el build command sencillo de Netlify es perfecto.

Seguí el manual y simplemente enlazo mi repo con el output en HTML de Pelican.

    $ pelican content


---

Así, le dijimos a Netlify que publique el directorio donde Pelican ha generado HTML.

    $ ls -al output/
     -rw-r--r--   1     3523 Jun 30 00:28 anadir-emojis-de-github-al-blog-de-pelican.html
     -rw-r--r--   1     2685 Jun 30 00:28 categories.html
     drwxr-xr-x   7      224 Jun 30 00:30 category
     -rw-r--r--   1     9859 Jun 30 00:28 glosario-devops.html
     -rw-r--r--   1     6871 Jun 30 00:28 index.html
     -rw-r--r--   1     3156 Jun 30 00:28 netlify-en-10-minutos.html

![publicado](/images/netlify_published.png)

---

### 

En [otro articulo]({{< ref "pelican_github_emojis.md" >}}) configuramos los emojis de Github.  Para lograr ejecutar un 
deploy de prueba en Netlify, uno sin el modulo Emoji y otro con, controlo esto de la 
siguiente forma en base al ``` setup.py```

     if [ -e setup.py ]; then python setup.py install && pelican content; else pelican content;fi

Una vez confirmado, ejecuto siempre el setup.py ya que quiero tener esos Emoji.

---

### Stork Search (Rust)  :muscle:

Adicionalmente en la última encarnación, el Blog utiliza el tema Papyrus, que incluye pelican-search además de las 
tablas de contenido.  El Pelican Search se basa en un módulo Rust que es [Stork Search](https://stork-search.net) y 
realmente es muy rápido al indexar texto, digamos un ElasticSearch localizado o para el edge, buenazo.

Añadir Stork Search es un poco complicado por ser otro lenguaje y plataforma consiguiente de desarrollo. Esto se 
maneja añadiendo otro commando al build: *build_stork_search.sh* el cual simplemente instala el toolchain de Rust y 
le comanda instalar Stork. 

Primero intenté instalar Stork directamente lo cual funciona, pero luego Netlify no permite poner esto en el PATH de 
ejecución y falla sin encontrarlo. Probablemente es una medida de seguridad importante no permitir la ejecución de 
binarios arbitrarios, entonces no le busqué más pies al gato y asumo el costo de instalar todo Rust stable 
en cada deploy por ahora.

:hankey: Could not find Stork in $Path

    wget https://files.stork-search.net/releases/v1.5.0/stork-ubuntu-20-04
    chmod +x stork-ubuntu-20-04
    

Site has been deployed. :boom: 

     #!/usr/bin/env bash
     rustup toolchain install stable
     cargo install stork-search --locked

Title: Netlify en 10 Minutos
Category: CICD
Tags: PaaS, DevOps, Web, CICD, Pelican, Python
Date: June 30, 2020

    $ The fastest way to build the fastest sites.

Netlify es una plataforma PaaS/CICD/DNS con full integración Git utilizada para desplegar este sitio web. En resumen:

> 1. Connect your repository
> 2. Add your build settings
> 3. Deploy your website

Para ejecutar un app completo en Python pueden existir diferencias y puedes utilizar un número de librerías. Pero para este blog en Pelican, el comando por defecto de Netlify es perfecto.

Seguimos el manual y simplemente enlazamos el repo y ejecutamos nuestro build command

    $ pelican content

para generar HTML de nuestro Markdown.

![buildcommand]({attach}images/build_command.png)



y zas, le decimos a Netlify que publique nuestro directorio donde Pelican ha generado HTML.

    $ ls -al output/
     -rw-r--r--   1     3523 Jun 30 00:28 anadir-emojis-de-github-al-blog-de-pelican.html
     -rw-r--r--   1     2685 Jun 30 00:28 categories.html
     drwxr-xr-x   7      224 Jun 30 00:30 category
     -rw-r--r--   1     9859 Jun 30 00:28 glosario-devops.html
     -rw-r--r--   1     6871 Jun 30 00:28 index.html
     -rw-r--r--   1     3156 Jun 30 00:28 netlify-en-10-minutos.html

![publicado]({attach}images/netlify_published.png)

#### 

En [otro articulo]({filename}pelican_github_emojis.md) configuramos los emojis de Github en este blog de Pelican. Para lograr ejecutar un deploy de prueba en Netlify, uno sin el modulo Emoji y otro con, controlamos esto de la siguiente forma en base al ``` setup.py```


     if [ -e setup.py ]; then python setup.py install && pelican content; else pelican content;fi

... próximamente ...

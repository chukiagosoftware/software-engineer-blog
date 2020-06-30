Title: Netlify en 10 Minutos
Category: CICD
Tags: PaaS, DevOps, Web, CICD, Pelican, Python

     "The fastest way to build the fastest sites." 

Netlify es la plataforma SaaS utilizada para desplegar este sitio web. En resumen:

> 1. Connect your repository
> 2. Add your build settings
> 3. Deploy your website

Para ejecutar un app en Python pueden existir diferencias. Pero para este blog en Pelican, Netlify es perfecto.

Seguimos el manual y simplemente ejecutamos

     pelican content
     
para generar HTML de nuestro Markdown, luego de descargar el repo de Github, claro.

     $ ls -al output/
     -rw-r--r--   1     3523 Jun 30 00:28 anadir-emojis-de-github-al-blog-de-pelican.html
     -rw-r--r--   1     2685 Jun 30 00:28 categories.html
     drwxr-xr-x   7      224 Jun 30 00:30 category
     -rw-r--r--   1     9859 Jun 30 00:28 glosario-devops.html
     -rw-r--r--   1     6871 Jun 30 00:28 index.html
     -rw-r--r--   1     3156 Jun 30 00:28 netlify-en-10-minutos.html


y zas, le decimos a Netlify que publique este directorio.


![publicado]({attach}images/netlify_published.png)

#### más detalles

... próximamente ...

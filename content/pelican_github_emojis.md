Title: Añadir Emojis de Github al blog en Pelican
Category: Emojis
Tags: Python, Pelican, Markdown
Date: July 10, 2020

[Pelican](https://docs.getpelican.com/en/stable/) es un generador de microblogs estáticos  en HTML/Python. Puedes utilizar Markdown, RTF, y algunos otros.

La versión 4.2.0 es muy robusta e incluye scripts para subir tu código a cualquier proveedor de nube moderno.  

Sólo que nos demoramos un poco, y ahora en lugar de Google AppEngine vamos a probar Netlify.

    # Arma tu blog así, y luego no hagas nada 2 años
    http://www.craigjperry.com/pelican-hosting-on-appengine.html  

#### Reto

No podemos utilizar emojis directamente en Pelican (es decir, con Python Markdown), pero existen algunos plugins para lo mismo, y varios repositorios de los códigos Unicode en la web.

Python maneja Unicode directamente ¡¡lo cual es genial!! 

    >>> n = "\N{FIRE}"
    >>> n
    '🔥'


Pero en este caso necesitamos algo que funcione con Markup
    
1. A conseguir los png de [GitHub](https://api.github.com/emojis) con **requests**, y copiaremos a [https://bytefish.de/blog/markdown_emoji_extension](https://bytefish.de/blog/markdown_emoji_extension) salvo que tenemos iconos más bonitos que Unicode estándar.      
       
        @staticmethod
        def load_from_github():
            try:
                resp = requests.get(SOURCE)
                payload = resp.content
                data = json.loads((payload.decode('utf-8')))
                return GheEmoji(emoji=data)
            except Exception as e:
                print(e)
    
          
1. Para crear nuestro plugin de Markdown e integrarlo con Pelican.

     *TODO*
     
     método para descargar emojis localmente  

1.  Más referencias: 

https://github.com/Dellos7/github-emoji-list

https://github.com/Python-Markdown/markdown/wiki/Tutorial:-Writing-Extensions-for-Python-Markdown
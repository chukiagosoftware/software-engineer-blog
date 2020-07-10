Title: Añadir Emojis de Github al blog en Pelican
Category: Emojis
Tags: Python, Pelican, Markdown, Github, Emoji
Date: July 10, 2020

[Pelican](https://docs.getpelican.com/en/stable/) es un generador de microblogs estáticos  en HTML/Python. Puedes utilizar Markdown, RTF, y algunos otros.

La versión 4.2.0 es muy robusta e incluye scripts para subir tu código a cualquier proveedor de nube moderno.  

Sólo que nos demoramos un poco, y ahora en lugar de Google AppEngine vamos a probar Netlify.

    # Arma tu blog así, y luego no hagas nada 2 años
    
    http://www.craigjperry.com/pelican-hosting-on-appengine.html  

#### Reto

No podemos utilizar emojis directamente en Pelican (es decir, con Python Markdown), pero existen algunos plugins para lo mismo, y varios repositorios de los códigos Unicode en la web.

Python también maneja Unicode directamente ¡¡lo cual es genial!! 

    >>> n = "\N{FIRE}"
    >>> n
    '🔥'
    
    # en caso de fuego, usar la máscara
    
    >>> u = "\U0001F637"
    >>> u
    '😷'

Pero en este caso quiero los emojis de Github.


### Código      
    
1. Conseguimos los png de [GitHub](https://api.github.com/emojis) con **requests**, y copiaremos a [https://bytefish.de/blog/markdown_emoji_extension](https://bytefish.de/blog/markdown_emoji_extension) salvo que tenemos iconos más bonitos que Unicode estándar.  Creamos nuestra clase. Python Markdown incluye varios handlers para generar tags HTML de patrones comunes, que podemos heredar y así no hacer el trabajo nosotros mismos. Usamos ``` ImageInlineProcessor ``` para crear tags ``` <img> ``` .
   
   :note: Dado que este blog se despliega en Netlify, los assets gráficos estarían en CDN globales y puede ser buena idea tener los png "localmente" en el repo para aprovechar la latencia del CDN.
   
        @staticmethod
        def load_from_github():
            try:
                resp = requests.get(SOURCE)
                payload = resp.content
                data = json.loads((payload.decode('utf-8')))
                return GheEmoji(emoji=data)
            except Exception as e:
                print(e)
                
   Haremos un método para esto pero inicialmente, vamos a simplemente descargar y usar los enlaces desde Github.  
   
1. Escribimos el resto del plugin de Markdown.

     a. Pelican se configura con un archivo Python sencillo que pasa las opciones deseadas  
  
       from github_emojis import GheEmoji
       
       MARKDOWN = { 
        'extensions' : [GheEmoji.load_from_github()], # ...
       }
       
     b. Markdown requiere una expresión regular **regex** para buscar nuestro tag de Emoticon ``` \:robot\: ``` => :robot:
   
       # let there be :+1:
         EMOJI_RE = r'(:)((?:[\+\-])?[0-9a-zA-Z]*?):'
         
     c. Creamos nuestras clases para extender Markdown y manejar los matches.        
       
       class GheEmoji(Extension):
         pattern = EmojiInlinePattern(EMOJI_RE, self.getConfig('emoji'))
         md.inlinePatterns.add('emoji', pattern, '>not_strong')
       
       class EmojiInlinePattern(Pattern):
         def __init__(self, pattern, emoji):
           super(EmojiInlinePattern, self).__init__(pattern)
           
           # acá está el json que sacamos de Github:
           
           self.emoji = emoji

       def handleMatch(self, m):
         tag = m.group(3)
         url = self.emoji.get(tag, '')
         
   Markdown nos regala un objeto Match dónde el grupo 1 es reservado, el 2 es nuestro primer ``` : ``` y el tag el 3.    

1. Ahora podemos configurar el setup.py

       from setuptools import setup
       ....
       
   E instalar el módulo en el entorno virtual (creado con pipenv):
       
       python3 setup.py develop  

1.  Listo! https://github.com/edam-software/pelican_github_emoji

1.  Bueno, ahora debemos desplegar esto en Netlify. 

        # TODO
        
        Crear un paquete para pip

    Netlify nos permite ejecutar cualquier comando Linux, que generalmente será alguna herramienta para builds y en este caso es ``` pelican content ```
   
    Intentamos replicar el entorno de desarrollo y correr 
   
   ``` python3 setup.py install && pelican content ```
   
    A ver si funciona!  

1.  Referencias 


https://github.com/Dellos7/github-emoji-list

https://github.com/Python-Markdown/markdown/wiki/Tutorial:-Writing-Extensions-for-Python-Markdown
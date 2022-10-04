Title: Emojis de Github con Python Markdown
Category: Emojis
Tags: Python, Regex, Pelican, Markdown, Emoji
Date: July 10, 2020
Summary: Python Markdown extension for Github Emojis used in this Pelican blog 


### Pelican blog with Python Markdown
[Pelican](https://docs.getpelican.com) es un generador de microblogs estáticos en HTML/Python. Permite utilizar 
Markdown, RTF, y algunos otros formatos de texto para su contenido. La versión 4.8.0 es muy robusta e incluye 
scripts para subir el código a cualquier proveedor de nube y desplegar cambios, así como un servidor de desarrollo y 
un catálogo amplio de extensiones y temas.

Armé el blog inicialmente según  [pelican-hosting-on-appengine.html](http://www.craigjperry.
com/pelican-hosting-on-appengine.html), pero me demoré un poco, y ahora en lugar de Google AppEngine lo despliego 
mediante Netlify.
---

### Reto: Github Emojis en Pelican

No se pueden utilizar emojis directamente en Pelican (es decir, con Python Markdown), pero existen varios plugins 
para lo mismo, y varios repositorios de los códigos Unicode en la web. Python también maneja Unicode directamente 
¡¡lo cual es genial!!  

    >>> n = "\N{FIRE}"
    >>> n
    '🔥'
     
    >>> u = "\U0001F637"
    >>> u
    '😷'

Pero en este caso quiero los emojis de Github especificamente, porque son más bonitos.
---

### Método

Conseguí los png del API [GitHub](https://api.github.com/emojis) con **requests**, y copiaremos a [https://bytefish.
de/blog/markdown_emoji_extension](https://bytefish.de/blog/markdown_emoji_extension) salvo que tenemos emojis 
disponibles en el enlace mencionado,  en mi opinión mejores que Unicode estándar y las demás ofertas en internet.

###  Markdown Extension

[Python Markdown](https://python-markdown.github.io) incluye la posiblidad de modificar el archivo *.md* antes y 
durante el análisis léxico, e inclusive después de generado el HTML. Para esto se utilizan una variedad de 
Processors y Handlers que mayormente vienen con el módulo. 

Estos cubren la mayoría de necesidades como ser HTML tags, imágenes, símbolos comunes, etc. Primero, Pelican se configura con un archivo Python sencillo que pasa las opciones deseadas. He desarrollado la 
clase GheEmoji que permite bajar los datos de Github: ```{ shortname: image_url}``` 
  

        from github_emojis import GheEmoji
       
        MARKDOWN = { 
         'extensions' : [GheEmoji.load_from_github()], # ...
      }

---       

Markdown requiere una expresión regular o **regex** para encontrar cada shortname por ejemplo

``` \:robot\: ``` =>  :robot:


Permitiremos +1 y tags con _

      EMOJI_RE = r'(:)((?:[\+\-])?[_0-9a-zA-Z]*?):'
     
#### Inline Processor

Siguiendo el manual de Markdown, creamos una clase para extender Markdown.Extension.   Inicialmente, usamos 
*ImageInlinePattern* para crear nuestro HTML tag *img* a partir del shortname del emoji Github. Posteriormente con 
la versión 3.4.1 actual, se recomienda utilizar *InlineProcessor*
      
#### Previous extension with InlinePattern
         from markdown.extensions import Extension
         
         class GheEmoji(Extension):
           pattern = EmojiInlinePattern(EMOJI_RE, self.getConfig('emoji'))
           md.inlinePatterns.add('emoji', pattern, '>not_strong')
       
         class EmojiInlinePattern(Pattern):
           def __init__(self, pattern, emoji):
             super(EmojiInlinePattern, self).__init__(pattern)
             self.emoji = emoji

         def handleMatch(self, m):
           tag = m.group(3)
           url = self.emoji.get(tag, '')
           
     d. Markdown nos brinda un objeto Match dónde el grupo 1 es reservado, el 2 es nuestro primer ``` : ``` y el tag el 3.    
---

#### Latest Python Markdown with InlineProcessor

Aqui utilizamos la misma regex, con una lógica algo diferente. InlineProcessor permite más control sobre el 
resultado y gestionar espacios o carácteres especiales. Además, aproveché el XML Etree para añadir el CSS class 
correspondiente que convierte a los emoji en inline_block del tamaño del texto.

    class EmojiInlineProcessor(InlineProcessor):
    def __init__(self, pattern, emoji):
        super(EmojiInlineProcessor, self).__init__(pattern)
        self.emoji = emoji

    def handleMatch(self, m, data):
        tag = m.group(2)
        url = self.emoji.get(tag, '')
        if not url:
            return None, None, None
        div = etree.Element("div")
        div.attrib["class"] = "ghe_emoji"
        el = etree.SubElement(div, "img")
        el.attrib["class"] = "ghe_emoji"
        el.set("src", url)
        el.set("title", tag)
        el.set("alt", tag)
        return div, m.start(0), m.end(0)

---

#### Python Setup

     setup(
    name='python_markdown_gh_emoji',
    version='0.9',
    packages=find_packages(),
    py_modules=['python_markdown_gh_emoji'],
    install_requires=['markdown>=3.0'],
    python_requires='>3.7',
    url='https://github.com/edam-software/github_emojis',
    license="OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    author='EDAM',
    author_email='eric.arellano@hey.com',
    description='Markdown extension to provide Github emoji (in Pelican)',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent"]
    )
   
[Código completo](https://github.com/edam-software/python_markdown_github_emoji_extension)

---

Test/usage

        txt = """
         line 1 :fight:
         line 2 :smiley:
         line 3 :metal:
         """
        
        result = markdown.markdown(txt, extensions=[GheEmoji.load_from_github()])
        assert result == """<p>line 1 
         line 2 <img alt="smiley" src="https://github.githubassets.com/images/icons/emoji/unicode/1f603.png?v8" title="smiley" />
         line 3 <img alt="metal" src="https://github.githubassets.com/images/icons/emoji/unicode/1f918.png?v8" title="metal" /></p>"""
        
        # plus_one = """
        # :+1: the plus sign
        # """
        #
        # thumbs_up = markdown.markdown(plus_one, extensions=[GheEmoji.load_from_github()])
        # print(thumbs_up)

___

#### Desplegar el blog con módulo emoji en Netlify. 

Netlify nos permite ejecutar cualquier comando Linux, que generalmente será alguna herramienta para builds y en este 
caso es ``` pelican content ```.  La idea es replicar el entorno de desarrollo y correr ``` python3 setup.py install && 
pelican content ```.

Para desarrollar este "feature" y no romper el sitio en vivo, creo un despliego mediante git branch, es decir 
configuramos Netlify para hacer un branch deploy.

   ![Branch Deploy]({attach}images/netlify_branch.png)
   
Y zás, está este blog emojiado :bowing_man:

---



En [CICD con Netlify]({filename}netlify.md) hablare más sobre estrategias de despliegue.

#### Referencias :book:

[github-emoji-list](https://github.com/Dellos7/github-emoji-list)

[Tutorial:-Writing-Extensions-for-Python-Markdown](https://github.com/Python-Markdown/markdown/wiki/Tutorial:-Writing-Extensions-for-Python-Markdown)

[PathLib](https://docs.python.org/3/library/pathlib.html)
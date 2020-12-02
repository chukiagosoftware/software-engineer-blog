Title: Descargas asíncronas con Async y aiohttp
Date:  December 1, 2020
Category: Emojis
Tags: Python, Pelican, Markdown, Emoji, requests, Async, aiohttp

En [Emojis de Github para Pelican con Markdown]({filename}pelican_github_emojis.md) armamos los hermosos íconos que se pueden ver por este blog.

Poco a poco vamos a mejorar algunas cosas, como el tamaño de los mismos con ImageMagick, o quién sabe qué otra librería descubriremos.

:snail:

Lo cuál me recuerda. Lo lindo de Python es que se puede hacer casi cualquier cosa, con un poco de estilo y sencillez. Nada de Java arcáico o Javascript surrealista, sólo código rico que funciona.

Pero divagamos.  Para descargar los 1793 emojis de GitHub..

:copyright:

la operación toma unos insoportables 5 minutos. Qué es esto, Atari? No, no puede quedar así.

![sync_download]({attach}images/sync.png)

Podríamos utilizar Threads, pero la idea es mirar hacia adelante con optimismo y darle con Async.

A veces, un diff vale mil palabras y esperemos que esta es una de esas veces.

![diff]({attach}images/diff.png)

Como ojalá puede ver, es increíblemente fácil añadir un poco de concurrencia a un sencillo código en Python con Async (y aiohttp, claro!).

 :godmode:

Ahorramos valiosos segundos, que en una aplicación real con muchos usuarios y todo eso, llegan a ser muy importantes.


![async_download]({attach}images/async_download.png)
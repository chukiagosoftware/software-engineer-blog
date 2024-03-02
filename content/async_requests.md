Title: Descargas asíncronas con Aiohttp | Async file download
Date:  December 1, 2020
Category: Python
Tags: Python, Asyncio, Emoji, requests, aiohttp
Authors: Eric Arellano

### Download Github Emojis locally 

![diff]({attach}images/diff.png)

En [Emojis de Github para Pelican con Markdown]({filename}pelican_github_emojis.md) armamos los hermosos íconos que 
se pueden ver por este blog. Bueno, en realidad bajamos el archivo json de Github con el diccionarios 

    #!python
    { _short_name_ : _http_url }

y utilizamos los enlaces para armar tags *img*. Poco a poco hemos mejorado algunas cosas, como regualr el tamaño de 
los íconos 64x64 con CSS.

Para descargar los 1793 emojis de GitHub :copyright:  la operación toma mucho tiempo para tan solo 9.1M: como 15 
minutos :stopwatch: 

En realidad es solamente esperar el round trip time entre nosotros y github.com 1800 veces, lo cual es una 
aplicación perfecta para IO mediante Async. 

![sync_download]({attach}images/sync.png)

---
Podríamos utilizar *threading.Thread* pero la idea es mirar hacia adelante con optimismo y darle con Async.

A veces, un diff vale mil palabras y esperemos que esta es una de esas veces.

Como se puede ver, es fácil añadir un poco de concurrencia async a un sencillo código en Python con 
Async y aiohttp.  :godmode:  Ahorramos valiosos minutos, que en una aplicación compleja pueden ser importantes.


![async_download]({attach}images/async_download.png)

---

### The code

#### The good old Requests method:

    @staticmethod
    def load_from_github():
        try:
            resp = requests.get(SOURCE)
            payload = resp.content
            data = json.loads((payload.decode('utf-8')))
            return GheEmoji(emoji=data)
        except Exception as e:
            print(e)

---

#### Quick and dirty aiohttp client session and write bytes

    @staticmethod
    async def get_bytes(url: str) -> bytes:
        async with aiohttp.ClientSession() as sesh:
            async with sesh.get(url) as payload:
                data = await payload.read()
                return data

    @staticmethod
    async def write_bytes(path: str, data: bytes) -> bool:
        try:
            with Path(f"{SAVE_PATH}{path}.png").open('xb') as file_name:
                file_name.write(data)
        except FileExistsError as failed:
            print(failed)
            return

    @staticmethod
    async def fetch_task(tag: str, url: str):
        file = url.split('/')[-1]
        content = await GheEmoji.get_bytes(url)
        await GheEmoji.write_bytes(tag, content)

    async def download(self):
        tasks = []
        for tag, url in self.getConfig('emoji').items():
            tasks.append(self.fetch_task(tag, url))
        await asyncio.wait(tasks)

---
#### Running the test

    t0 = datetime.now()
    # single Get, just uses Requests
    m = GheEmoji.load_from_github() 
    
    asyncio.run(m.download())
    dt = datetime.now() - t0
    print(f"This took {dt} to run")

# kodi-addons-async
https://docs.python.org/3/library/asyncio.html

**Most addons are network bound, trying to get rid of it.**

# Seems to be working
Got https://docs.aiohttp.org/en/stable/web_quickstart.html# up.
```
2022-04-27 22:18:25.581 T:4483    DEBUG <general>: AIOHTTP getting event-loop, http://localhost:1081
2022-04-27 22:18:27.423 T:4460    DEBUG <general>: Sink changed
2022-04-27 22:18:30.109 T:4485    DEBUG <general>: AIOHTTP Application Starting, http://localhost:1081
2022-04-27 22:18:30.109 T:4485    DEBUG <general>: AIOHTTP Adding route and handler "hello", http://localhost:1081
2022-04-27 22:18:30.109 T:4485    DEBUG <general>: AIOHTTP Creating runner, http://localhost:1081
2022-04-27 22:18:30.109 T:4485    DEBUG <general>: AIOHTTP runner setup, http://localhost:1081
2022-04-27 22:18:30.110 T:4485    DEBUG <general>: AIOHTTP Creating site, http://localhost:1081
2022-04-27 22:18:30.110 T:4485    DEBUG <general>: AIOHTTP Starting site, http://localhost:1081
2022-04-27 22:18:41.695 T:4485    DEBUG <general>: AIOHTTP Application Request: !!!
2022-04-27 22:18:41.695 T:4485    DEBUG <general>: AIOHTTP TEST running...
2022-04-27 22:18:53.763 T:4474    DEBUG <general>: Thread JobWorker 140551991064128 terminating (autodelete)
2022-04-27 22:18:53.763 T:4475    DEBUG <general>: Thread JobWorker 140551982671424 terminating (autodelete)
2022-04-27 22:18:53.763 T:4472    DEBUG <general>: Thread JobWorker 140552086431296 terminating (autodelete)
2022-04-27 22:22:45.453 T:4485    DEBUG <general>: AIOHTTP Application Request: !!!
2022-04-27 22:22:45.453 T:4485    DEBUG <general>: AIOHTTP TEST running...
```

```
LibreELEC:~ # curl -v http://localhost:1081
*   Trying 127.0.0.1:1081...
* Connected to localhost (127.0.0.1) port 1081 (#0)
> GET / HTTP/1.1
> Host: localhost:1081
> User-Agent: curl/7.74.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-Type: text/plain; charset=utf-8
< Content-Length: 389
< Date: Wed, 27 Apr 2022 22:22:45 GMT
< Server: Python/3.8 aiohttp/4.0.0a1
< 
Hello there! Wanna run a test? Ups ran it already...
http://httpbin.org/get.resp=<ClientResponse(http://httpbin.org/get) [200 OK]>
<CIMultiDictProxy('Date': 'Wed, 27 Apr 2022 22:22:45 GMT', 'Content-Type': 'application/json', 'Content-Length': '311', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true')>
* Connection #0 to host localhost left intact
```

# Status
Struggle acquiring a clean https://docs.python.org/3/library/asyncio-eventloop.html, we're still in a Kodi thread.

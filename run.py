from aiohttp import web


async def http_handler(request):
    name = request.match_info.get('name', "person")
    text = "Hello world, " + name + "!"
    return web.Response(text=text)


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            await ws.send_str("Hello, {}".format(msg.data))
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws


async def app():
    application = web.Application()
    application.add_routes([
        web.get('/', http_handler),
        web.get('/ws', websocket_handler),
        web.get('/{name}', http_handler)
    ])
    return application


if __name__ == '__main__':
    web.run_app(app())

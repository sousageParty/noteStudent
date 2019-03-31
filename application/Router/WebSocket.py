import aiohttp
import json


class WebSocket:

    web = None
    wss = {}
    SOCKET_EVENTS = {}  # Объект с обработчиками всевозможных событий

    def __init__(self, web, mediator):
        self.web = web
        self.mediator = mediator
        self.EVENTS = self.mediator.getEvents()
        self.TRIGGERS = self.mediator.getTriggers()

    # обработчик вообще всех сокетных запросов, которые могут прилететь в сервер
    async def get(self, request):
        ws = self.web.WebSocketResponse()
        await ws.prepare(request)
        print('websocket connection open')
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.text:
                if msg.data == 'close':  # сообщение, чтобы закрыть соединение
                    await ws.close()
                else:  # все остальные сообщения
                    obj = json.loads(msg.data)  # преобразовать в объект
                    if obj:
                        if 'id_message' in obj.keys() and obj['id_message'] in self.SOCKET_EVENTS.keys():
                            await self.SOCKET_EVENTS[obj['id_message']](obj, ws)  # Обрабатываем всевозможные события
            elif msg.type == aiohttp.WSMsgType.error:
                print('connection broken')
                print(ws.exception())
                break
        print('websocket connection close')
        return True

    # Слушатель сообщений
    def on(self, idMessage, cb):
        if idMessage in self.SOCKET_EVENTS.keys():
            raise KeyError("Handler for this message already exists!!!")
        self.SOCKET_EVENTS[idMessage] = cb

    # Послать сообщение всем клиентам или одному, кто подключен к серверу.
    async def emit(self, idMessage, data=None, idSocket=None):
        data['id_message'] = idMessage
        if idSocket:
            return None
        else:
            for key in self.wss:
                await self.wss[key].send_str(str(data))
            return None

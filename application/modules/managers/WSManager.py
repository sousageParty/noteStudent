from application.modules.managers.BaseManager import BaseManager


class WSManager(BaseManager):

    def __init__(self, options):
        super().__init__(options)
        self.socket.on(self.SOCKET_EVENTS['START_CONNECTION'], self.connect)
        self.socket.on(self.SOCKET_EVENTS['TEST_MESSAGE'], self.test)

    # Поднять сокетное соединение
    async def connect(self, data, ws):
        if data['id']:
            self.socket.wss[data['id']] = ws  # запомнить сокет клиента в список сокетов
            print(data['id'])

    async def test(self, data, ws):
        print(data)
        await self.socket.emit('TEST_MESSAGE', {
            'text': 'test text'
        })
from .ApiAnswer import ApiAnswer


class Router:

    web = None
    api = None

    # Метод, проверяющий параметры, пришедшие в теле запроса. method - название метода, data - данные, пришедшие в метод
    @staticmethod
    def checkParams(method, data):
        if method == 'addUser':
            if 'login' in data.keys() and 'password' in data.keys() and 'group' in data.keys() and 'type' in data.keys() and 'name' in data.keys() and 'surname' in data.keys() and 'thirdname' in data.keys():
                return True
            return False
        return False

    def __init__(self, app, web, mediator):
        self.web = web
        self.api = ApiAnswer()
        self.mediator = mediator
        self.TYPES = mediator.getTypes()
        self.TRIGGERS = mediator.getTriggerTypes()
        routes = [
            ('*', '/', self.staticHandler),
            # О юзерах
            ('GET', "/api/user", self.getUsers),  # Получить всех юзеров
            ('GET', "/api/user/{login}", self.getUser),  # Получить юзера по ИД
            ('POST', "/api/user", self.addUser),  # Добавить юзера и студента одновременно
            ('GET', "/api/user/login/{login}/{password}", self.login),  # Логин юзера
            ('GET', "/api/user/logout/{token}", self.logout),  # Выход юзера
            # О группах
            ('GET', '/api/group/codes', self.getGroupsCodes)  # Получить коды групп
        ]
        app.router.add_static('/img/', path=str('./public/img/'))
        app.router.add_static('/css/', path=str('./public/css/'))
        app.router.add_static('/js/', path=str('./public/js/'))
        for route in routes:
            app.router.add_route(route[0], route[1], route[2])

    def staticHandler(self, request):
        return self.web.FileResponse('./public/index.html')

    def getUsers(self, request):
        return self.web.json_response(self.api.answer(self.mediator.get(self.TRIGGERS['GET_USERS'])))

    def getUser(self, request):
        login = request.match_info.get('login')
        result = self.mediator.get(self.TRIGGERS['GET_USER'], {'login': login})
        if result:
            return self.web.json_response(self.api.answer(result))
        return self.web.json_response(self.api.error(404))

    async def addUser(self, request):
        data = await request.json()
        if self.checkParams('addUser', data):
            result = self.mediator.get(self.TRIGGERS['SET_USER'], data)
            if result:
                return self.web.json_response(self.api.answer(result))
            return self.web.json_response(self.api.error(2000))
        return self.web.json_response(self.api.error(1000))

    def login(self, request):
        login = request.match_info.get('login')
        password = request.match_info.get('password')
        result = self.mediator.get(self.TRIGGERS['LOGIN'], {'login': login, 'password': password})
        if result:
            return self.web.json_response(self.api.answer(result))
        return self.web.json_response(self.api.error(2010))

    def logout(self, request):
        token = request.match_info.get('token')
        result = self.mediator.get(self.TRIGGERS['LOGOUT'], {'token': token})
        if result:
            return self.web.json_response(self.api.answer(result))
        return self.web.json_response(self.api.error(2010))

    def getGroupsCodes(self, request):
        return self.web.json_response(self.api.answer(self.mediator.get(self.TRIGGERS['GET_GROUPS_CODES'])))

from .ApiAnswer import ApiAnswer
from .WebSocket import WebSocket

# Класс для описасния API методов и их обработчиков
class Router:

    web = None
    api = None

    # Метод, проверяющий параметры, пришедшие в теле запроса. method - название метода, data - данные, пришедшие в метод
    @staticmethod
    def checkParams(method, data):
        if method == 'addUser':
            if 'login' in data.keys() and 'password' in data.keys() and 'group' in data.keys() and 'type' in data.keys() and 'name':
                return True
            return False
        return False

    def __init__(self, app, web, mediator, webSocket):
        self.web = web
        self.api = ApiAnswer()
        self.mediator = mediator
        self.TYPES = mediator.getEvents()
        self.TRIGGERS = mediator.getTriggers()
        routes = [
            ('*', '/', self.staticHandler),
            ('GET', '/ws', webSocket.get),
            # О юзерах
            ('GET', "/api/user", self.getUsers),  # Получить всех юзеров
            ('GET', "/api/user/{login}", self.getUser),  # Получить юзера по логину
            ('GET', "/api/user/type/{token}", self.getUserTypeByToken),  # Получить тип юзера по токену
            ('POST', "/api/user", self.register),  # Добавить юзера и студента одновременно
            ('POST', "/api/updatePassword", self.updatePassword),
            ('GET', "/api/user/login/{login}/{password}/{rnd}", self.login),  # Логин юзера
            ('GET', "/api/user/logout/{token}", self.logout),  # Выход юзера
            # О группах
            ('GET', '/api/group/codes', self.getGroupsCodes),  # Получить коды групп
            # О студентах
            ('GET', '/api/student/note/{tokenAdmin}/{tokenStudent}', self.noteStudent),  # Отметить студентов
            ('GET', '/api/student/getOnLesson/{tokenAdmin}/{date}/{lessonNum}', self.getStudentsOnLesson)  # Получить список студентов, бывших на конкретной паре, конкретного дня
        ]
        app.router.add_static('/img/', path=str('./public/img/'))
        app.router.add_static('/css/', path=str('./public/css/'))
        app.router.add_static('/js/', path=str('./public/js/'))
        for route in routes:
            app.router.add_route(route[0], route[1], route[2])

    def staticHandler(self, request):
        return self.web.FileResponse('./public/index.html')

    def getUserTypeByToken(self, request):
        token = request.match_info.get('token')
        result = self.mediator.get(self.TRIGGERS['GET_USER_TYPE_BY_TOKEN'], {'token': token})
        if result:
            return self.web.json_response(self.api.answer(result))
        return self.web.json_response(self.api.error(404))

    def getUsers(self, request):
        return self.web.json_response(self.api.answer(self.mediator.get(self.TRIGGERS['GET_USERS'])))

    def getUser(self, request):
        token = request.match_info.get('token')
        result = self.mediator.get(self.TRIGGERS['GET_USER'], {'token': token})
        if result:
            result['password'] = ''
            return self.web.json_response(self.api.answer(result))
        return self.web.json_response(self.api.error(404))



    async def updatePassword(self, request):
        data = await request.json()
        result = self.mediator.get(self.TRIGGERS['UPDATE_PASSWORD'], data)
        if result:
            return self.web.json_response(self.api.answer(result))



    async def register(self, request):
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
        rnd = request.match_info.get('rnd')
        result = self.mediator.get(self.TRIGGERS['LOGIN'], {'login': login, 'password': password, 'rnd': rnd})
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

    def noteStudent(self, request):
        tokenAdmin = request.match_info.get('tokenAdmin')
        tokenStudent = request.match_info.get('tokenStudent')
        result = self.mediator.get(self.TRIGGERS['NOTE_STUDENT'], {'tokenAdmin': tokenAdmin, 'tokenStudent': tokenStudent})
        if result:
            return self.web.json_response(self.api.answer(result))
        return self.web.json_response(self.api.error(3010))

    def getStudentsOnLesson(self, request):
        tokenAdmin = request.match_info.get('tokenAdmin')
        date = request.match_info.get('date')
        lessonNum = request.match_info.get('lessonNum')
        result = self.mediator.get(self.TRIGGERS['GET_STUDENTS_ON_LESSON'], {'tokenAdmin': tokenAdmin, 'date': date, 'lessonNum': lessonNum})
        if result or result == []:
            return self.web.json_response(self.api.answer(result))
        return self.web.json_response(self.api.error(3020))

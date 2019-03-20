# Описание структуры данных Пользователь
class User:

    id = None
    login = None
    password = None
    token = None
    name = None

    def __init__(self, params):
        self.id = int(params['id'])
        self.login = str(params['login'])
        self.password = str(params['password'])
        self.name = str(params['name'])
        self.token = str(params['token'])

    def __str__(self):
        return {'id': self.id, 'login': self.login, 'password': self.password, 'token': self.token, 'name': self.name}

    # Сериализация класса в объект
    def get(self):
        return {'id': self.id, 'login': self.login, 'password': self.password, 'token': self.token, 'name': self.name}

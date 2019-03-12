class User:

    id = None
    login = None
    password = None
    token = None

    def __init__(self, params):
        self.id = int(params['id'])
        self.login = str(params['login'])
        self.password = str(params['password'])
        self.token = str(params['token'])

    def __str__(self):
        return {'id': self.id, 'login': self.login, 'password': self.password, 'token': self.token}

    def get(self):
        return {'id': self.id, 'login': self.login, 'password': self.password, 'token': self.token}

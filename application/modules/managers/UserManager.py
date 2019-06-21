from hashlib import md5
import random

from .BaseManager import BaseManager
from ..struct.User import User


# Класс для описания методов для работы с пользователями
class UserManager(BaseManager):

    users = {}

    def __init__(self, params):
        super().__init__(params)
        self.mediator.set(self.TRIGGERS['GET_ACTIVE_USERS'], self.getActiveUsers)
        self.mediator.set(self.TRIGGERS['GET_USER'], self.getUser)
        self.mediator.set(self.TRIGGERS['GET_USER_TYPE_BY_TOKEN'], self.getUserTypeByToken)
        self.mediator.set(self.TRIGGERS['GET_USERS'], self.getUsers)
        self.mediator.set(self.TRIGGERS['SET_USER'], self.setUser)
        self.mediator.set(self.TRIGGERS['UPDATE_PASSWORD'], self.updatePassword)
        self.mediator.set(self.TRIGGERS['LOGIN'], self.login)
        self.mediator.set(self.TRIGGERS['LOGOUT'], self.logout)

    # Обновление пароля. data = {login, newPassword}
    def updatePassword(self, data):
        user = self.getUser(data)
        if user:
            if (data['newPassword']):
                self.db.updatePassword(user['id'], data['newPassword'])
                user.update({'password': data['newPassword']})
                self.users.update({data['newPassword']: User(user)})
                return data['newPassword']
        return False

    # Регистрация. data = {login, password, name}
    def setUser(self, data):
        result = self.db.addUser(data)
        if result:
            data['userId'] = result['id']
            return self.mediator.get(self.TRIGGERS['SET_STUDENT'], data)
        return False

    def getActiveUsers(self, data):
        return self.users

    def getUserTypeByToken(self, data):
        user = self.db.getUserByToken(data['token'])
        if user:
            return self.db.getStudentType(user['id'])
        return False

    # Получить пользователя по логину. data = {login}
    def getUser(self, data):
        return self.db.getUserByLogin(data['login'])

    def getUsers(self, data):
        return self.db.getUsers()

    # Вход в систему. data = {login, password, rnd}
    def login(self, data):
        user = self.getUser(data)
        if user:
            passHash = md5((user['password'] + str(data['rnd'])).encode('utf-8')).hexdigest()
            if user and data['password'] == passHash:
                rnd = random.random()
                token = md5((str(rnd) + user['login'] + user['password']).encode('utf-8')).hexdigest()
                self.db.setToken(user['id'], token)
                user.update({'token': token})
                self.users.update({token: User(user)})
                return token
        return False

    # Выход из системы. data = {token}
    def logout(self, data):
        user = self.db.getUserByToken(data['token'])
        if user:
            self.db.setToken(user['id'])
            return True
        return False

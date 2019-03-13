from hashlib import md5
import random

from .BaseManager import BaseManager
from ..struct.User import User


class UserManager(BaseManager):

    users = {}

    def __init__(self, params):
        super().__init__(params)
        self.mediator.set(self.TRIGGERS['GET_USER'], self.getUser)
        self.mediator.set(self.TRIGGERS['GET_USERS'], self.getUsers)
        self.mediator.set(self.TRIGGERS['SET_USER'], self.setUser)
        self.mediator.set(self.TRIGGERS['LOGIN'], self.login)
        self.mediator.set(self.TRIGGERS['LOGOUT'], self.logout)

    def getUser(self, data):
        return self.db.getUserByLogin(data['login'])

    def getUsers(self, data):
        return self.db.getUsers()

    def setUser(self, data):
        result = self.db.addUser(data)
        if result:
            data['userId'] = result['id']
            return self.mediator.get(self.TRIGGERS['SET_STUDENT'], data)
        return False

    def login(self, data):
        user = self.getUser(data)
        passHash = md5((user['password'] + str(data['rnd'])).encode('utf-8')).hexdigest()
        if user and data['password'] == passHash:
            rnd = random.random()
            token = md5((str(rnd) + user['login'] + user['password']).encode('utf-8')).hexdigest()
            self.db.setToken(user['id'], token)
            user.update({'token': token})
            self.users.update({token: User(user)})
            return token
        return False

    def logout(self, data):
        user = self.db.getUserByToken(data['token'])
        if user:
            self.db.setToken(user['id'])
            self.users.pop(data['token'])
            return True
        return False

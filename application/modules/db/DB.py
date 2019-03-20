import sqlite3


# Класс для работы с базой данных.
# Все запросы прописываются здесь
class DB:

    conn = None

    def __init__(self, settings):
        self.conn = sqlite3.connect(settings['PATH'])
        self.conn.row_factory = self.dictFactory
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    @staticmethod
    def dictFactory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def getUserByLogin(self, login):
        query = 'SELECT * FROM user WHERE login=:login'
        self.c.execute(query, {'login': login})
        return self.c.fetchone()

    def getUserByToken(self, token):
        query = 'SELECT id FROM user WHERE token=:token'
        self.c.execute(query, {'token': token})
        return self.c.fetchone()

    def getUsers(self):
        query = 'SELECT * FROM user'
        self.c.execute(query)
        return self.c.fetchall()

    def setToken(self, id, token=None):
        query = 'UPDATE user SET token=:token WHERE id=:id'
        self.c.execute(query, {"token": token, "id": id})
        self.conn.commit()

    def addUser(self, data):
        query = 'INSERT INTO user (login, password, name) VALUES (:login, :password, :name)'
        try:
            self.c.execute(query, {'login': data['login'], 'password': data['password'], 'name': data['name']})
            self.conn.commit()
        except sqlite3.IntegrityError:
            return False
        user = self.getUserByLogin(data['login'])
        return user

    def addStudent(self, data):
        query = 'INSERT INTO student (user_id, group_id, type) ' \
                'VALUES (:userId, (SELECT id FROM "group" WHERE "group".code = :group), :type)'
        self.c.execute(query, {'userId': data['userId'], 'group': data['group'], 'type': data['type']})
        self.conn.commit()
        return True

    def getGroupsCodes(self):
        query = "SELECT code FROM 'group'"
        self.c.execute(query)
        return self.c.fetchall()

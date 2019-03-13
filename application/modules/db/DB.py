import sqlite3


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
        query = 'SELECT * FROM users WHERE login=:login'
        self.c.execute(query, {'login': login})
        return self.c.fetchone()

    def getUserByToken(self, token):
        query = 'SELECT id FROM users WHERE token=:token'
        self.c.execute(query, {'token': token})
        return self.c.fetchone()

    def getUsers(self):
        query = 'SELECT * FROM users'
        self.c.execute(query)
        return self.c.fetchall()

    def setToken(self, id, token=None):
        query = 'UPDATE users SET token=:token WHERE id=:id'
        self.c.execute(query, {"token": token, "id": id})
        self.conn.commit()

    def addUser(self, data):
        query = 'INSERT INTO users (login, password) VALUES (:login, :password)'
        try:
            self.c.execute(query, {'login': data['login'], 'password': data['password']})
            self.conn.commit()
        except sqlite3.IntegrityError:
            return False
        user = self.getUserByLogin(data['login'])
        return user

    def addStudent(self, data):
        query = 'INSERT INTO student (user_id, group_id, name, surname, thirdname, type) ' \
                'VALUES (:userId, (SELECT id FROM groups WHERE groups.code = :group), :name, :surname, :thirdname, :type)'
        self.c.execute(query, {'userId': data['userId'], 'group': data['group'],
                               'name': data['name'], 'surname': data['surname'],
                               'thirdname': data["thirdname"], 'type': data['type']})
        self.conn.commit()
        return True

    def getGroupsCodes(self):
        query = 'SELECT code FROM groups'
        self.c.execute(query)
        return self.c.fetchall()

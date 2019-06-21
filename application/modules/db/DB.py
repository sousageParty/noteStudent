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

    def updatePassword (self, id, password):
        query = 'UPDATE user SET password=:password WHERE id=:id'
        self.c.execute(query, {"password": password, "id": id})
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

    def getStudentByToken(self, token):
        query = "SELECT " \
                 "student.id AS student_id, student.group_id AS group_id, student.type AS type, " \
                 "user.id AS id, user.login AS login, user.password AS password, user.name AS name, user.token AS token " \
                "FROM student JOIN user ON (student.user_id = user.id) " \
                "WHERE user.token = :token"
        self.c.execute(query, { 'token': token })
        return self.c.fetchone()

    def getGroupsCodes(self):
        query = "SELECT code FROM 'group'"
        self.c.execute(query)
        return self.c.fetchall()

    def getCurrentLesson(self):
        query = "SELECT * FROM lesson_time WHERE time_start < time('now', 'localtime') AND time('now', 'localtime') < time_finish"
        self.c.execute(query)
        return self.c.fetchone()

    def noteStudent(self, adminId, studentId, lessonId):
        query = "INSERT INTO " \
                 "student_on_lessons (admin_id, students_id, lesson_time_id, date, time) " \
                "VALUES (:adminId, :studentId, :lessonId, date('now', 'localtime'), time('now', 'localtime'))"
        self.c.execute(query, {"adminId": adminId, "studentId": studentId, "lessonId": lessonId})
        self.conn.commit()
        return True

    def getLessonByNum(self, lessonNum):
        query = "SELECT * FROM lesson_time WHERE num_lesson = :lessonNum"
        self.c.execute(query, { "lessonNum": lessonNum })
        return self.c.fetchone()

    def getStudentOnLesson(self, studentId, lessonId):
        query = "SELECT * " \
                "FROM student_on_lessons " \
                "WHERE students_id = :studentId " \
                 "AND lesson_time_id = :lessonId " \
                 "AND student_on_lessons.date = date('now', 'localtime')"
        self.c.execute(query, { "studentId": studentId, "lessonId": lessonId })
        return self.c.fetchone()

    def getStudentsOnLesson(self, adminId, date, lessonId):
        query = "SELECT " \
                  "student_on_lessons.date AS date, student_on_lessons.time AS time, " \
                  "lesson_time.num_lesson AS lessonNum, lesson_time.time_start AS timeStart, lesson_time.time_finish AS timeFinish, " \
                  "student.type AS type, user.id AS userId, user.name AS name, 'group'.short_name AS shortName " \
                "FROM student_on_lessons " \
                  "JOIN lesson_time ON (student_on_lessons.lesson_time_id = lesson_time.id) " \
                  "JOIN user ON (user.id = student_on_lessons.students_id) " \
                  "JOIN student ON (student.user_id = user.id) " \
                  "JOIN 'group' ON ('group'.id = student.group_id) " \
                "WHERE student_on_lessons.date = :date " \
                  "AND student_on_lessons.admin_id = :adminId " \
                  "AND student_on_lessons.lesson_time_id = :lessonId;"
        self.c.execute(query, { "adminId": adminId, "date": date, 'lessonId': lessonId })
        return self.c.fetchall()

    def getStudentType(self, id):
        query = "SELECT type FROM student WHERE user_id = :id"
        self.c.execute(query, {'id': id})
        return self.c.fetchone()


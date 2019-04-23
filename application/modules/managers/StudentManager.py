import threading
from datetime import datetime
from ..struct.Student import Student
from .BaseManager import BaseManager


# Класс для описания методов для работы со студентами
class StudentManager(BaseManager):

    def __init__(self, params):
        super().__init__(params)
        self.mediator.set(self.TRIGGERS['SET_STUDENT'], self.setStudent)
        self.mediator.set(self.TRIGGERS['NOTE_STUDENT'], self.noteStudent)
        self.mediator.set(self.TRIGGERS['GET_STUDENTS_ON_LESSON'], self.getStudentsOnLesson)

    # Добавить студента data = {userId, group, type}
    def setStudent(self, data):
        return self.db.addStudent(data)

    def normalizeStudent(self, student):
        users = self.mediator.get(self.TRIGGERS['GET_ACTIVE_USERS'])
        for u in users:
            if u == student.token:
                student.socketId = users[u].socketId
                return

    def sendStudentsList(self, admin, students):
        self.mediator.call(self.EVENTS['GET_STUDENTS_LIST'], {
            'admin': admin,
            'students': students
        })

    # Отметить студента data = { tokenAdmin, tokenStudent }
    def noteStudent(self, data):
        tokenAdmin = data['tokenAdmin']
        tokenStudent = data['tokenStudent']
        admin = Student(self.db.getStudentByToken(tokenAdmin))
        self.normalizeStudent(admin)
        if admin and (admin.type == 1 or admin.type == 2):
            student = Student(self.db.getStudentByToken(tokenStudent))
            self.normalizeStudent(student)
            if student and (student.groupId == admin.groupId):
                lesson = self.db.getCurrentLesson()
                if lesson:
                    isStudentHere = self.db.getStudentOnLesson(student.id, lesson['id'])  # Смотрим, отметился ли уже этот студент на этой пару
                    if not isStudentHere:
                        self.db.noteStudent(admin.id, student.id, lesson['id'])  # Отметить студента
                        # получить список студентов на этой паре
                        students = self.db.getStudentsOnLesson(
                            admin.groupId,
                            datetime.today().strftime('%Y-%m-%d'),
                            lesson['id']
                        )
                        # послать обновленный список студентов старосте/админу
                        thread = threading.Thread(target=self.sendStudentsList, args=(admin, students))
                        thread.start()
                        return True
        return False

    # Получить студентов, пришедших на пару data = { tokenAdmin, date, lessonNum }
    def getStudentsOnLesson(self, data):
        tokenAdmin = data['tokenAdmin']
        date = data['date']
        lessonNum = data['lessonNum']
        admin = Student(self.db.getStudentByToken(tokenAdmin))
        if admin and (admin.type == 1 or admin.type == 2):
            lesson = self.db.getLessonByNum(lessonNum)
            if lesson:
                return self.db.getStudentsOnLesson(admin.groupId, date, lesson['id'])
        return False

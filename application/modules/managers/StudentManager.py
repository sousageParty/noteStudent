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

    # Отметить студента data = { tokenAdmin, tokenStudent }
    def noteStudent(self, data):
        tokenAdmin = data['tokenAdmin']
        tokenStudent = data['tokenStudent']
        admin = Student(self.db.getStudentByToken(tokenAdmin))
        if admin and (admin.type == 1 or admin.type == 2):
            student = Student(self.db.getStudentByToken(tokenStudent))
            if student and (student.groupId == admin.groupId):
                lesson = self.db.getCurrentLesson()
                if lesson:
                    isStudentHere = self.db.getStudentOnLesson(student.id, lesson['id'])  # Смотрим, отметился ли уже этот студент на этой пару
                    if not isStudentHere:
                        return self.db.noteStudent(admin.id, student.id, lesson['id'])
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

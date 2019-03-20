from .BaseManager import BaseManager


# Класс для описания методов для работы со студентами
class StudentManager(BaseManager):

    def __init__(self, params):
        super().__init__(params)
        self.mediator.set(self.TRIGGERS['SET_STUDENT'], self.setStudent)

    # Добавить студента data = {userId, group, type}
    def setStudent(self, data):
        return self.db.addStudent(data)

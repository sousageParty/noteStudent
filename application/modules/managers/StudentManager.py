from .BaseManager import BaseManager


class StudentManager(BaseManager):

    def __init__(self, params):
        super().__init__(params)
        self.mediator.set(self.TRIGGERS['SET_STUDENT'], self.setStudent)

    def setStudent(self, data):
        return self.db.addStudent(data)

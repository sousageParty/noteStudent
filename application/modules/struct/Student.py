from .User import User


class Student(User):

    studentId = None
    groupId = None
    name = None
    surname = None
    thirdname = None
    type = None

    def __init__(self, params):
        super().__init__(params)
        self.studentId = params['student_id']
        self.groupId = params['group_id']
        self.name = params['name']
        self.surname = params['surname']
        self.thirdname = params['thirdname']
        self.type = params['type']

    def get(self):
        return {'id': self.id, 'studentId': self.studentId, 'groupId': self.groupId,
                'login': self.login, 'password': self.password, 'token': self.token,
                'name': self.name, 'surname': self.surname, 'thirdname': self.thirdname, 'type': self.type}

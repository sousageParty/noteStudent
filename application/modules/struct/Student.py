from .User import User


# Описание структуры данных Студент
class Student(User):

    studentId = None
    groupId = None
    type = None

    def __init__(self, params):
        super().__init__(params)
        self.studentId = params['student_id']
        self.groupId = params['group_id']
        self.type = params['type']

    # Сериализация класса в объект
    def get(self):
        return {'id': self.id, 'studentId': self.studentId, 'groupId': self.groupId,
                'login': self.login, 'password': self.password, 'token': self.token,
                'name': self.name, 'type': self.type}

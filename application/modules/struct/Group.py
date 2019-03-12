class Group:

    id = None
    name = None
    shortName = None
    code = None
    students = None

    def __init__(self, params):
        self.id = params['id']
        self.name = params['name']
        self.shortName = params['short_name']
        self.code = params['code']
        self.students = params['students']

    def get(self):
        return {'id': self.id, 'shortName': self.shortName,
                'name': self.name, 'code': self.code, 'students': self.students}

# В базе данных приложения используются 6 триггеров:
# 1. check_student_on_lesson - проверка на то, чтобы при добавлении одной записи студент и админ были из одной группы
# 2. check_student_on_lesson_update - проверка на то, чтобы при изменении одной записи студент и админ были из одной группы
# 3. check_admin_student_on_lesson - проверка на то, чтобы при добавлении одной записи админ являлся админом (тип 1 или 2)
# 4. check_admin_student_on_lessonupdate - проверка на то, чтобы при изменении одной записи админ являлся админом (тип 1 или 2)
# 3. check_student - проверка на то, чтобы при добавлении одной записи админа в заданной группе еще нет
# 4. check_student - проверка на то, чтобы при изменении одной записи админа в заданной группе еще нет
SETTINGS = {

    'DB': {
        'PATH': 'application/modules/db/projectDB.db'
    },

    'MEDIATOR': {
        'EVENTS': {
        },
        'TRIGGERS': {
            # О юзерах
            'GET_USERS': 'GET_USERS',
            'GET_USER': 'GET_USER',
            'SET_USER': 'SET_USER',
            'LOGIN': 'LOGIN',
            'LOGOUT': 'LOGOUT',
            # О студентах
            'SET_STUDENT': 'SET_STUDENT',
            # О группах
            'GET_GROUPS_CODES': 'GET_GROUPS_CODES',
        }
    }
}

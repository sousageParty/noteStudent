# В базе данных приложения используются 6 триггеров:
# 1. check_student_on_lesson - проверка на то, чтобы при добавлении одной записи студент и админ были из одной группы
# 2. check_student_on_lesson_update - проверка на то, чтобы при изменении одной записи студент и админ были из одной группы
# 3. check_admin_student_on_lesson - проверка на то, чтобы при добавлении одной записи админ являлся админом (тип 1 или 2)
# 4. check_admin_student_on_lesson_update - проверка на то, чтобы при изменении одной записи админ являлся админом (тип 1 или 2)
# 3. check_student - проверка на то, чтобы при добавлении одной записи админа в заданной группе еще нет
# 4. check_student - проверка на то, чтобы при изменении одной записи админа в заданной группе еще нет
SETTINGS = {

    'DB': {
        'PATH': 'application/modules/db/projectDB.db'
    },

    'MEDIATOR': {
        'EVENTS': {
            'GET_STUDENTS_LIST': 'GET_STUDENTS_LIST'  # отправить старосте список студентов на паре
        },
        'TRIGGERS': {
            # О юзерах
            'GET_USERS': 'GET_USERS',
            'GET_ACTIVE_USERS': 'GET_ACTIVE_USERS',
            'GET_USER': 'GET_USER',
            'SET_USER': 'SET_USER',
            'UPDATE_PASSWORD': 'UPDATE_PASSWORD',
            'GET_USER_TYPE_BY_TOKEN': 'GET_USER_TYPE_BY_TOKEN',
            'LOGIN': 'LOGIN',
            'LOGOUT': 'LOGOUT',
            # О студентах
            'SET_STUDENT': 'SET_STUDENT',
            'NOTE_STUDENT': 'NOTE_STUDENT',
            'GET_STUDENTS_ON_LESSON': 'GET_STUDENTS_ON_LESSON',
            # О группах
            'GET_GROUPS_CODES': 'GET_GROUPS_CODES',
        }
    },
    # О сокетах
    'SOCKET_EVENTS': {
        'START_CONNECTION': 'START_CONNECTION',
        'SEND_MESSAGE': 'SEND_MESSAGE',
        'SEND_MESSAGE_TO_ALL': 'SEND_MESSAGE_TO_ALL',
        'GET_STUDENTS_LIST': 'GET_STUDENTS_LIST',
        'LOGOUT_CHAT': 'LOGOUT_CHAT',
    }
}

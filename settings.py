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

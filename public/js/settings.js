/**
 * Важные настройки клиента
 */
const SETTINGS = {

    PAGES: {
        LOGIN: 'login',
        REGISTRATION: 'registration',
        MAIN: 'main'
    },

    URL: `${window.location.protocol}//${window.location.hostname}:${window.location.port}/api/`,

    SOCKET_EVENTS: {
        START_CONNECTION: 'START_CONNECTION',
        TEST_MESSAGE: 'TEST_MESSAGE',
        SEND_MESSAGE: 'SEND_MESSAGE', // сообщение с клиента на сервер
        SEND_MESSAGE_TO_ALL: 'SEND_MESSAGE_TO_ALL', // отправить сообщение с сервера всем клиентам
        GET_STUDENTS_LIST: 'GET_STUDENTS_LIST',
    },

    MEDIATOR: {
        EVENTS: {
            ADMIN_LOGIN: 'ADMIN_LOGIN',
            FILL_ADMIN_TABLE: 'FILL_ADMIN_TABLE',
            SET_SOCKET: 'SET_SOCKET',
        },
        TRIGGERS: {
        }
    }

};
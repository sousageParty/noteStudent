/**
 * Конструктор для инкапсуляции логики входа в систему
 * @param options параметры с которыми вызывается конструктор
 */

function Login(options) {

    options = options instanceof Object ? options : {};

    const $SELECTORS = options.$SELECTORS;
    const PAGES = options.PAGES;
    const showPage = options.showPage instanceof Function ? options.showPage : () => {};
    const SOCKET_EVENTS = options.SOCKET_EVENTS;

    const server = options.server;
    const socket = options.socket;

    /**
     * Заполняем выпадашку с группами
     * @param groups массив групп, которыми нужно заполнить выпадашку
     */
    function fillGroups(groups) {
        const select = $('.auth-reg-block__select-js');
        select.empty();
        for (let group of groups) {
            select.append(`<option class="auth-reg-block__select-elem">${group.code}</option>`);
        }
    }

    /**
     * Функция входа в сиситему
     * @param e событие клика на кнопку
     */
    async function login(e) {
        const loginField = $('.auth-reg-block__input-login-js');
        const passwordField = $('.auth-reg-block__input-password-js');
        const login = loginField.val();
        let password = passwordField.val();
        if (login && password) {
            const rnd = Math.random();
            password = md5(md5(login + password) + rnd);
            const result = await server.login({login, password, rnd});
            if (result.result === 'ok') {
                server.token = result.data;
                loginField.val('');
                passwordField.val('');
                showPage(PAGES.MAIN);
                return;
            }
            $('.auth-reg-block__error-login-js').empty().append(result.error);
            return;
        }
        $('.auth-reg-block__error-login-js').empty().append("Не введен логин и(или) пароль!");
    }

    /**
     * Функция-обработчик всех событий, касающихся Login-а
     */
    function eventHandler() {
        $('.auth-reg-block__button-login-js').on('click', login);

        /**
         * Вешаем событие на кнопку "перейти к регистрации" и обрабатываем его
         */
        $SELECTORS.toRegBtn.on('click', async e => {
            const result = await server.getGroupsCodes();
            fillGroups(result.data);
            showPage(PAGES.REGISTRATION)
        });
    }

    /**
     * Функция-инициализатор компонента
     */
    function init() {
        eventHandler();
        $('#testMessage').on('click', event => {
            socket.emit(SOCKET_EVENTS.TEST_MESSAGE, {});
        });
        socket.on(SOCKET_EVENTS.TEST_MESSAGE, data => console.log(data));
    }
    init();
}
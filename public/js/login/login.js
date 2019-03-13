function Login(options) {

    options = options instanceof Object ? options : {};

    const $SELECTORS = options.$SELECTORS;
    const PAGES = options.PAGES;
    const showPage = options.showPage instanceof Function ? options.showPage : () => {};

    const server = options.server;

    function fillGroups(groups) {
        const select = $('.auth-reg-block__select-js');
        select.empty();
        for (let group of groups) {
            select.append(`<option class="auth-reg-block__select-elem">${group.code}</option>`);
        }
    }

    //Функция логина
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

    //Вешаем все события, касающиеся логина здесь
    function eventHandler() {
        $('.auth-reg-block__button-login-js').on('click', login);

        $SELECTORS.toRegBtn.on('click', async e => {
            const result = await server.getGroupsCodes();
            fillGroups(result.data);
            showPage(PAGES.REGISTRATION)
        });
    }

    function init() {
        eventHandler();
    }
    init();
}
/**
 * Конструктор для инкапсуляции логики смены пароля
 * @param options параметры с которыми вызывается конструктор
 */
function UpdatePassword(options) {

    options = options instanceof Object ? options : {};

    const $SELECTORS = options.$SELECTORS;
    const PAGES = options.PAGES;
    const showPage = options.showPage instanceof Function ? options.showPage : () => {};
    const SOCKET_EVENTS = options.SOCKET_EVENTS;

    const mediator = options.mediator;
    const EVENTS = mediator.EVENTS;
    const TRIGGERS = mediator.TRIGGERS;

    const server = options.server;
    const socket = options.socket;
    /**
     * Функция смены пароля
     * @param e событие нажатия на кнопку
     */
    async function updatePassword(e) {
        const loginField = $('.auth-reg-block__upd-pas__input-login-js');
        const passwordField = $('.auth-reg-block__upd-pas__input-password-js');
        const login = loginField.val();
        let password = $(passwordField[0]).val();
        const newPassword1 = $(passwordField[1]).val();
        const newPassword2 = $(passwordField[2]).val();
        if (login && password && newPassword1 && newPassword2) {
            const rnd = Math.random();
            password = md5(md5(login + password) + rnd);
            const result = await server.login({login, password, rnd});
            if (result.result === 'ok') {
                if (newPassword1 === newPassword2) {
                    newPassword = md5(login + newPassword1);
                    const result = await server.updatePassword({ login, newPassword});
                    if (result.result === "ok") {
                        loginField.val('');
                        passwordField.val('');
                        $('.auth-reg-block__error-upd-pas-js').empty();
                        showPage(PAGES.LOGIN);
                        return;
                    }
                    $('.auth-reg-block__error-upd-pas-js').empty().append("Какая-то лажа, пароль не обновился");
                    return;
                }
                $('.auth-reg-block__error-upd-pas-js').empty().append("Пароли не совпадают");
                return;
            }
            $('.auth-reg-block__error-upd-pas-js').empty().append("Неверный пароль");
            return;
        }
        $('.auth-reg-block__error-upd-pas-js').empty().append("Введены не все значения");
        return;
    }
    /**
     * Метод-обработчик всех событий, касательно регистрации
     */
    function eventHandler() {
        $('.auth-reg-block__upd-pas__button-js').on('click', updatePassword);
        $SELECTORS.toLoginBtn.on('click', e => {
            $('.auth-reg-block__error-upd-pas-js').empty();
            showPage(PAGES.LOGIN);
        });
    }

   /**
     * Функция-инициализатор компонента
     */
    function init () {
        eventHandler();
    }
    init();
}

function Registration(options) {

    options = options instanceof Object ? options : {};

    const $SELECTORS = options.$SELECTORS;
    const PAGES = options.PAGES;
    const showPage = options.showPage instanceof Function ? options.showPage : () => {};

    const server = options.server;

    //Разбиваем строку с ФИО, на массив с как минимум двумя элементами
    function normalizeName(nameField) {
        const longName = nameField.val();
        return (longName && longName.length >= 2) ? longName.split(" ") : [];
    }

    //Функция регистрации
    async function registration(e) {
        const loginField = $('.auth-reg-block__reg__input-login-js');
        const nameField = $('.auth-reg-block__reg__input-name-js');
        const passwordField = $('.auth-reg-block__reg__input-password-js');
        const login = loginField.val();
        const longName = normalizeName(nameField);
        const password1 = $(passwordField[0]).val();
        const password2 = $(passwordField[1]).val();
        const group = $('.auth-reg-block__select-js').val();
        if (login && password1 && password2 && longName && longName.length >= 2 && group) {
            if (password1 === password2) {
                const surname = longName[0];
                const name = longName[1];
                const thirdname = longName[2];
                const result = await server.registration({ login, password: password1, group, name, surname, thirdname, type: 0 });
                if (result.result === "ok") {
                    loginField.val('');
                    nameField.val('');
                    passwordField.val('');
                    showPage(PAGES.LOGIN);
                    return;
                }
                $('.auth-reg-block__error-reg-js').empty().append(result.error);
                return;
            }
            $('.auth-reg-block__error-reg-js').empty().append("Пароли не совпадают");
            return;
        }
        $('.auth-reg-block__error-reg-js').empty().append("Введены не все данные");
    }

    //Вешаем все события, касающиеся регистрации здесь
    function eventHandler() {
        $('.auth-reg-block__reg__button-js').on('click', registration);
        $SELECTORS.toLoginBtn.on('click', e => showPage(PAGES.LOGIN));
    }

    function init () {
        eventHandler();
    }
    init();

}
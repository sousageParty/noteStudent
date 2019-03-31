/**
 * Основной компонент клиента приложения.
 * Отправная точка
 */
$(document).ready(function () {

    const PAGES = SETTINGS.PAGES;

    //Константа со всеми базовыми селекторами
    const $SELECTORS = {
        'loginBlock': $('.auth-reg-block__auth'), 'regBlock': $('.auth-reg-block__reg'), 'mainBlock': $('.main-block'),
        'toLoginBtn': $('#go-to-auth-button'), 'toRegBtn': $('#go-to-reg-button'), 'loginRegContainer': $('.auth-reg-block')
    };

    /**
     * Метод показывающий нужную страницу по запросу
     * @param page страница, которую нужно показать
     */
    function showPage(page) {
        $SELECTORS.mainBlock.hide();
        $SELECTORS.regBlock.hide();
        $SELECTORS.loginBlock.hide();
        $SELECTORS.toRegBtn.hide();
        $SELECTORS.toLoginBtn.hide();
        $SELECTORS.loginRegContainer.hide();
        switch (page) {
            case PAGES.LOGIN:
                $SELECTORS.loginRegContainer.css('display', 'flex');
                $SELECTORS.loginBlock.css('display', 'flex');
                $SELECTORS.toRegBtn.show();
                break;
            case PAGES.REGISTRATION:
                $SELECTORS.loginRegContainer.css('display', 'flex');
                $SELECTORS.regBlock.css('display', 'flex');
                $SELECTORS.toLoginBtn.show();
                break;
            case PAGES.MAIN:
                $SELECTORS.mainBlock.show();
                break;
        }
    }

    const mediator = new Mediator({ ...SETTINGS.MEDIATOR });
    const server = new Server({ ...SETTINGS });
    const socket = new Socket(SETTINGS.SOCKET_EVENTS);
    new Registration({ ...SETTINGS, $SELECTORS, showPage, server });
    new Login({ ...SETTINGS, $SELECTORS, showPage, server, socket, mediator });
    new MainManager({ ...SETTINGS, $SELECTORS, showPage, server, socket, mediator });

    showPage(PAGES.LOGIN);
});
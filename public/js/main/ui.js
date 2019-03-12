function UI(options) {

    options = options instanceof Object ? options : {};

    const $SELECTORS = options.$SELECTORS;
    const PAGES = options.PAGES;
    const showPage = options.showPage instanceof Function ? options.showPage : () => {};
    const server = options.server;

    //Вешаем все события, касающиеся основного экрана здесь
    function eventHandler() {
        $('.main-block__logout-button-js').on('click', async e => {
            const result = await server.logout();
            if (result.result === "ok") {
                showPage(PAGES.LOGIN);
            }
        });
    }

    function init() {
        eventHandler();
    }
    init()


}
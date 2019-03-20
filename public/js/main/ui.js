/**
 * Конструктор для инкапсуляции основных событий клиента приложения
 * @param options параметры с которыми вызывается конструктор
 */
function UI(options) {

    options = options instanceof Object ? options : {};

    const $SELECTORS = options.$SELECTORS;
    const PAGES = options.PAGES;
    const showPage = options.showPage instanceof Function ? options.showPage : () => {};
    const server = options.server;

    /**
     * Функция-обработчик основных событий клиента
     */
    function eventHandler() {
        $('.main-block__logout-button-js').on('click', async e => {
            const result = await server.logout();
            if (result.result === "ok") {
                showPage(PAGES.LOGIN);
            }
        });
    }

    /**
     * Функция-инициализатор компонента
     */
    function init() {
        eventHandler();
    }
    init()


}
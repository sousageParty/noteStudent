/**
 * Конструктор для инкапсуляции основной логики клиента приложения
 * @param options параметры с которыми вызывается конструктор
 */
function MainManager(options) {

    options = options instanceof Object ? options : {};

    const $SELECTORS = options.$SELECTORS;
    const PAGES = options.PAGES;
    const showPage = options.showPage instanceof Function ? options.showPage : () => {};
    const server = options.server;

    const ui = new UI(options);

}
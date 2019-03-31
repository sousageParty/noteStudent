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

    const mediator = options.mediator;
    const EVENTS = mediator.EVENTS;
    const TRIGGERS = mediator.TRIGGERS;

    $SELECTORS.DATE = $('.main-block_date-js');
    $SELECTORS.SELECT = $('.main-block_select-js');
    $SELECTORS.LIST_BTN = $('.main-block_list-btn-js');

    /**
     * Функция-обработчик основных событий клиента
     */
    function baseEventHandler() {
        $('.main-block__logout-button-js').off('click').on('click', async e => {
            const result = await server.logout();
            if (result.result === "ok") {
                showPage(PAGES.LOGIN);
            }
        });
    }

    /**
     * Функция-обработчик всех событий админа
     */
    this.adminEventHandler = () => {
        $SELECTORS.LIST_BTN.off('click').on('click', async e => {
            let date = $SELECTORS.DATE.val();
            let lessonNum = $SELECTORS.SELECT.val();
            const data = { date, lessonNum };
            const answer = await server.getStudentsOnLesson(data);
            if (answer.result === "ok") {
                mediator.call(EVENTS.FILL_ADMIN_TABLE, answer.data);
            }
        });
    };

    /**
     * Функция-инициализатор компонента
     */
    function init() {
        baseEventHandler();
    }
    init()


}
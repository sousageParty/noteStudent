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
    let socket = null;

    const mediator = options.mediator;
    const EVENTS = mediator.EVENTS;
    const TRIGGERS = mediator.TRIGGERS;

    let ui = null;

    function showAdminInterface() {
        $('.main-block__content-admin').css('display', 'flex');
        ui.adminEventHandler(true);
    }

    function hideAdminInterface() {
        $('.main-block__content-admin').hide();
        ui.adminEventHandler(false);
    }

    /**
     * Проверяем админ ли залогинился
     * @returns {Promise<void>}
     */
    async function isAdminLogin() {
        const answer = await server.getUserType();
        if (answer.result === "ok") {
            let userType = answer.data.type;
            if (userType !== 0) {
                showAdminInterface();
            } else {
                hideAdminInterface();
            }
        }
    }

    /**
     * Высчитываем время опоздания
     * @param timeArrive время прибытия на пару
     * @param timeStart время начала пары
     * @returns {string|null}
     */
    function getLateTime(timeArrive, timeStart) {
        if (timeArrive > timeStart) {
            let timeA = timeArrive.split(":");
            let timeS = timeStart.split(":");
            let hours = '00';
            let mins = Math.abs(timeA[1] - timeS[1]);
            if (timeA[0] !== timeS[0]) {
                hours = Math.abs(timeA[0] - timeS[0]);
            }
            return `${hours < 10 ? '0' + hours : hours}:${mins < 10 ? '0' + mins : mins}`;
        }
        return null;
    }

    /**
     * Заполняем таблицу со студентами для админа
     * @param students
     */
    function fillAdminTable(_students) {
        console.log(_students);
        const students = _students instanceof Array ? _students : _students.students;
        const tableBody = $('.main-block__table-body-js');
        tableBody.empty();
        let tr;
        for (let student of students) {
            student.time = [student.time.split(":")[0], student.time.split(":")[1]].join(":");
            tr = "<tr>" +
                `<td>${student.name}</td><td>${student.shortName}</td><td>${student.time}</td>` +
                `<td>${getLateTime(student.time, student.timeStart)}</td><td>${student.timeStart}</td><td>${student.timeFinish}</td>` +
                `<td>${student.date}</td></tr>`;
            tableBody.append(tr);
        }
    }

    function init() {
        mediator.subscribe(EVENTS.ADMIN_LOGIN, isAdminLogin);
        mediator.subscribe(EVENTS.FILL_ADMIN_TABLE, fillAdminTable);
        mediator.subscribe(EVENTS.SET_SOCKET, s => {
            socket = null;
            socket = s;
            new Chat({...SETTINGS, socket});
            ui = new UI({...options, ...{socket}});
            socket.on(SETTINGS.SOCKET_EVENTS.GET_STUDENTS_LIST, fillAdminTable);
        });
    }
    init();
}



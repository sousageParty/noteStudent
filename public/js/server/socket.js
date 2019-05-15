class Socket {

    id = null;
    socket = null;
    messages = {};
    SOCKET_EVENTS = {};

    constructor(events) {
        this.SOCKET_EVENTS = events;
        this.initSocket();
        this.socket.onmessage = event => this.getMessage(
                (event && event.data) ?
                    eval('(function () { return ' + event.data + ' })()') :
                    null);
        this.socket.onopen = () => this.emit(this.SOCKET_EVENTS.START_CONNECTION, { id: this.id , token: localStorage.getItem('token')});
        this.socket.onclose = () => this.initSocket();
        this.socket.onerror = error => console.log(error);
    }

    // послать сообщение на сервер
    emit(idMessage, message) {
        message = (message instanceof Object) ? message : {};
        message.id = this.id;
        message.id_message = idMessage;
        this.socket.send(JSON.stringify(message));
    }

    // повесить слушатель обработки события
    on(idMessage, cb) {
        if (!this.messages[idMessage]) {
            this.messages[idMessage] = cb;
        } else {
            throw new Error("Handler for this message already exists!!!");
        }
    }

    // получать сообщение с сервера
    getMessage(message) {
        if (message &&
            message.id_message &&
            this.messages[message.id_message] instanceof Function) {
            this.messages[message.id_message](message);
        }
    }

    initSocket() {
        this.id = md5('Marat ' + Date.now());
        try {
            this.socket = new WebSocket('ws://' + window.location.host + '/ws');
        } catch (e) {
            this.socket = new WebSocket('wss://' + window.location.host + '/ws');
        }
    }
}
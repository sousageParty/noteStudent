class Chat {

    sendMessageBtn = $('#sendMessage');
    message = $('#message');
    chatBlock = $('#chat');

    constructor(options) {
        this.socket = options.socket;
        this.EVENT = options.SOCKET_EVENTS;
        this.sendMessageBtn.off('click').on("click",() => this.sendMessage());
        this.socket.on(this.EVENT.SEND_MESSAGE_TO_ALL, data => this.getMessage(data));
    }

    sendMessage() {
        let text = this.message.val();
        if (text) {
            this.socket.emit(this.EVENT.SEND_MESSAGE, { text });
            this.message.val('')
        }
    }

    getMessage(data) {
        let text = document.createElement("p");
        text.innerHTML = `<b>${data['name']}:</b> ${data['text']}`;
        this.chatBlock.prepend(text);
    }
}


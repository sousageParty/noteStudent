class Server {

    constructor(options) {
        this.options = options instanceof Object ? options : {};
        this.url = options.URL;
        this.token = null;
    }

    //Выполнить любой GET-запрос
    executeGet(data) {
        return new Promise(resolve => {
            $.ajax({
                url: this.url + data.url,
                data,
                method: 'GET',
                dataType: 'json',
                success: data => resolve(data)
            })
        });
    }

    //Выполнить любой POST-запрос
    executePost(data) {
        return new Promise(resolve => {
            $.ajax({
                url: this.url + data.url,
                data: JSON.stringify(data),
                method: 'POST',
                dataType: 'json',
                success: data => resolve(data)
            })
        });
    }

    login(data = {}) {
        data.url = `user/login/${data.login}/${data.password}`;
        return this.executeGet(data);
    }

    logout(data = {}) {
        data.url = `user/logout/${this.token}`;
        return this.executeGet(data);
    }

    registration(data = {}) {
        data.url = 'user';
        return this.executePost(data);
    }

    getGroupsCodes(data = {}) {
        data.url = 'group/codes';
        return this.executeGet(data);
    }
}
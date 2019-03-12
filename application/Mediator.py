class Mediator:
    TYPES = {}  # типы событий
    events = {}  # списки событий
    TRIGGER_TYPES = {}  # типы событий
    triggers = {}  # список триггеров

    def __init__(self, types):
        self.TYPES = types['EVENTS']
        self.TRIGGER_TYPES = types['TRIGGERS']
        for key in self.TYPES.keys():
            self.events.update({self.TYPES[key]: []})
        for key in self.TRIGGER_TYPES.keys():
            self.triggers.update({self.TRIGGER_TYPES[key]: lambda x=None: None})

    def __del__(self):
        self.events.clear()

    # подписка на события
    def subscribe(self, name, func):
        if name and func:
            self.events.get(name).append(func)

    def getTypes(self):
        return self.TYPES

    # выозов события
    def call(self, name, data=None):
        if name:
            cbs = self.events.get(name)
            if cbs:
                for cb in cbs:
                    cb(data)

    def getTriggerTypes(self):
        return self.TRIGGER_TYPES

    # Установить Триггер
    def set(self, name, func):
        if name and func:
            self.triggers[name] = func

    # Вызвать триггер
    def get(self, name, data=None):
        if name:
            return self.triggers.get(name)(data)

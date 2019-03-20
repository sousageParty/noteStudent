from .BaseManager import BaseManager


# Класс для описания методов для работы с группами
class GroupManager(BaseManager):

    def __init__(self, params):
        super().__init__(params)
        self.mediator.set(self.TRIGGERS['GET_GROUPS_CODES'], self.getGroupsCodes)

    # Вернуть коды всех групп
    def getGroupsCodes(self, data):
        return self.db.getGroupsCodes()

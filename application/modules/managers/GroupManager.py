from .BaseManager import BaseManager


class GroupManager(BaseManager):

    def __init__(self, params):
        super().__init__(params)
        self.mediator.set(self.TRIGGERS['GET_GROUPS_CODES'], self.getGroupsCodes)

    def getGroupsCodes(self, data):
        return self.db.getGroupsCodes()

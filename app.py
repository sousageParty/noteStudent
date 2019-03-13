from aiohttp import web
from settings import SETTINGS

from application.Mediator import Mediator
from application.modules.db.DB import DB
from application.modules.managers.UserManager import UserManager
from application.modules.managers.StudentManager import StudentManager
from application.modules.managers.GroupManager import GroupManager
from application.router.Router import Router

mediator = Mediator(SETTINGS['MEDIATOR'])
db = DB(SETTINGS['DB'])

UserManager({'mediator': mediator, 'db': db})
StudentManager({'mediator': mediator, 'db': db})
GroupManager({'mediator': mediator, 'db': db})

# Users in DB (login <=> password):
# vasya <=> 123
# petya <=> 321
# ivan <=> 213
# katya <=> 1234

app = web.Application()
Router(app, web, mediator)
web.run_app(app)

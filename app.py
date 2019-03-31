from aiohttp import web
from settings import SETTINGS

from application.Mediator import Mediator
from application.modules.db.DB import DB
from application.modules.managers.UserManager import UserManager
from application.modules.managers.WSManager import WSManager
from application.modules.managers.StudentManager import StudentManager
from application.modules.managers.GroupManager import GroupManager
from application.router.Router import Router
from application.router.WebSocket import WebSocket

mediator = Mediator(SETTINGS['MEDIATOR'])
socket = WebSocket(web, mediator)
db = DB(SETTINGS['DB'])

WSManager({'mediator': mediator, 'db': db, 'socket': socket, 'SOCKET_EVENTS': SETTINGS['SOCKET_EVENTS']})
UserManager({'mediator': mediator, 'db': db, 'socket': socket, 'SOCKET_EVENTS': SETTINGS['SOCKET_EVENTS']})
StudentManager({'mediator': mediator, 'db': db, 'socket': socket, 'SOCKET_EVENTS': SETTINGS['SOCKET_EVENTS']})
GroupManager({'mediator': mediator, 'db': db, 'socket': socket, 'SOCKET_EVENTS': SETTINGS['SOCKET_EVENTS']})

# Users in DB (login <=> password):
# vasya <=> 123
# petya <=> 321
# ivan <=> 213
# katya <=> 1234

app = web.Application()
Router(app, web, mediator, socket)
web.run_app(app)

from aiohttp import web
from settings import config
from routes import setup_routes

app = web.Application()
app['config'] = config
setup_routes(app)
web.run_app(app)

from aiohttp import web
from settings import config
from routes import setup_routes
import logging

stdio_handler = logging.StreamHandler()
stdio_handler.setLevel(logging.INFO)
_logger = logging.getLogger('aiohttp.access')
_logger.addHandler(stdio_handler)
_logger.setLevel(logging.DEBUG)

app = web.Application(logger=_logger)
app['config'] = config
setup_routes(app)
web.run_app(app)

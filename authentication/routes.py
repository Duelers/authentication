from views import signin


def setup_routes(app):
    app.router.add_post('/public/v1/signin/', signin)

from flask import Flask

def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # import blueprints
    from landing.views import landing_app

    # register blueprints
    app.register_blueprint(landing_app)

    return app

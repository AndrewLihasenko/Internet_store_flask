from datetime import timedelta
from flask import Flask, app

from stores import name_bp
from config import run_config
from create_db import create_db
from db import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    migrate.init_app(app, db)
    app.permanent_session_lifetime = timedelta(minutes=20)

    app.register_blueprint(create_db)
    app.register_blueprint(name_bp)

    return app

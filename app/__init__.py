from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


db = SQLAlchemy()

login_manager = LoginManager()


def create_app():

    app = Flask(__name__)

    app.config.from_object(
        "app.config.Config"
    )


    db.init_app(
        app
    )


    login_manager.init_app(
        app
    )


    from app.models.user import User


    @login_manager.user_loader
    def load_user(
        user_id
    ):

        return User.query.get(
            int(user_id)
        )


    from app.routes.auth_routes import auth_bp

    from app.routes.admin import admin_bp

    from app.routes.user_routes import user_bp


    app.register_blueprint(
        auth_bp
    )

    app.register_blueprint(
        admin_bp
    )

    app.register_blueprint(
        user_bp
    )


    return app
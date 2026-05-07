from app import create_app

from app import db


from app.models.user import User

from app.models.retiree import Retiree


app = create_app()


with app.app_context():

    db.create_all()

    print(
        "tables created"
    )
from app import create_app
from app import db

from app.models.user import User
from app.models.retiree import Retiree


app = create_app()


with app.app_context():

    db.create_all()

    admin = User.query.filter_by(
        username="admin"
    ).first()


    if not admin:

        admin = User(
            username="admin",
            role="admin"
        )

        admin.set_password(
            "admin123"
        )

        db.session.add(
            admin
        )

        db.session.commit()


if __name__ == "__main__":

    app.run(
        debug=True
    )
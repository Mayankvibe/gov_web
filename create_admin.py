from app import create_app

from app import db

from app.models.user import User


app = create_app()


with app.app_context():

    admin = User.query.filter_by(

        username="admin"

    ).first()


    if admin:

        print(
            "ADMIN ALREADY EXISTS"
        )


    else:

        admin = User(

            username="admin",

            role="admin"
        )


        admin.set_password(

            "1234"
        )


        db.session.add(

            admin
        )


        db.session.commit()


        print(
            "ADMIN CREATED"
        )
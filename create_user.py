from app import create_app

from app import db

from app.models.user import User


app = create_app()


with app.app_context():

    user = User.query.filter_by(

        username="user"

    ).first()


    if user:

        print(
            "USER पहले से मौजूद है"
        )


    else:

        user = User(

            username="user",

            role="user"
        )


        user.set_password(

            "1234"
        )


        db.session.add(

            user
        )


        db.session.commit()


        print(
            "USER बन गया"
        )
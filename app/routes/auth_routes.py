from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)

from flask_login import (
    login_user
)

from app.models.user import User


auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route(
    "/",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form.get(
            "username"
        ).strip()

        password = request.form.get(
            "password"
        )

        role = request.form.get(
            "role"
        )


        user = User.query.filter_by(

            username=username

        ).first()


        if (

            user and

            user.role == role and

            user.check_password(
                password
            )

        ):

            login_user(
                user
            )


            if role == "admin":

                return redirect(
                    "/admin/dashboard"
                )


            return redirect(
                "/user/add"
            )


        return render_template(

            "login.html",

            error="गलत जानकारी"
        )


    return render_template(

        "login.html"
    )
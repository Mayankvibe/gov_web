from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)

from app import db

from app.models.retiree import (
    Retiree
)


user_bp = Blueprint(
    "user",
    __name__
)


@user_bp.route(
    "/user/add",
    methods=[
        "GET",
        "POST"
    ]
)
def add_employee():

    if request.method == "POST":

        employee = Retiree(

            employee_name=request.form.get(
                "employee_name"
            ),

            designation=request.form.get(
                "designation"
            ),

            ddo_info=request.form.get(
                "ddo_info"
            ),

            retirement_date=request.form.get(
                "retirement_date"
            ),
            employe_code=request.form.get(
                "employe_code"
            )
        )

        db.session.add(
            employee
        )

        db.session.commit()

        return redirect(
            "/user/add"
        )

    return render_template(
        "user/add_employee.html"
    )
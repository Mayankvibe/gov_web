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


admin_bp = Blueprint(
    "admin",
    __name__
)


# Dashboard


@admin_bp.route(
    "/admin/dashboard"
)
def dashboard():

    search = request.args.get(
        "search",
        ""
    )

    date = request.args.get(
        "date",
        ""
    )


    query = Retiree.query


    if search:

        query = query.filter(
            Retiree.employee_name.ilike(
                f"%{search}%"
            )
        )


    if date:

        query = query.filter(
            Retiree.retirement_date == date
        )


    employees = query.all()


    return render_template(

        "admin/dashboard.html",

        employees=employees
    )


# Checkbox Update


@admin_bp.route(
    "/admin/update/<int:employee_id>",
    methods=["POST"]
)
def update_employee(

    employee_id
):

    employee = Retiree.query.get_or_404(

        employee_id
    )


    employee.pension = (

        "pension" in request.form
    )

    employee.upadhan = (

        "upadhan" in request.form
    )

    employee.jpf = (

        "jpf" in request.form
    )

    employee.nakdikaran_avkas = (

        "nakdikaran_avkas" in request.form
    )

    

    employee.life_insurance = (

        "life_insurance"
        in request.form
    )


    db.session.commit()


    return redirect(

        "/admin/dashboard"
    )
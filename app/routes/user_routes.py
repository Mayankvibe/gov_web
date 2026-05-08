from flask import (

    Blueprint,

    render_template,

    request,

    redirect
)


from flask_login import (

    login_required,

    current_user
)


from app import db

from app.models.retiree import Retiree


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

@login_required
def add_employee():


    if request.method == "POST":


        employee = Retiree(


            user_id=current_user.id,


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


            pension=False,

upadhan=False,


jpf="jpf" in request.form,


nakdikaran_avkas=

    "nakdikaran_avkas"

    in request.form,


life_insurance=

    "life_insurance"

    in request.form
        )


        db.session.add(

            employee
        )


        db.session.commit()


        return redirect(

            "/user/add"
        )



    employees = Retiree.query.filter_by(

        user_id=current_user.id

    ).all()



    return render_template(

        "user/add_employee.html",

        employees=employees
    )
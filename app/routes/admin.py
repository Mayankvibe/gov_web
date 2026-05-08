from flask import (

    Blueprint,

    render_template
)


from flask_login import (

    login_required
)


from app.models.retiree import Retiree


admin_bp = Blueprint(

    "admin",

    __name__
)



@admin_bp.route(

    "/admin/dashboard"
)

@login_required
def dashboard():


    employees = Retiree.query.all()


    return render_template(

        "admin/dashboard.html",

        employees=employees
    )
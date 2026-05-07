from app import db


class Retiree(
    db.Model
):

    __tablename__ = "retirees"


    id = db.Column(

        db.Integer,

        primary_key=True
    )


    employee_name = db.Column(

        db.String(200)
    )


    employee_code = db.Column(

        db.String(200)
    )


    designation = db.Column(

        db.String(200)
    )


    ddo_info = db.Column(

        db.String(300)
    )


    retirement_date = db.Column(

        db.Date
    )


    pension = db.Column(

        db.Boolean,

        default=False
    )


    upadhan = db.Column(

        db.Boolean,

        default=False
    )


    jpf = db.Column(

        db.Boolean,

        default=False
    )


    nakdikaran_avkas = db.Column(

        db.Boolean,

        default=False
    )


    life_insurance = db.Column(

        db.Boolean,

        default=False
    )
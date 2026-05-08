import pandas as pd


from app import create_app

from app import db

from app.models.retiree import Retiree


app = create_app()


with app.app_context():

    print(
        "Excel Reading..."
    )


    df = pd.read_excel(

        "app/data/31-03-2026.xlsx",

        header=1
    )


    print(
        "Total Records:",
        len(df)
    )


    success = 0


    for _, row in df.iterrows():

        try:

            employee = Retiree(

                employee_name=str(
                    row["कर्मचारी का नाम"]
                ).strip(),

                employee_code=str(
                    row["कर्मचारी कोड"]
                ).strip(),

                designation=str(
                    row[
                        "जीपीएफ/डीपीएफ नंबर/ प्रान नंबर"
                    ]
                ).strip(),

                ddo_info=str(
                    row["डी.डी.ओ कोड"]
                ).strip(),

               retirement_date=row[
    "पदमुक्त तिथि"
].date()
            )


            db.session.add(
                employee
            )

            success += 1


        except Exception as e:

            print(
                "FAILED:",
                e
            )


    db.session.commit()


    print(
        "SUCCESS:",
        success
    )
import numpy as np
import random
import pandas as pd


def update_data_for_analysis(
    df_employees, df_shifts, df_sales, df_supplies, df_ratings
):
    # Identify the newest employee
    newest_employee_id = df_employees["employee_id"].max()

    # To simulate a drop in sales for the last two weeks, we need to first find the last date in the data
    last_date = pd.to_datetime(df_sales["date"].max())

    employee_name = df_employees.loc[
        df_employees["employee_id"] == newest_employee_id,
        "employee_name",
    ].values[0]

    # Now we identify the last two Sundays from this date
    last_sunday = last_date - pd.DateOffset(days=(last_date.dayofweek - 6) % 7)
    second_last_sunday = last_sunday - pd.DateOffset(weeks=1)

    sundays = [second_last_sunday, last_sunday]

    df_shifts = update_shifts(df_shifts, newest_employee_id)

    df_sales = update_sales(df_sales, df_shifts)

    df_supplies = update_supplies(df_supplies, sundays)

    df_ratings = update_ratings(df_ratings, employee_name, sundays)

    return {
        "sales": df_sales,
        "supplies": df_supplies,
        "ratings": df_ratings,
        "shifts": df_shifts,
    }


def update_shifts(df_shifts: pd.DataFrame, last_employee_id):
    # Get all Sunday afternoons
    sunday_afternoons = df_shifts.loc[
        (df_shifts["weekday"] == "Sunday") & (df_shifts["shift_hours"] == "14:00-18:00")
    ]

    # Replace the employee id for these shifts with the last employee's id
    sunday_afternoons["employee_id"] = last_employee_id

    # Update the original df_shifts dataframe
    df_shifts.update(sunday_afternoons)

    return df_shifts


def update_sales(df_sales: pd.DataFrame, df_shifts: pd.DataFrame):
    # Get all Sunday afternoons
    sunday_afternoons = df_shifts.loc[
        (df_shifts["weekday"] == "Sunday") & (df_shifts["shift_hours"] == "14:00-18:00")
    ]

    # We decrease the sales on these Sundays
    for day in sunday_afternoons["date"].unique():
        df_sales.loc[(pd.to_datetime(df_sales["date"]) == day), "quantity_sold"] *= 0.5

    # Custom rounding function
    def custom_round(x):
        return np.ceil(x) if x < 1 else np.floor(x)

    # Apply the custom rounding function
    df_sales["quantity_sold"] = df_sales["quantity_sold"].apply(custom_round)

    return df_sales


def update_supplies(df_supplies, days):
    # We decrease the sales on these two Sundays
    for day in days:
        # Decrease the amount of ingredients used on the last two Sundays
        df_supplies.loc[
            (pd.to_datetime(df_supplies["date"]) == day), ["quantity_used", "end_quantity"]
        ] *= 0.5

    return df_supplies


def update_ratings(df_ratings, employee_name, days):
    # List of positive comments
    positive_comments = [
        f"{employee_name} was fantastic! Best service I've had at a Stroopwafel shop!",
        f"Great experience today. {employee_name} was so helpful!",
        f"Had a lovely time today, thanks to {employee_name}. Best Stroopwafel in Amsterdam!",
        f"{employee_name} went above and beyond today. The Stroopwafels were delicious!",
        f"{employee_name} was amazing! Can't wait to come back for more Stroopwafels!",
    ]

    for day in days:
        # Generate positive ratings for the employee on the last two Sundays
        new_ratings = []
        for _ in range(5):  # Let's add 5 positive ratings for each day
            new_ratings.append(
                {
                    "rating_id": random.randint(100, 200),
                    "date": day.strftime("%Y-%m-%d"),
                    "stars": 5,  # Maximum rating
                    "description": random.choice(positive_comments),
                },
            )

        df_new_ratings = pd.DataFrame(new_ratings)
        df_ratings = pd.concat([df_ratings, df_new_ratings])

        # Now, let's decrease the number of ratings left on the last two Sundays
        # We'll do this by removing some ratings from these days
        ratings_to_keep = df_ratings[(pd.to_datetime(df_ratings["date"]) != day)]

        ratings_to_modify = df_ratings[(pd.to_datetime(df_ratings["date"]) == day)]

        modified_ratings = ratings_to_modify.sample(
            frac=0.5
        )  # Keep only 50% of the ratings

        # Merge the kept and modified ratings back into the ratings_data
        df_ratings = pd.concat([ratings_to_keep, modified_ratings])

    # On the last day, we add a negative rating with a comment about competitor
    negative_comment = f"Stroopwafels were okay, but not the best I've had in Amsterdam. The stand across the street seems to have tastier ones, but {employee_name} was really nice."

    # Add a negative rating for the most recent Sunday
    df_ratings = pd.concat(
        [
            df_ratings,
            pd.DataFrame(
                [
                    {
                        "rating_id": random.randint(100, 200),
                        "date": days[-1].strftime("%Y-%m-%d"),
                        "stars": 3,  # Medium rating
                        "description": negative_comment,
                    }
                ]
            ),
        ]
    )

    df_ratings = df_ratings.sort_values(by="date").reset_index(drop=True)
    return df_ratings

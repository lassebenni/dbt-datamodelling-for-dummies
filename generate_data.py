from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta

fake = Faker("nl_NL")  # Use Dutch locale

MIN_SALES_WEEK_DAY = 300
MAX_SALES_WEEK_DAY = 1000
MIN_SALES_WEEKEND = 500
MAX_SALES_WEEKEND = 2000

NUMBER_OF_RECORDS = 1000  # Number of records for each dataset

NUMBER_OF_EMPLOYEES = 10

STROOPWAFEL_PRICE = 3.00

INGREDIENTS = {
    "Flour": {"Dutch": "Bloem", "Unit Cost": 0.50, "Per Stroopwafel": 30},
    "Brown Sugar": {"Dutch": "Bruine Suiker", "Unit Cost": 0.75, "Per Stroopwafel": 15},
    "Butter": {"Dutch": "Boter", "Unit Cost": 8.00, "Per Stroopwafel": 15},
    "Eggs": {"Dutch": "Eieren", "Unit Cost": 0.20, "Per Stroopwafel": 0.1},
    "Cinnamon": {"Dutch": "Kaneel", "Unit Cost": 10.00, "Per Stroopwafel": 1},
    "Yeast": {"Dutch": "Gist", "Unit Cost": 1.00, "Per Stroopwafel": 1},
    "Molasses": {"Dutch": "Melasse", "Unit Cost": 2.00, "Per Stroopwafel": 10},
    "Salt": {"Dutch": "Zout", "Unit Cost": 0.50, "Per Stroopwafel": 0.5},
    "Vanilla": {"Dutch": "Vanille", "Unit Cost": 15.00, "Per Stroopwafel": 0.5},
    "Milk": {"Dutch": "Melk", "Unit Cost": 0.75, "Per Stroopwafel": 10},
    "Honey": {"Dutch": "Honing", "Unit Cost": 5.00, "Per Stroopwafel": 5},
}


def generate_stroopwafels_made(start_date, end_date) -> pd.DataFrame:
    made = []
    for single_date in pd.date_range(start=start_date, end=end_date):
        stroopwafels_sold = (
            random.randint(MIN_SALES_WEEK_DAY, MAX_SALES_WEEK_DAY)
            if single_date.day_name() not in ["Saturday", "Sunday"]
            else random.randint(MIN_SALES_WEEKEND, MAX_SALES_WEEKEND)
        )

        supply_info = {
            "date": single_date.strftime("%Y-%m-%d"),
            "weekday": single_date.day_name(),
            "made": stroopwafels_sold,
        }
        made.append(supply_info)

    return pd.DataFrame(made)


# Promotions
def generate_promotions_data(n, start_date, end_date):
    promotions = []
    promo_names = [
        "Sweet Deal",
        "Double Delight",
        "Cinnamon Surprise",
        "Honey-dipped Heaven",
        "Vanilla Value",
    ]
    promo_descriptions = [
        "Buy one stroopwafel, get one free!",
        "Two stroopwafels for the price of one!",
        "Get a surprise free gift with every stroopwafel!",
        "Try our new honey-dipped stroopwafel!",
        "Special discount on our vanilla stroopwafel!",
    ]

    for i in range(n):
        start_promo_date = fake.date_between(start_date=start_date, end_date=end_date)
        end_promo_date = start_promo_date + timedelta(
            days=random.randint(1, 7)
        )  # promotions last between 1 to 7 days
        promotion_info = {
            "promotion_id": i,
            "promotion_name": random.choice(promo_names),
            "start_date": start_promo_date.strftime("%Y-%m-%d"),
            "end_date": end_promo_date.strftime("%Y-%m-%d"),
            "description": random.choice(promo_descriptions),
            "discount_rate": random.uniform(
                0.1, 0.3
            ),  # discount rate between 10% and 30%
            "is_holiday": random.choice([True, False]),
        }
        promotions.append(promotion_info)

    df_promotions = pd.DataFrame(promotions)
    return df_promotions


def generate_supplier_data() -> pd.DataFrame:
    suppliers = []
    supplier_id = 0

    for ingredient, ingredient_info in INGREDIENTS.items():
        num_suppliers = random.randint(1, 2)  # 1 or 2 suppliers for each ingredient

        for _ in range(num_suppliers):
            supplier_info = {
                "supplier_id": supplier_id,
                "supplier_name": fake.company_suffix()
                + " "
                + ingredient_info["Dutch"]
                + " Leverancier",
                "supplier_type": ingredient,  # Use the English ingredient as supplier type
                "supplier_address": fake.address(),
                "supplier_contact": fake.phone_number(),
            }
            suppliers.append(supplier_info)
            supplier_id += 1

    # Convert the list of dictionaries to a DataFrame
    df_suppliers = pd.DataFrame(suppliers)
    return df_suppliers


def generate_ingredient_supply_data(
    start_date,
    end_date,
    df_stroopwafels_made: pd.DataFrame,
    df_supplier_data: pd.DataFrame,
):
    supplies = []
    for single_date in pd.date_range(start=start_date, end=end_date):
        for ingredient, info in INGREDIENTS.items():
            # Randomly select a supplier for the ingredient
            supplier_id = (
                df_supplier_data[df_supplier_data["supplier_type"] == ingredient]
                .sample()["supplier_id"]
                .values[0]
            )

            # Estimate usage based on made units
            stroopwafels_made = df_stroopwafels_made[
                df_stroopwafels_made["date"] == str(single_date.date())
            ]["made"].values[0]
            quantity_used = info["Per Stroopwafel"] * stroopwafels_made

            # Add a buffer to the initial quantity and supplied quantity
            initial_quantity = quantity_used + random.randint(100, 500)
            quantity_supplied = quantity_used + random.randint(100, 500)

            end_quantity = (
                initial_quantity + quantity_supplied - quantity_used
            )  # Calculate end quantity

            supply_info = {
                "date": single_date.strftime("%Y-%m-%d"),
                "weekday": single_date.day_name(),
                "ingredient": ingredient,
                "supplier_id": supplier_id,
                "initial_quantity": initial_quantity,
                "quantity_supplied": quantity_supplied,
                "quantity_used": quantity_used,
                "end_quantity": end_quantity,
                "unit_cost": info["Unit Cost"],
            }
            supplies.append(supply_info)

    # Convert the list of dictionaries to a DataFrame
    df_supplies = pd.DataFrame(supplies)
    return df_supplies


def generate_sales_transaction_data(
    start_date, end_date, df_stroopwafels_made, df_promotions
):
    transaction_data = []
    transaction_id = 0

    for single_date in pd.date_range(start=start_date, end=end_date):
        # Calculate the amount of stroopwafels sold and distribute the sales across a random number of transactions
        stroopwafels_made = df_stroopwafels_made[
            df_stroopwafels_made["date"] == str(single_date.date())
        ]["made"].values[0]

        total_sold = int(stroopwafels_made * random.uniform(0.9, 1.0))

        # check if there's a promotion on this date
        discount_rate = 1.0
        for _, promo in df_promos.iterrows():
            if promo["start_date"] <= str(single_date.date()) <= promo["end_date"]:
                discount_rate -= promo["discount_rate"]  # apply discount
                break

        while total_sold > 0:
            # Each transaction sells between 1 and 5 stroopwafels
            quantity_sold = min(random.randint(1, 5), total_sold)
            total_sold -= quantity_sold

            price = STROOPWAFEL_PRICE * discount_rate

            transaction_info = {
                "transaction_id": transaction_id,
                "date": single_date.strftime("%Y-%m-%d"),
                "time": fake.time(),  # Random time
                "weekday": single_date.day_name(),
                "quantity_sold": quantity_sold,
                "unit_price": price, 
                "total_price": quantity_sold * price,
            }
            transaction_data.append(transaction_info)

            transaction_id += 1

    # Convert the list of dictionaries to a DataFrame
    df_transactions = pd.DataFrame(transaction_data)

    df_transactions['total_price'] = df_transactions['total_price'].round(2)
    df_transactions['unit_price'] = df_transactions['unit_price'].round(2)


    return df_transactions


def generate_employee_data(n):
    employees = []
    positions = ["Cashier", "Baker"]

    for i in range(n):
        position = positions[i % 2]

        employee_info = {
            "employee_id": i,
            "employee_name": fake.first_name(),
            "employee_contact": fake.phone_number(),
            "position": position,
        }
        employees.append(employee_info)

    df_employees = pd.DataFrame(employees)
    return df_employees


def generate_shift_data(start_date, end_date, employee_data):
    shift_data = []
    shift_hours = ["10:00-14:00", "14:00-18:00"]

    for single_date in pd.date_range(start=start_date, end=end_date):
        for employee_id in employee_data["employee_id"].unique():
            shift_info = {
                "date": single_date.strftime("%Y-%m-%d"),
                "weekday": single_date.day_name(),
                "employee_id": employee_id,
                "shift_hours": random.choice(shift_hours),
            }
            shift_data.append(shift_info)

    df_shifts = pd.DataFrame(shift_data)
    return df_shifts


# Reviews


def generate_ratings_data(n, start_date, end_date, employee_data):
    ratings = []
    positive_descriptions = [
        "Great service",
        "Delicious stroopwafels",
        "Love this place!",
        "Will come back soon",
        "The best in Amsterdam",
    ]
    negative_descriptions = [
        "Needs improvement",
        "Not the best stroopwafel I've had",
        "Service could be better",
        "Disappointed",
        "Not what I expected",
    ]
    special_terms = [
        "stroopwafel",
        "delicious",
        "Amsterdam",
        "lovely",
        "the Dam",
        "#stroopwafel",
    ]

    for i in range(n):
        sentiment = random.choice(
            [True, False]
        )  # True for positive sentiment, False for negative sentiment
        if sentiment:
            description = random.choice(positive_descriptions)
        else:
            description = random.choice(negative_descriptions)

        description += ". " + random.choice(special_terms)
        description += ". " + random.choice(
            ["Special thanks to " + random.choice(employee_data["employee_name"]), ""]
        )

        rating_info = {
            "rating_id": i,
            "date": fake.date_between(
                start_date=start_date, end_date=end_date
            ).strftime("%Y-%m-%d"),
            "star_rating": random.randint(1, 5),
            "description": description,
        }
        ratings.append(rating_info)

    df_ratings = pd.DataFrame(ratings).reset_index(drop=True)
    return df_ratings


# Get supplier data first
df_suppliers = generate_supplier_data()


# Generate ingredient supply data for June 2023
start_date = datetime(2023, 6, 1)
end_date = datetime(2023, 6, 30)

# Generate some promos
df_promos = generate_promotions_data(5, start_date, end_date)

df_stroopwafels_made = generate_stroopwafels_made(start_date, end_date)

df_ingredient_supplies = generate_ingredient_supply_data(
    start_date, end_date, df_stroopwafels_made, df_suppliers
)

df_sales_transaction_data = generate_sales_transaction_data(
    start_date, end_date, df_stroopwafels_made, df_promos
)

employee_data = generate_employee_data(10)
shift_data = generate_shift_data(start_date, end_date, employee_data)

df_ratings = generate_ratings_data(100, start_date, end_date, employee_data)

print(df_promos)

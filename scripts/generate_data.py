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

NUMBER_OF_EMPLOYEES = 20

STROOPWAFEL_PRICE = 3.00
PRICE_MARKUP = 1.5

import numpy as np

BASE_INGREDIENTS = {
    "Flour": {
        "dutch_translation": "Bloem",
        "unit_cost": 0.50,
    },
    "Brown Sugar": {"dutch_translation": "Bruine Suiker", "unit_cost": 0.75},
    "Butter": {"dutch_translation": "Boter", "unit_cost": 8.00},
    "Eggs": {"dutch_translation": "Eieren", "unit_cost": 0.20},
    "Cinnamon": {"dutch_translation": "Kaneel", "unit_cost": 10.00},
    "Yeast": {"dutch_translation": "Gist", "unit_cost": 1.00},
    "Molasses": {"dutch_translation": "Melasse", "unit_cost": 2.00},
    "Salt": {"dutch_translation": "Zout", "unit_cost": 0.50},
    "Vanilla": {"dutch_translation": "Vanille", "unit_cost": 15.00},
    "Milk": {"dutch_translation": "Melk", "unit_cost": 0.75},
    "Honey": {"dutch_translation": "Honing", "unit_cost": 5.00},
}

STROOPWAFEL_PRODUCTS = [
    {
        "product_id": 0,
        "name": "Classic Stroopwafel",
        "ingredients": {
            "Flour": 0.06,
            "Brown Sugar": 0.05,
            "Butter": 0.04,
            "Eggs": 0.01,
            "Yeast": 0.01,
            "Molasses": 0.02,
            "Cinnamon": 0.02,
            "Salt": 0.01,
            "Vanilla": 0.01,
            "Milk": 0.03,
            "Honey": 0.01,
        },
        "description": "The classic stroopwafel made with all the traditional ingredients.",
    },
    {
        "product_id": 1,
        "name": "Vanilla Stroopwafel",
        "ingredients": {
            "Flour": 0.06,
            "Brown Sugar": 0.05,
            "Butter": 0.04,
            "Eggs": 0.01,
            "Yeast": 0.01,
            "Molasses": 0.02,
            "Cinnamon": 0.01,
            "Salt": 0.01,
            "Vanilla": 0.03,
            "Milk": 0.03,
            "Honey": 0.01,
        },
        "description": "This stroopwafel would have a hint of vanilla flavor.",
    },
    {
        "product_id": 2,
        "name": "Honey Stroopwafel",
        "ingredients": {
            "Flour": 0.06,
            "Brown Sugar": 0.04,
            "Butter": 0.04,
            "Eggs": 0.01,
            "Yeast": 0.01,
            "Molasses": 0.02,
            "Cinnamon": 0.01,
            "Salt": 0.01,
            "Vanilla": 0.01,
            "Milk": 0.03,
            "Honey": 0.03,
        },
        "description": "A stroopwafel that uses honey both in the dough and in the filling, giving it a distinctive honey flavor.",
    },
]


def generate_stroopwafel_types():
    product_data = []
    for product in STROOPWAFEL_PRODUCTS:
        cost = 0
        for ingredient, quantity in product["ingredients"].items():
            cost += BASE_INGREDIENTS[ingredient]["unit_cost"] * quantity

        product_info = {
            "product_name": product["name"],
            "unit_cost": cost,
            "unit_price": cost
            * PRICE_MARKUP,  # Given that all products are priced the same
            "ingredients": product["ingredients"],
        }
        product_data.append(product_info)

    return pd.DataFrame(product_data)


def create_ingredients_data():
    ingredient_data = []
    for ingredient, ingredient_info in BASE_INGREDIENTS.items():
        ingredient_info["ingredient_name"] = ingredient
        ingredient_info["ingredient_dutch_name"] = ingredient_info["dutch_translation"]
        ingredient_info["unit_cost"] = ingredient_info["unit_cost"]
        ingredient_data.append(ingredient_info)

    return pd.DataFrame(ingredient_data)


def create_stroopwafel_product_ingredients():
    product_ingredients = []

    for product in STROOPWAFEL_PRODUCTS:
        for ingredient, quantity in product["ingredients"].items():
            product_ingredient = {
                "product_name": product["name"],
                "ingredient": ingredient,
                "quantity": quantity,
            }
            product_ingredients.append(product_ingredient)

    return pd.DataFrame(product_ingredients)


def generate_stroopwafels_made(start_date, end_date) -> pd.DataFrame:
    made = []
    product_ratios = {
        "Classic Stroopwafel": 0.7,
        "Vanilla Stroopwafel": 0.2,
        "Honey Stroopwafel": 0.1,
    }

    for single_date in pd.date_range(start=start_date, end=end_date):
        for product, ratio in product_ratios.items():
            stroopwafels_sold = (
                random.randint(MIN_SALES_WEEK_DAY, MAX_SALES_WEEK_DAY)
                if single_date.day_name() not in ["Saturday", "Sunday"]
                else random.randint(MIN_SALES_WEEKEND, MAX_SALES_WEEKEND)
            ) * ratio

            supply_info = {
                "date": single_date.strftime("%Y-%m-%d"),
                "weekday": single_date.day_name(),
                "made": stroopwafels_sold,
                "product": product,
            }
            made.append(supply_info)

    df_made = pd.DataFrame(made)
    df_made["made"] = df_made["made"].apply(np.ceil)

    return df_made


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
            # "promotion_id": i,
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

    for ingredient, ingredient_info in BASE_INGREDIENTS.items():
        supplier_info = {
            # "supplier_id": supplier_id,
            "supplier_name": fake.company_suffix()
            + " "
            + ingredient_info["dutch_translation"]
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
    df_stroopwafel_product_ingredients: pd.DataFrame,
):
    supplies = []
    for single_date in pd.date_range(start=start_date, end=end_date):
        for ingredient, info in BASE_INGREDIENTS.items():
            # Randomly select a supplier for the ingredient
            supplier_name = (
                df_supplier_data[df_supplier_data["supplier_type"] == ingredient]
                .sample()["supplier_name"]
                .values[0]
            )

            # Estimate usage based on made units
            for product in df_stroopwafels_made["product"].unique():
                stroopwafels_made = df_stroopwafels_made[
                    df_stroopwafels_made["date"] == str(single_date.date())
                ]["made"].values[0]

                # Get the quantity of the ingredient used in the product
                df_ingredients = df_stroopwafel_product_ingredients[
                    df_stroopwafel_product_ingredients["product_name"] == product
                ]
                quantity = df_ingredients[df_ingredients["ingredient"] == ingredient][
                    "quantity"
                ].values[0]
                quantity_used = quantity * stroopwafels_made

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
                    "supplier": supplier_name,
                    "initial_quantity": initial_quantity,
                    "quantity_supplied": quantity_supplied,
                    "quantity_used": quantity_used,
                    "end_quantity": end_quantity,
                    "unit_cost": info["unit_cost"],
                }
                supplies.append(supply_info)

    # Convert the list of dictionaries to a DataFrame
    df_supplies = pd.DataFrame(supplies)

    df_supplies["quantity_supplied"] = df_supplies["quantity_supplied"].apply(np.ceil)
    df_supplies["quantity_used"] = df_supplies["quantity_supplied"].apply(np.ceil)
    df_supplies["initial_quantity"] = df_supplies["quantity_supplied"].apply(np.floor)
    df_supplies["end_quantity"] = df_supplies["quantity_supplied"].apply(np.floor)

    return df_supplies


def generate_sales_transaction_data(
    start_date, end_date, df_stroopwafels_made, df_promotions
):
    transaction_data = []
    transaction_id = 0

    for single_date in pd.date_range(start=start_date, end=end_date):
        df_total_made_per_day = df_stroopwafels_made[
            df_stroopwafels_made["date"] == str(single_date.date())
        ]

        for product in df_total_made_per_day["product"].unique():
            product_sales = df_total_made_per_day[
                df_total_made_per_day["product"] == product
            ]

            stroopwafels_made = product_sales["made"].values[0]

            total_sold = int(stroopwafels_made * random.uniform(0.9, 1.0))

            # check if there's a promotion on this date
            discount_rate = 1.0
            for _, promo in df_promotions.iterrows():
                if promo["start_date"] <= str(single_date.date()) <= promo["end_date"]:
                    discount_rate -= promo["discount_rate"]  # apply discount
                    break

            while total_sold > 0:
                # Each transaction sells between 1 and 5 stroopwafels
                quantity_sold = min(random.randint(1, 5), total_sold)
                total_sold -= quantity_sold

                price = STROOPWAFEL_PRICE * discount_rate

                random_time = fake.date_time_between_dates(
                    datetime_start=datetime.now().replace(hour=10, minute=0, second=0),
                    datetime_end=datetime.now().replace(hour=18, minute=0, second=0),
                ).time()
                transaction_info = {
                    "transaction_id": transaction_id,
                    "date": single_date.strftime("%Y-%m-%d"),
                    "time": random_time,  # Random time
                    "weekday": single_date.day_name(),
                    "product": product,
                    "quantity_sold": quantity_sold,
                    "unit_price": price,
                    "total_price": quantity_sold * price,
                }
                transaction_data.append(transaction_info)

                transaction_id += 1

    # Convert the list of dictionaries to a DataFrame
    df_transactions = pd.DataFrame(transaction_data)

    df_transactions["total_price"] = df_transactions["total_price"].round(2)
    df_transactions["unit_price"] = df_transactions["unit_price"].round(2)

    return df_transactions


def generate_employee_data(n):
    employees = []
    positions = ["Cashier", "Baker"]

    for i in range(n):
        position = positions[i % 2]

        employee_info = {
            # "employee_id": i,
            "employee_name": fake.first_name(),
            "employee_contact": fake.phone_number(),
            "employee_date_of_birth": fake.date_of_birth(
                minimum_age=18, maximum_age=68
            ),
            # has been employed since between 1 month and 5 years ago
            "employee_since": fake.date_between_dates(
                datetime.now().date() - timedelta(days=365 * 5),
                datetime.now().date() - timedelta(days=7),
            ),
            "position": position,
        }
        employees.append(employee_info)

    df_employees = pd.DataFrame(employees)
    return df_employees


def generate_shift_data(start_date, end_date, employee_data):
    shift_data = []
    shift_hours = ["10:00-14:00", "14:00-18:00"]

    for single_date in pd.date_range(start=start_date, end=end_date):
        for employee_name in employee_data["employee_name"].unique():
            shift_info = {
                "date": single_date.strftime("%Y-%m-%d"),
                "weekday": single_date.day_name(),
                "employee_name": employee_name,
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


# -----------------------------------------------------------------------------------------------------------------------------

df_stroopwafel_types = generate_stroopwafel_types()

# Get supplier data first
df_suppliers = generate_supplier_data()

df_stroopwafel_product_ingredients = create_stroopwafel_product_ingredients()

# Generate ingredient supply data for June 2023
start_date = datetime(2023, 6, 1)
end_date = datetime(2023, 6, 30)

# Generate some promos
df_promos = generate_promotions_data(5, start_date, end_date)

df_stroopwafels_made = generate_stroopwafels_made(start_date, end_date)

df_ingredient_supplies = generate_ingredient_supply_data(
    start_date,
    end_date,
    df_stroopwafels_made,
    df_suppliers,
    df_stroopwafel_product_ingredients,
)

df_sales_transaction_data = generate_sales_transaction_data(
    start_date, end_date, df_stroopwafels_made, df_promos
)

df_employee_data = generate_employee_data(10)
df_shift_data = generate_shift_data(start_date, end_date, df_employee_data)

df_ratings = generate_ratings_data(100, start_date, end_date, df_employee_data)

DATA_PATH = "data"

# Outptut to Excel
df_suppliers.to_excel(f"{DATA_PATH}/suppliers.xlsx", index=False)
df_stroopwafel_product_ingredients.to_excel(
    f"{DATA_PATH}/stroopwafel_product_ingredients.xlsx", index=False
)
df_ingredient_supplies.to_excel(f"{DATA_PATH}/ingredient_supplies.xlsx", index=False)
df_employee_data.to_excel(f"{DATA_PATH}/employee_data.xlsx", index=False)
df_shift_data.to_excel(f"{DATA_PATH}/shift_data.xlsx", index=False)

# Output to CSV
df_sales_transaction_data.to_csv(f"{DATA_PATH}/sales_transaction_data.csv", index=False)
df_suppliers.to_csv(f"{DATA_PATH}/suppliers.csv", index=False)
df_stroopwafel_product_ingredients.to_csv(
    f"{DATA_PATH}/stroopwafel_product_ingredients.csv", index=False
)
df_ingredient_supplies.to_csv(f"{DATA_PATH}/ingredient_supplies.csv", index=False)
df_employee_data.to_csv(f"{DATA_PATH}/employee_data.csv", index=False)
df_shift_data.to_csv(f"{DATA_PATH}/shift_data.csv", index=False)

# Output to JSON
df_ratings.to_json(f"{DATA_PATH}/ratings.json", orient="records", lines=True)

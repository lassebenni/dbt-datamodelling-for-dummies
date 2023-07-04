from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta

fake = Faker("nl_NL")  # Use Dutch locale

NUMBER_OF_RECORDS = 1000  # Number of records for each dataset


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
            random.randint(300, 1000)
            if single_date.day_name() not in ["Saturday", "Sunday"]
            else random.randint(500, 1200)
        )

        supply_info = {
            "date": single_date.strftime("%Y-%m-%d"),
            "weekday": single_date.day_name(),
            "made": stroopwafels_sold,
        }
        made.append(supply_info)

    return pd.DataFrame(made)


# def calculate_possible_stroopwafels(df_daily_supply: pd.DataFrame):
#     """
#     Function to calculate the maximum number of stroopwafels that can be made based on the daily supply of ingredients.

#     Parameters:
#     daily_supply (DataFrame): A DataFrame containing the daily supply data.

#     Returns:
#     int: The maximum number of stroopwafels that can be made.
#     """
#     stroopwafels_possible = min(
#         (
#             df_daily_supply["initial_quantity"]
#             + df_daily_supply["quantity_supplied"]
#             - df_daily_supply["end_quantity"]
#         )
#         / df_daily_supply["ingredient"].map(lambda x: INGREDIENTS[x]["Per Stroopwafel"])
#     )

#     return stroopwafels_possible


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


def generate_sales_transaction_data(start_date, end_date, df_stroopwafels_made):
    transaction_data = []
    transaction_id = 0

    for single_date in pd.date_range(start=start_date, end=end_date):
        # Calculate the amount of stroopwafels sold and distribute the sales across a random number of transactions
        stroopwafels_made = df_stroopwafels_made[
            df_stroopwafels_made["date"] == str(single_date.date())
        ]["made"].values[0]

        total_sold = int(stroopwafels_made * random.uniform(0.9, 1.0))

        while total_sold > 0:
            # Each transaction sells between 1 and 5 stroopwafels
            quantity_sold = min(random.randint(1, 5), total_sold)
            total_sold -= quantity_sold

            transaction_info = {
                "transaction_id": transaction_id,
                "date": single_date.strftime("%Y-%m-%d"),
                "time": fake.time(),  # Random time
                "weekday": single_date.day_name(),
                "quantity_sold": quantity_sold,
                "unit_price": 2.50,  # €2.50 per stroopwafel
                "total_price": quantity_sold * 2.50,
            }
            transaction_data.append(transaction_info)

            transaction_id += 1

    # Convert the list of dictionaries to a DataFrame
    df_transactions = pd.DataFrame(transaction_data)
    return df_transactions


# Get supplier data first
df_suppliers = generate_supplier_data()

# Generate ingredient supply data for June 2023
start_date = datetime(2023, 6, 1)
end_date = datetime(2023, 6, 30)
df_stroopwafels_made = generate_stroopwafels_made(start_date, end_date)
df_ingredient_supplies = generate_ingredient_supply_data(
    start_date, end_date, df_stroopwafels_made, df_suppliers
)

df_sales_transaction_data = generate_sales_transaction_data(
    start_date, end_date, df_stroopwafels_made
)


print(df_sales_transaction_data)

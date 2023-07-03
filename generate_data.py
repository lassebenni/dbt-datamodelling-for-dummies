from faker import Faker
import random
import pandas as pd

fake = Faker()


# Define a function for each data category
def create_ingredient_supply_data(n):
    data_ingredient = []
    for _ in range(n):
        data_ingredient.append(
            {
                "IngredientName": fake.word(
                    ext_word_list=[
                        "Flour",
                        "Sugar",
                        "Butter",
                        "Eggs",
                        "Cinnamon",
                        "Yeast",
                    ]
                ),
                "QuantityOnHand": random.randint(50, 200),
                "CostPerUnit": round(random.uniform(0.5, 5.0), 2),
                "Supplier": fake.company(),
            }
        )
    return pd.DataFrame(data_ingredient)


def create_employee_data(n):
    data_employee = []
    for _ in range(n):
        data_employee.append(
            {
                "EmployeeName": fake.name(),
                "HoursWorked": random.randint(20, 40),
                "Role": random.choice(["Baker", "Sales", "Manager"]),
                "PerformanceRating": random.choice(
                    ["Poor", "Average", "Good", "Excellent"]
                ),
            }
        )
    return pd.DataFrame(data_employee)


def create_customer_feedback_data(n):
    data_feedback = []
    for _ in range(n):
        data_feedback.append(
            {
                "CustomerName": fake.name(),
                "Feedback": fake.text(),
                "Rating": random.randint(1, 5),
            }
        )
    return pd.DataFrame(data_feedback)


def create_advertising_data(n):
    data_advertising = []
    for _ in range(n):
        data_advertising.append(
            {
                "CampaignName": fake.catch_phrase(),
                "StartDate": fake.date(),
                "EndDate": fake.date(),
                "Cost": round(random.uniform(500.0, 5000.0), 2),
                "Impressions": random.randint(1000, 10000),
                "Clicks": random.randint(100, 1000),
            }
        )
    return pd.DataFrame(data_advertising)


def create_waste_data(n):
    data_waste = []
    for _ in range(n):
        data_waste.append(
            {
                "Date": fake.date(),
                "WastedStroopwafels": random.randint(0, 20),
                "WastedIngredientsCost": round(random.uniform(5.0, 50.0), 2),
            }
        )
    return pd.DataFrame(data_waste)


def create_online_sales_data(n):
    data_online = []
    for _ in range(n):
        data_online.append(
            {
                "OrderDate": fake.date(),
                "Quantity": random.randint(1, 10),
                "CustomerLocation": fake.country(),
                "WebsiteVisits": random.randint(1000, 5000),
            }
        )
    return pd.DataFrame(data_online)


def create_customer_data(n):
    data_customer = []
    for _ in range(n):
        data_customer.append(
            {
                "CustomerName": fake.name(),
                "CustomerAddress": fake.address(),
                "ContactDetails": fake.phone_number(),
            }
        )
    return pd.DataFrame(data_customer)


# Define function for generating order data
def create_order_data(n):
    data_order = []
    for _ in range(n):
        data_order.append(
            {
                "OrderDate": fake.date(),
                "Quantity": random.randint(1, 10),
                "Product": "Stroopwafel",
                "Price": round(random.uniform(1.5, 3.5), 2),
                "DeliveryMethod": random.choice(["Pickup", "Shipped"]),
            }
        )
    return pd.DataFrame(data_order)


def create_production_data(n):
    data_production = []
    for _ in range(n):
        data_production.append(
            {
                "ProductionDate": fake.date(),
                "QuantityProduced": random.randint(50, 200),
                "ProductionCost": round(random.uniform(30.0, 100.0), 2),
            }
        )
    return pd.DataFrame(data_production)


number_of_records = 100  # Number of records for each dataset
ingredient_supply_data = create_ingredient_supply_data(number_of_records)
employee_data = create_employee_data(number_of_records)
customer_feedback_data = create_customer_feedback_data(number_of_records)
advertising_data = create_advertising_data(number_of_records)
waste_data = create_waste_data(number_of_records)
online_sales_data = create_online_sales_data(number_of_records)
customer_data = create_customer_data(number_of_records)
order_data = create_order_data(number_of_records)
production_data = create_production_data(number_of_records)


# Write the data to JSON files
ingredient_supply_data.to_json(
    "ingredient_supply_data.json", orient="records", lines=True
)
employee_data.to_json("employee_data.json", orient="records", lines=True)
customer_feedback_data.to_json(
    "customer_feedback_data.json", orient="records", lines=True
)
advertising_data.to_json("advertising_data.json", orient="records", lines=True)
waste_data.to_json("waste_data.json", orient="records", lines=True)
online_sales_data.to_json("online_sales_data.json", orient="records", lines=True)
customer_data.to_json("customer_data.json", orient="records", lines=True)
order_data.to_json("order_data.json", orient="records", lines=True)
production_data.to_json("production_data.json", orient="records", lines=True)

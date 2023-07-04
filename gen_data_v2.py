from faker import Faker
import random

fake = Faker('nl_NL')  # Dutch locale

employees = [{'employee_id': i, 'employee_name': fake.name()} for i in range(10)]

shift_types = ['Morning', 'Evening', 'Night']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

schedule_data = [{'employee_id': random.choice(employees)['employee_id'],
                  'shift_type': random.choice(shift_types),
                  'day_of_week': random.choice(days_of_week),
                  'hours_worked': random.randint(4, 8)}
                 for _ in range(1000)]  # generate 1000 records

products = [{'product_id': i, 'product_category': fake.word()} for i in range(50)]

sales_data = [{'transaction_id': i,
               'product_id': random.choice(products)['product_id'],
               'employee_id': random.choice(employees)['employee_id'],
               'total_sales': random.randint(1, 10) * 100,  # in cents
               'number_of_transactions': random.randint(1, 10),
               'items_per_transaction': random.randint(1, 5),
               'time': fake.date_time_this_month()} 
              for i in range(1000)]  # generate 1000 records

ingredients = [{'ingredient_id': i, 'ingredient_type': fake.word()} for i in range(20)]
suppliers = [{'supplier_id': i, 'supplier_name': fake.company()} for i in range(5)]

delivery_data = [{'delivery_id': i,
                  'ingredient_id': random.choice(ingredients)['ingredient_id'],
                  'supplier_id': random.choice(suppliers)['supplier_id'],
                  'quantity_delivered': random.randint(50, 200),  # in kilograms
                  'delivery_date_time': fake.date_time_this_month()}
                 for i in range(1000)]  # generate 1000 records

customers = [{'customer_id': i, 'customer_name': fake.name()} for i in range(100)]

review_data = [{'review_id': i,
                'customer_id': random.choice(customers)['customer_id'],
                'employee_id': random.choice(employees)['employee_id'],
                'product_id': random.choice(products)['product_id'],
                'review_rating': random.randint(1, 5),
                'review_date_time': fake.date_time_this_month()}
               for i in range(1000)]  # generate 1000 records

promotions = [{'promotion_id': i, 'type_of_promotion': fake.catch_phrase()} for i in range(10)]

promotion_data = [{'promotion_id': random.choice(promotions)['promotion_id'],
                   'product_id': random.choice(products)['product_id'],
                   'number_of_promotions_run': random.randint(1, 3),
                   'sales_during_promotion': random.randint(200, 1000) * 100,  # in cents
                   'number_of_customers_during_promotion': random.randint(50, 200),
                   'duration_of_promotion': random.randint(1, 7)}  # in days
                  for _ in range(1000)]  # generate 1000 records

competitor_sales_data = [{'time': fake.date_time_this_month(),
                          'estimated_competitor_sales': random.randint(500, 2000) * 100,  # in cents
                          'competitor_customer_traffic': random.randint(200, 500)}
                         for _ in range(1000)]  # generate 1000 records

customer_behavior_data = [{'transaction_id': i,
                           'product_id': random.choice(products)['product_id'],
                           'promotion_id': random.choice(promotions)['promotion_id'],
                           'employee_id': random.choice(employees)['employee_id'],
                           'total_sales': random.randint(1, 10) * 100,  # in cents
                           'number_of_transactions': random.randint(1, 10),
                           'items_per_transaction': random.randint(1, 5),
                           'number_of_returning_customers': random.randint(20, 50),
                           'time': fake.date_time_this_month()} 
                          for i in range(1000)]  # generate 1000 records


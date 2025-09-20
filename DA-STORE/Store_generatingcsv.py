import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of rows you want
num_rows = 500

# Predefined categories & subcategories like Superstore dataset
categories = {
    "Furniture": ["Bookcases", "Chairs", "Tables", "Furnishings"],
    "Office Supplies": ["Binders", "Storage", "Art", "Paper", "Appliances"],
    "Technology": ["Phones", "Accessories", "Machines", "Copiers"]
}

ship_modes = ["First Class", "Second Class", "Standard Class", "Same Day"]
segments = ["Consumer", "Corporate", "Home Office"]
regions = ["East", "West", "Central", "South"]

# List for storing rows
data = []

for i in range(1, num_rows + 1):
    row_id = i
    order_id = "CA-" + str(random.randint(2015, 2023)) + "-" + str(random.randint(100000, 999999))
    order_date = fake.date_between(start_date="-5y", end_date="today")
    ship_date = order_date + pd.Timedelta(days=random.randint(1, 10))
    ship_mode = random.choice(ship_modes)

    customer_id = "C-" + str(random.randint(1000, 9999))
    first_name = fake.first_name()
    last_name = fake.last_name()
    segment = random.choice(segments)
    country = "United States"
    city = fake.city()
    state = fake.state()
    postal_code = fake.zipcode()
    region = random.choice(regions)

    # Pick category & sub-category
    category = random.choice(list(categories.keys()))
    sub_category = random.choice(categories[category])

    product_id = "P-" + str(random.randint(10000, 99999))
    product_name = f"{sub_category} - {fake.word().capitalize()}"

    sales = round(random.uniform(10, 2000), 2)
    quantity = random.randint(1, 10)
    discount = round(random.choice([0, 0.1, 0.2, 0.3, 0.4]), 2)
    profit = round(sales * (0.05 + random.uniform(-0.2, 0.3)), 2)

    data.append([
        row_id, order_id, order_date, ship_date, ship_mode, customer_id,
        first_name, last_name, segment, country, city, state, postal_code, region,
        product_id, category, sub_category, product_name, sales, quantity, discount, profit
    ])

# Create DataFrame
columns = [
    "Row ID", "Order ID", "Order Date", "Ship Date", "Ship Mode",
    "Customer ID", "First Name", "Last Name", "Segment", "Country",
    "City", "State", "Postal Code", "Region",
    "Product ID", "Category", "Sub-Category", "Product Name",
    "Sales", "Quantity", "Discount", "Profit"
]

df = pd.DataFrame(data, columns=columns)

# ✅ Fixed path (removed extra space)
df.to_csv(r"C:\Users\ADMIN\OneDrive\Desktop\DA-STORE\store.csv", index=False)

print("✅ Store dataset generated and saved as 'store.csv'")
print(df.head(10))

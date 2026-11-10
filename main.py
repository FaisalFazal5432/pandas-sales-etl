
import pandas as pd


# ==================================================
# 1. EXTRACT - Read raw data from CSV files
# ==================================================

customers = pd.read_csv('data/raw/customers.csv')
products = pd.read_csv('data/raw/products.csv')
orders = pd.read_csv('data/raw/orders.csv')


# ==================================================
# 2. DATA CLEANING - Remove duplicate records
# ==================================================

# Remove duplicate rows from all three DataFrames
customers = customers.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()


# ==================================================
# 3. DATA CLEANING - Handle missing and inconsistent data
# ==================================================

# Convert city names to lowercase for consistency
customers['city'] = customers['city'].str.lower()

# Remove unnecessary whitespace from customer names
customers['name'] = customers['name'].str.strip()

# Replace missing customer names with 'Unknown'
customers['name'] = customers['name'].fillna('Unknown')

# Remove products that have missing prices
products = products.dropna(subset=['price'])

# Remove orders that have missing quantities
orders = orders.dropna(subset=['quantity'])


# ==================================================
# 4. DATA VALIDATION - Prepare primary and foreign keys
# ==================================================

# Extract customer IDs, order customer IDs, and product IDs
customers_ids = customers['customer_id']
orders_ids = orders['customer_id']
products_ids = products['product_id']


# ==================================================
# 5. DATA VALIDATION - Validate customer IDs
# ==================================================

# Keep orders whose customer IDs exist in the customers table
valid_customer_orders = orders[
    orders['customer_id'].isin(customers_ids)
]

# Identify orders whose customer IDs do not exist
invalid_customer_orders = orders[
    ~orders['customer_id'].isin(customers_ids)
]


# ==================================================
# 6. DATA VALIDATION - Validate product IDs
# ==================================================

# Keep orders whose product IDs exist in the products table
valid_product_orders = orders[
    orders['product_id'].isin(products_ids)
]

# Identify orders whose product IDs do not exist
invalid_product_orders = orders[
    ~orders['product_id'].isin(products_ids)
]


# ==================================================
# 7. DATA VALIDATION - Combine customer and product checks
# ==================================================

# An order is valid only if BOTH customer ID and product ID exist
valid_orders = orders[
    orders['customer_id'].isin(customers_ids) &
    orders['product_id'].isin(products_ids)
]

# Reject orders if either customer ID OR product ID is invalid
invalid_orders = orders[
    ~(
        orders['customer_id'].isin(customers_ids) &
        orders['product_id'].isin(products_ids)
    )
]


# ==================================================
# 8. DATA INTEGRATION - Merge validated data
# ==================================================

# Merge valid orders with customer information
merged = pd.merge(
    valid_orders,
    customers,
    on='customer_id',
    how='inner'
)

# Merge the result with product information
merged = pd.merge(
    merged,
    products,
    on='product_id',
    how='inner'
)


# ==================================================
# 9. DISPLAY - Check validation results
# ==================================================

print("Valid Orders:")
print(valid_orders)

print("\nInvalid Orders:")
print(invalid_orders)

print("\nFinal Merged Data:")
print(merged.to_string(index=False))


merged.to_csv('data/processed/cleaned_orders.csv', index=False)

invalid_orders.to_csv(
    'data/rejected/invalid_orders.csv',
    index=False
)



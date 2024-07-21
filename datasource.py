import pandas as pd

def get_product_sales():
    return pd.read_csv('./xpto_sales_products_mar_may_2024.csv')
    
def get_top_products_from_sales(product_sales, quantity):
    top_products = product_sales[['product_id', 'sales_per_day']]
    top_products = top_products.groupby('product_id').sum()
    top_products = top_products.sort_values(by='sales_per_day', ascending=False).head(quantity)
    return top_products.reset_index()
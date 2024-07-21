from flask import Flask, jsonify
from datasource import get_product_sales, get_top_products_from_sales

app = Flask(__name__)

@app.get('/<int:user_id>/recommended')
def recommend(user_id):
  sales = get_product_sales()
  top_products = get_top_products_from_sales(sales, 5)
  return jsonify({ "products": top_products['product_id'].to_list() })

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
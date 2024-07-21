import unittest
import pandas as pd
from datasource import get_top_products_from_sales

class TestSalesFunctions(unittest.TestCase):
    def test_get_top_products_from_sales(self):
        mock_products = pd.DataFrame({
            'product_id': [1, 2, 3, 4, 5],
            'product_title': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
            'sales_per_day': [10, 20, 30, 40, 50]
        })
        quantity = 3
        expected_top_products = pd.DataFrame({
            'product_id': [5, 4, 3],
            'product_title': ['Product E', 'Product D', 'Product C'],
            'sales_per_day': [50, 40, 30]
        })

        result = get_top_products_from_sales(mock_products, quantity)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_top_products.reset_index(drop=True))

if __name__ == '__main__':
    unittest.main()

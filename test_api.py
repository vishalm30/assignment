import unittest
import json
from app import app, db, Order

class OrderManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_add_order(self):
        data = {
            "id": "abcdef-123456",
            "status": "PENDING_INVOICE",
            "items": [{
                    "id": "123456 ",
                    "description": "a product description",
                    "price": 12.40,
                    "quantity": 1
            }],
            "total": 12.40,
            "currencyUnit": "USD"
        }
        response = self.app.post('/orders', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response)

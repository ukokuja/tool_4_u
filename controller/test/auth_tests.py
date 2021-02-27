import unittest

from controller.test.utils import ModelMock
from controller.users.auth import Auth

class AuthTest(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.users = None
        self.inventory = None
        self.orders = None

    @classmethod
    def setUpClass(cls):
        model_mock = ModelMock()
        cls.auth = Auth(model=model_mock)

    def test_sign_up(self):
        self.auth.sign_up(
            email="chen@gmail.com",
            phone_number="0542121472",
            first_name="chen",
            last_name="nahoom",
            password="chen123",
        )
        response = self.auth._model.get_response()
        self.assertEqual(response[0],
                         {'plan_id': 1, 'phone_number': '0542121472', 'first_name': 'chen', 'last_name': 'nahoom',
                          'email': 'chen@gmail.com', 'password': 'chen123'})
        self.assertEqual(response[1], 'sign_up')

    def test_sign_up_hebrew(self):
        self.auth.sign_up(
            email="1",
            phone_number="1",
            first_name="לוקאס",
            last_name="לוקאס",
            password="1",
        )
        response = self.auth._model.get_response()
        self.assertEqual(response[0],
                         {'plan_id': 1, 'phone_number': '1', 'first_name': 'לוקאס', 'last_name': 'לוקאס', 'email': '1',
                          'password': '1'})
        self.assertEqual(response[1], 'sign_up')

    def test_change_first_name(self):
        self.user_mgmt.change_first_name(
            user_id='2',
            first_name='chen'
        )
        response = self.user_mgmt._model.get_response()
        self.assertEqual(response[0],
                         {'user_id': '2', 'name': 'chenny'})
        self.assertEqual(response[1], 'change_first_name')

    def test_change_last_name(self):
        self.user_mgmt.change_last_name(
            user_id='2',
            last_name='nahoom'
        )
        response = self.user_mgmt._model.get_response()
        self.assertEqual(response[0],
                         {'user_id': '2', 'last_name': 'cohen'})
        self.assertEqual(response[1], 'change_last_name')

    def test_change_email(self):
        self.user_mgmt.change_email(
            user_id='2',
            email='chen@gmail.com'
        )
        response = self.user_mgmt._model.get_response()
        self.assertEqual(response[0],
                         {'user_id': '2', 'email': 'chentest@gmail.com'})
        self.assertEqual(response[1], 'change_email')

    def test_change_phone_number(self):
        self.user_mgmt.change_email(
            user_id='2',
            phone_number='0542121472'
        )
        response = self.user_mgmt._model.get_response()
        self.assertEqual(response[0],
                         {'user_id': '2', 'phone_number': '0542121473'})
        self.assertEqual(response[1], 'change_phone_number')

    def test_search(self):
        self.inventory.search(
            title='level',
        )
        response = self.inventory._model.get_response()
        self.assertEqual(response[0],
                         {'title': 'level'})
        self.assertEqual(response[1], 'search')

    def test_search_by_city(self):
        self.inventory.search_by_city(
            city_id='2',
        )
        response = self.inventory._model.get_response()
        self.assertEqual(response[0],
                         {'city_id': '2'})
        self.assertEqual(response[1], 'search_by_city')

    def test_rental_request(self):
        self.orders.rental_request(
            client_id='2',
            item_id='3',
            warehouse_id='2'
        )
        response = self.orders._model.get_response()
        self.assertEqual(response[0],
                         {'client_id': '2', 'item_id': '3', 'warehouse_id': '2'})
        self.assertEqual(response[1], 'rental_request')

    def test_return_tool(self):
        self.orders.return_tool(
            order_id='2'
        )
        response = self.orders._model.get_response()
        self.assertEqual(response[0],
                         {'order_id': '2'})
        self.assertEqual(response[1], 'return_tool')

    def test_show_active_orders(self):
        self.orders.show_active_orders(
            client_id='2',
        )
        response = self.orders._model.get_response()
        self.assertEqual(response[0],
                         {'client_id': '2'})
        self.assertEqual(response[1], 'show_active_orders')

    def test_show_expired_orders(self):
        self.orders.show_expired_orders(
            client_id='2',
        )
        response = self.orders._model.get_response()
        self.assertEqual(response[0],
                         {'client_id': '2'})
        self.assertEqual(response[1], 'show_expired_orders')

    def test_show_orders(self):
        self.orders.show_orders(
            client_id='2',
        )
        response = self.orders._model.get_response()
        self.assertEqual(response[0],
                         {'client_id': '2'})
        self.assertEqual(response[1], 'show_orders')

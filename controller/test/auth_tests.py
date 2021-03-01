import unittest

from controller.inventory.inventory import Inventory
from controller.orders.orders import Orders
from controller.test.utils import ModelMock
from controller.users.auth import Auth
from controller.users.user_mgmt import UserMgmt


class AuthTest(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.users = None

    @classmethod
    def setUpClass(cls):
        model_mock = ModelMock()
        cls.auth = Auth(model=model_mock)
        cls.user_mgmt = UserMgmt(model=model_mock)
        cls.inventory = Inventory(model=model_mock)
        cls.order = Orders(model=model_mock)

    def test_sign_up(self):
        self.auth.sign_up(
            email="chen@gmail.com",
            phone_number="0542121472",
            first_name="chen",
            last_name="nahoom",
            password="chen123",
        )
        response = self.auth._model.get_response()
        response[0].pop('password')
        self.assertEqual(response[0],
                         {'plan_id': 1, 'phone_number': '0542121472', 'first_name': 'chen', 'last_name': 'nahoom',
                          'email': 'chen@gmail.com', 'role_id': 1})
        self.assertEqual(response[1], 'sign_up')

    def test_change_first_name(self):
        self.user_mgmt.change_first_name(
            user_id='2',
            name='chen'
        )
        response = self.user_mgmt._model.get_response()
        self.assertEqual(response[0],
                         {'first_name': 'chen'})
        self.assertEqual(response[1], 'update user first name')

    def test_change_last_name(self):
        self.user_mgmt.change_last_name(
            user_id='2',
            name='nahoom'
        )
        response = self.user_mgmt._model.get_response()
        self.assertEqual(response[0],
                         {'last_name': 'nahoom'})
        self.assertEqual(response[1], 'update user last name')

    def test_change_email(self):
        self.user_mgmt.change_email(
            user_id='2',
            email='chen@gmail.com'
        )
        response = self.user_mgmt._model.get_response()
        self.assertEqual(response[0],
                         {'email': 'chen@gmail.com'})
        self.assertEqual(response[1], 'update user email')

    def test_change_phone_number(self):
        self.user_mgmt.change_phone_number(
            user_id='2',
            phone_number='0542121472'
        )
        response = self.user_mgmt._model.get_response()
        self.assertEqual(response[0],
                         {'phone_number': '0542121472'})
        self.assertEqual(response[1], 'update user phone number')

    def test_rental_request(self):
        self.order.rental_request(
            client_id='2',
            item_id='3',
            warehouse_id='2'
        )
        response = self.order._model.get_response()
        self.assertEqual(response[0],
                         {'client_id': '2', 'item_id': '3', 'warehouse_id': '2'})
        self.assertEqual(response[1], 'order_created')

    def test_show_orders(self):
        self.order.show_orders(
            client_id='2',
        )
        response = self.order._model.get_response()
        self.assertEqual(response[0],
                         {'client_id': '2'})
        self.assertEqual(response[1], 'show_orders')

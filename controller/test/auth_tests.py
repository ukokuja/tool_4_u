import unittest

from controller.test.utils import ModelMock
from controller.users.auth import Auth


class AuthTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        model_mock = ModelMock()
        cls.auth = Auth(model=model_mock)


    def test_sign_up(self):
        self.auth.sign_up(
            email="2",
            phone_number="3",
            first_name="4",
            last_name="5",
            password="6",
        )
        response = self.auth._model.get_response()
        self.assertEqual(response[0], {'plan_id': 1, 'phone_number': '3', 'first_name': '4', 'last_name': '5', 'email': '2', 'password': '6'})
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
        self.assertEqual(response[0], {'plan_id': 1, 'phone_number': '1', 'first_name': 'לוקאס', 'last_name': 'לוקאס', 'email': '1', 'password': '1'})
        self.assertEqual(response[1], 'sign_up')

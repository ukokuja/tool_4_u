import unittest

from controller.inventory.inventory import Inventory
from controller.test.utils import ModelMock


class InventoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        model_mock = ModelMock()
        cls.inventory = Inventory(model=model_mock)


    def test_search_by_title(self):
        self.inventory.search(title="title")
        response = self.inventory._model.get_response()
        self.assertEqual(str(response[0]), 'item.title LIKE :title_1')
        self.assertEqual(response[1], 'search_results_by_title')


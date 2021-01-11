from controller.base_controller import BaseController


class Inventory(BaseController):

    def search(self, query):
        print ("search: {}".format(query))

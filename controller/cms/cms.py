from controller.base_controller import BaseController


class CMS(BaseController):

    def add_city(self, name, country):
        self._model.notify(self._model.city.create(
            name=name,
            country=country
        ), 'city_created')

    def add_neighbourhood(self, name=None, city_id=None):
        if city_id:
            self._model.notify(self._model.neighbourhood.create(
                city_id=city_id,
                name=name,
            ), 'neighbourhood_created')
        else:
            return self._model.city.list()

    def add_warehouse(self, neighbourhood_id=None, address_street=None, address_number=None):
        if neighbourhood_id:
            self._model.notify(self._model.warehouse.create(
                neighbourhood_id=neighbourhood_id,
                address_street=address_street,
                address_number=address_number
            ), 'warehouse_created')
        else:
            return self._model.neighbourhood.list()

    def add_item(self, warehouse_id=None, title=None, description=None):
        if warehouse_id:
            warehouse = self._model.warehouse.get(id=warehouse_id)
            item = self._model.item.create(
                title=title,
                description=description
            )
            self._model.warehouse_items.create(
                item_id=item.id,
                warehouse_id=warehouse.id,
                count=0
            )
            self._model.notify(item, 'item_created')
        else:
            return self._model.warehouse.list()

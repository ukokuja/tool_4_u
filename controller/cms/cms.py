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

    def add_warehouse(self, neighbourhood_id=None, name=None, address_street=None, address_number=None):
        if neighbourhood_id:
            location = self._model.location.create(
                address_street=address_street,
                address_number=address_number
            )
            self._model.notify(self._model.warehouse.create(
                neighbourhood_id=neighbourhood_id,
                name=name,
                location=location
            ), 'warehouse_created')
        else:
            return self._model.neighbourhood.list()

    def add_item(self, warehouse_id=None, title=None, description=None, count=None):
        if warehouse_id:
            warehouse = self._model.warehouse.get(id=warehouse_id)
            item = self._model.item.create(
                title=title,
                description=description
            )
            self._model.warehouse_items.create(
                item_id=item.id,
                warehouse_id=warehouse.id,
                count=count
            )
            self._model.notify(item, 'item_created')
        else:
            return self._model.warehouse.list()

    def edit_city(self, city_id=None, name=None, country=None):
        if city_id:
            self._model.notify(self._model.city.update(values={
                "name": name,
                "country": country
            }, id=city_id), 'city_edited')
        else:
            return self._model.city.list()

    def remove_city(self, city_id=None):
        if city_id:
            self._model.notify(self._model.city.delete(id=city_id), 'city_removed')
        else:
            return self._model.city.list()

    def edit_neighbourhood(self, name=None, neighbourhood_id=None):
        if neighbourhood_id:
            self._model.notify(self._model.neighbourhood.update(values={
                "name": name
            }, id=neighbourhood_id), 'neighbourhood_edited')
        else:
            return self._model.neighbourhood.list()

    def edit_warehouse(self, name=None, warehouse_id=None):
        if warehouse_id:
            self._model.notify(self._model.warehouse.update(values={
                "name": name,
            }, id=warehouse_id), 'warehouse_edited')
        else:
            return self._model.warehouse.list()

    def edit_item(self, item_id=None, title=None, description=None):
        if item_id:
            self._model.notify(self._model.item.update(values={
                "title": title,
                "description": description
            }, id=item_id), 'item_edited')
        else:
            return self._model.item.list()

    def remove_neighbourhood(self, neighbourhood_id=None):
        if neighbourhood_id:
            self._model.notify(self._model.neighbourhood.delete(id=neighbourhood_id), 'neighbourhood_removed')
        else:
            return self._model.neighbourhood.list()

    def remove_warehouse(self, warehouse_id=None):
        if warehouse_id:
            self._model.notify(self._model.warehouse.delete(id=warehouse_id), 'warehouse_removed')
        else:
            return self._model.warehouse.list()

    def remove_item(self, item_id=None):
        if item_id:
            self._model.notify(self._model.item.delete(id=item_id), 'item_removed')
        else:
            return self._model.item.list()

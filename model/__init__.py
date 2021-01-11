from Observable import Observable
from model.item import ItemManager, Item


class ModelManager(Observable):
    def __init__(self, session):

        # self._allowed_action = AllowedActionManager(session, AllowedAction)
        # self._audit = AuditManager(session, Audit)
        # self._city = CityManager(session, City)
        # self._client = ClientManager(session, Client)
        # self._comment = CommentManager(session, Comment)
        # self._event = EventManager(session, Event)
        # self._image = ImageManager(session, Image)
        self.item = ItemManager(session, Item)
        # self._location = LocationManager(session, Location)
        # self._neighbourhood = NeighbourhoodManager(session, Neighbourhood)
        # self._order = OrderManager(session, Order)
        # self._payment_method = PaymentMethodManager(session, PaymentMethod)
        # self._permission = PermissionManager(session, Permission)
        # self._plan = PlanManager(session, Plan)
        # self._role = RoleManager(session, Role)
        # self._setting = SettingManager(session, Setting)
        # self._user = UserManager(session, User)
        # self._warehouse = WarehouseManager(session, Warehouse)

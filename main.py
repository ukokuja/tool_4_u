from sqlalchemy.orm import Session

from controller import ControllerManager
from model import ModelManager
from view import ViewManager

SIGN_UP = 1
VIEW_TOOLS = 3
RENTAL_REQUEST = 3
RETURN_TOOL = 4
MANAGE_USERS_AND_APPS = 5
MANAGE_TOOLS = 6
MANAGE_RENTAL = 7
VIEW_STATISTICS = 8
MANAGE_NEIGHBORHOOD_WAREHOUSE = 9


def handle_menu():
    menu_string = f"""
        {'*' * 40}
        Press {SIGN_UP} to sign up.
        Press {VIEW_TOOLS} to view tools.
        Press {RENTAL_REQUEST} to rental request.
        Press {RETURN_TOOL} to return tool.
        Press {MANAGE_USERS_AND_APPS} to manage users and full applications.
        Press {MANAGE_RENTAL} to manage rental.
        Press {VIEW_STATISTICS} to view statistics.
        Press {MANAGE_NEIGHBORHOOD_WAREHOUSE} to manage neighborhood warehouse.
        {'*' * 40}
        """
    user_input = int(input(menu_string))
    while not (SIGN_UP <= user_input <= MANAGE_NEIGHBORHOOD_WAREHOUSE):
        print("Invalid input! Please try again!")
        user_input = int(input(menu_string))

    return user_input


def sign_up():
    pass


def view_tools():
    pass


def rental_request():
    pass


def return_tool():
    pass


def manage_users_and_apps():
    pass


def manage_rental():
    pass


def view_statistics():
    pass


def manage_neighborhood_warehouse():
    pass


def menu():
    operation = handle_menu()
    if operation == SIGN_UP:
        sign_up()
    elif operation == VIEW_TOOLS:
        view_tools()
    elif operation == RENTAL_REQUEST:
        rental_request()
    elif operation == RETURN_TOOL:
        return_tool()
    elif operation == MANAGE_USERS_AND_APPS:
        manage_users_and_apps()
    elif operation == MANAGE_RENTAL:
        manage_rental()
    elif operation == VIEW_STATISTICS:
        view_statistics()
    else:
        manage_neighborhood_warehouse()


def run():
    session = Session()
    try:
        model = ModelManager()
        controller = ControllerManager(model)
        view = ViewManager(controller)
        model.add_observer(view)
        view.start()
        session.commit()
        menu()
    except:
        session.rollback()
        raise
    finally:
        session.close()



if __name__ == "__main__":
    run()

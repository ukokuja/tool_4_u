from sqlalchemy.orm import Session

from controller import ControllerManager
from model import ModelManager
from view import ViewManager


def run():
    session = Session()
    try:
        model = ModelManager()
        controller = ControllerManager(model)
        view = ViewManager(controller)
        model.add_observer(view)
        view.start()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()



if __name__ == "__main__":
    run()

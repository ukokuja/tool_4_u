from sqlalchemy.orm import Session

from controller import ControllerManager
from database import init_db
from model import ModelManager
from view import ViewManager


def run():
    session = Session()
    try:
        session = init_db()

        model = ModelManager(session)
        item = model.item.get(1)
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


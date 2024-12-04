from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.user_repository import UserRepository
from src.controllers.login_creator import LoginCreator
from src.views.login_creator_view import LoginCreatorView

def loign_creator_composer():
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)
    controller = LoginCreator(model)
    view = LoginCreatorView(controller)

    return view
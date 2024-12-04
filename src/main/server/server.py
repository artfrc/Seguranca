from flask import Flask
from src.models.sqlite.settings.db_connection_handler import db_connection_handler

from src.main.routes.bank_account_route import bank_routes_bp

db_connection_handler.connect()

app = Flask(__name__)
app.register_blueprint(bank_routes_bp)
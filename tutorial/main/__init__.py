from flask import Blueprint

bp = Blueprint('main', __name__)

from tutorial.main import routes

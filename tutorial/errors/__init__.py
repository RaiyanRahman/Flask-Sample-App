from flask import Blueprint

bp = Blueprint('errors', __name__)

from tutorial.errors import handlers
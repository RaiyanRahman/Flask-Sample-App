from flask import Blueprint

bp = Blueprint('auth', __name__)

from tutorial.auth import routes
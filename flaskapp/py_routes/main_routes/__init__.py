from flask import Blueprint

# main = Blueprint('main', __name__, template_folder='folder-name')
main = Blueprint('main', __name__)

from . import general_routes




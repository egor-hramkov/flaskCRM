from flask import Blueprint

users_bp = Blueprint('users', __name__)


@users_bp.route('/login')
def register():
    return 'Admin Login Page'


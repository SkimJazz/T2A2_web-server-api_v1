# Custom decorators

# Library and Package Imports
from flask_jwt_extended import get_jwt
from flask import jsonify
from functools import wraps


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        claims = get_jwt()
        if not claims['is_admin']:
            return jsonify({"message": "Admin privileges required."}), 401
        else:
            return fn(*args, **kwargs)
    return wrapper

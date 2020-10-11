from functools import wraps
from flask import request, abort
from flask import current_app


def require_apikey(view_function):
    """Decorate for requiring API key"""
    @wraps(view_function)
    def wrapper(*args, **kwargs):
        if request.headers.get('apiKey') and request.headers.get('apiKey') == current_app.config.get('API_KEY'):
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return wrapper

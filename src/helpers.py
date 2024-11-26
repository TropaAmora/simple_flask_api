from functools import wraps
from datetime import datetime
from http import HTTPStatus
from flask import jsonify

def validate_date_format(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validate_class_id(class_id: str) -> bool:
    """Function that validates student ids"""
    if class_id not in ['class21']:
        return False

    return True

def handle_errors(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({
                'error': str(e),
                'status': 'error'
            }), HTTPStatus.INTERNAL_SERVER_ERROR
    return wrapper


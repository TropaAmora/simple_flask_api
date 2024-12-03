"""File that initializes directories as libraries"""

from flask import Flask, jsonify
from http import HTTPStatus

from app.config.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.api.v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from app.helpers.helpers import handle_errors

    @app.route('/health', methods=['GET'])
    @handle_errors
    def health_check():
        return jsonify({
            'status': 'healthy',
            'version': '1.0.0'
        }), HTTPStatus.OK
    
    return app
from flask import Flask, jsonify, request
from http import HTTPStatus
from datetime import datetime
from typing import Tuple, Dict, Any

from app import create_app

app = create_app()

# Very important, this ensures it only calls the .run() method when called locally
if __name__ == '__main__':
    app.run(debug=False)
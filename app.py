from flask import Flask, jsonify, request
from http import HTTPStatus
from datetime import datetime
from typing import Tuple, Dict, Any

from src.helpers import validate_date_format, handle_errors, validate_class_id
from src.config import CONFIG
from src.models import Student, Class

app = Flask(__name__)

# Global variables: remove after
STUDENT_REF_COUNTER = 0
CLASS_REF_COUNTER = 0

# Route 2
@app.route('/api/v1/create_student', methods=['POST'])
@handle_errors
def create_student() -> Tuple[Dict[str, Any], int]:
    # Get JSON data from the request body
    data = request.get_json()

    # Get student info from query parameters
    #STUDENT_REF_COUNTER += 1
    #student_ref = STUDENT_REF_COUNTER
    student_ref = 1
    student_name = data.get('student_name')
    student_level = data.get('student_level')
    student_bd = data.get('student_bd')

    if not (student_name and student_level and student_bd):
        return(jsonify({
            'error': 'student_name, student_level and student_bd is required',
            'status': 'error'
        })), HTTPStatus.BAD_REQUEST
    
    student = Student(
        ref=student_ref,
        name=student_name,
        level=int(student_level),
        birthday_date=student_bd
    )

    if not student:
        return jsonify({
            'error': 'Error creating Student class',
            'status': 'error'
        }), HTTPStatus.BAD_REQUEST

    return jsonify({
        'result': student._get_dictionary(),
        'status': 'success'
    }), HTTPStatus.OK

@app.route('/api/v1/create_class', methods=['POST'])
@handle_errors
def create_class() -> Tuple[Dict[str, Any], int]:
    # Get JSON data from the request body
    data = request.get_json()

    # Get class attributes from query params
    # CLASS_REF_COUNTER += 1
    class_ref = 1
    class_level = data.get('class_level')
    class_day_date = data.get('class_day_date')
    class_start_time = data.get('class_start_time')
    class_end_time = data.get('class_end_time')

    if not (class_level and class_day_date and class_start_time and class_end_time):
        return jsonify({
            'error': 'class_level, class_day_date, class_start_time and class_end_time required',
            'status': 'error'
        }), HTTPStatus.BAD_REQUEST

    class_instance = Class(
        ref=class_ref,
        level=class_level,
        day_date=class_day_date,
        start_time=class_start_time,
        end_time=class_end_time
    )

    if not class_instance :
        return jsonify({
            'error': 'Unable to initiate Class instance',
            'status': 'error'
        }), HTTPStatus.BAD_REQUEST
    
    return jsonify({
        'result': class_instance._get_dictionary(),
        'status': 'success'
    }), HTTPStatus.OK

@app.route('//api/v1/get_students_from_class', methods=['GET'])
@handle_errors
def get_students() -> Tuple[Dict[str, Any], int]:
    # Get class from query parameters to query the students in that class
    class_id = str(request.args.get('class_id'))

    if not class_id:
        return jsonify({
            'error': 'class_id is required',
            'status': 'error'
        }), HTTPStatus.BAD_REQUEST
    
    if not validate_class_id(class_id=class_id):
        return jsonify({
            'error': 'class_id not found',
            'status': 'error'
        }), HTTPStatus.BAD_REQUEST
    
    result = CONFIG.get('result_students')

    return jsonify({
        'result': result,
        'status': 'success'
    }), HTTPStatus.OK


# Get example: GET /api/v1/dates?start_date=2024-01-01&end_date=2024-12-31
@app.route('/api/v1/get_classes', methods=['GET'])
@handle_errors
def get_classes() -> Tuple[Dict[str, Any], int]:
    # Get dates from query parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    # Validate presence of parameters
    if not start_date or not end_date:
        return jsonify({
            'error': 'Both start_date and end_date are required',
            'status': 'error'
        }), HTTPStatus.BAD_REQUEST
    
    # Validate date format
    if not validate_date_format(start_date) or not validate_date_format(end_date):
        return jsonify({
            'error': 'Dates must be in YYYY-MM-DD format',
            'status': 'error'
        }), HTTPStatus.BAD_REQUEST
    
    # Convert strings to datetime objects
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Validate date range
    if start > end:
        return jsonify({
            'error': 'start_date must be before or equal to end_date',
            'status': 'error'
        }), HTTPStatus.BAD_REQUEST
    
    result = CONFIG.get('result_classes')

    # Return processed dates
    return jsonify({
        'result': result,
        'status': 'success'
    }), HTTPStatus.OK


# Route 3
@app.route('/api/v1/resource3', methods=['GET'])
@handle_errors
def resource3():
    return jsonify({}), HTTPStatus.OK

# Route 4
@app.route('/api/v1/resource4', methods=['GET'])
@handle_errors
def resource4():
    return jsonify({}), HTTPStatus.OK

# Route 5
@app.route('/api/v1/resource5', methods=['GET'])
@handle_errors
def resource5():
    return jsonify({}), HTTPStatus.OK

# Health check endpoint
@app.route('/health', methods=['GET'])
@handle_errors
def health_check():
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0'
    }), HTTPStatus.OK

# Very important, this ensures it only calls the .run() method when called locally
if __name__ == '__main__':
    app.run(debug=False)
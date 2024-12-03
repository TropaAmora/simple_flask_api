# TODO: Add a utf-8 for codification
class Config:
    """Base config."""
    SECRET_KEY = 'your-secret-key'
    FLASK_APP = 'run.py'
    JSON_SORT_KEYS = False
    
class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    DEBUG = True

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


MOCK_DATA = {
    'result_classes': {
        'Monday': {
            '09:00-11:00': 'class1',
            '11:00-13:00': 'class2',
            '14:00-16:00': 'class3',
            '16:00-18:00': 'class4',
            '18:00-20:00': 'class5'
        },
        'Tuesday': {
            '09:00-11:00': 'class6',
            '11:00-13:00': 'class7',
            '14:00-16:00': 'class8',
            '16:00-18:00': 'class9',
            '18:00-20:00': 'class10',
        },
        'Wednesday': {
            '09:00-11:00': 'class11',
            '11:00-13:00': 'class12',
            '14:00-16:00': 'class13',
            '16:00-18:00': 'class14',
            '18:00-20:00': 'class15',
        },
        'Thursday': {
            '09:00-11:00': 'class16',
            '11:00-13:00': 'class17',
            '14:00-16:00': 'class18',
            '16:00-18:00': 'class19',
            '18:00-20:00': 'class20',
        },
        'Friday': {
            '09:00-11:00': 'class21',
            '11:00-13:00': 'class22',
            '14:00-16:00': 'class23',
            '16:00-18:00': 'class24',
            '18:00-20:00': 'class25',
        }
    }, 

    'result_students': {
        'result1': {
            'id': 1,
            'name': 'António Alves',
            'level': 5,
            'age': 26
        },
        'result2': {
            'id': 2,
            'name': 'Bernardo Terroso',
            'level': 1,
            'age': 20
        },
        'result3': {
            'id': 3,
            'name': 'Tomás Pacheco',
            'level': 4,
            'age': 30
        },
        'result4': {
            'id': 4,
            'name': 'Pedro Pacheco',
            'level': 3,
            'age': 22
        }
    }, 
}
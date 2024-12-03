import os 
from .config import config_by_name, MOCK_DATA

# Get config name from environment variable or default to 'development'
config_name = os.getenv('FLASK_CONFIG', 'development')

Config = config_by_name[config_name]
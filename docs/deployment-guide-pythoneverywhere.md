# PythonAnywhere Deployment Guide

## 1. Project Structure Setup
First, ensure your project structure is organized like this:
```
simple_flask_api/
├── requirements.txt
├── runtime.txt
├── wsgi.py
├── app.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── helpers.py
│   └── models.py
```

## 2. Create Required Files

### requirements.txt
```
Flask==2.0.1
gunicorn==20.1.0
python-dateutil==2.8.2
typing-extensions==4.1.1
```

### runtime.txt
```
python-3.9
```

### wsgi.py
```python
from app import app as application

if __name__ == '__main__':
    application.run()
```

## 3. PythonAnywhere Deployment Steps

1. **Sign up and login to PythonAnywhere**
   - Go to www.pythonanywhere.com
   - Create a new account or login

2. **Open a Bash console on PythonAnywhere**
   ```bash
   # Clone your repository (if using git)
   git clone https://github.com/yourusername/simple_flask_api.git
   
   # Create and activate virtual environment
   mkvirtualenv --python=/usr/bin/python3.9 myflaskapp
   workon myflaskapp
   
   # Install dependencies
   cd simple_flask_api
   pip install -r requirements.txt
   ```

3. **Configure Web App**
   - Go to Web tab in PythonAnywhere dashboard
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python 3.9
   - Configure the WSGI file (/var/www/yourusername_pythonanywhere_com_wsgi.py):

   ```python
   import sys
   import os
   
   # Add your project directory to the sys.path
   project_home = '/home/yourusername/simple_flask_api'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)
   
   # Set environment variables (if needed)
   os.environ['FLASK_ENV'] = 'production'
   
   from app import app as application
   ```

4. **Configure Virtual Environment**
   - In the Web app configuration:
   - Set the virtual environment path:
   ```
   /home/yourusername/.virtualenvs/myflaskapp
   ```

5. **Configure Static Files** (if needed)
   - In the Web app configuration:
   - Add static file mapping:
   ```
   URL: /static/
   Directory: /home/yourusername/simple_flask_api/static
   ```

## 4. Security Considerations

1. **Update config.py**
```python
import os

CONFIG = {
    # ... your existing config ...
}

# Add production configurations
PRODUCTION_CONFIG = {
    'SECRET_KEY': os.environ.get('SECRET_KEY', 'your-secret-key'),
    'DEBUG': False,
    'TESTING': False
}

# Update your CONFIG dictionary with production settings
if os.environ.get('FLASK_ENV') == 'production':
    CONFIG.update(PRODUCTION_CONFIG)
```

2. **Update app.py**
```python
from flask import Flask
from src.config import CONFIG

app = Flask(__name__)
app.config.update(CONFIG)

if __name__ == '__main__':
    app.run(debug=False)
```

## 5. Testing the Deployment

1. **Reload your web app** in PythonAnywhere dashboard

2. **Test your endpoints**
   - Your app will be available at: `yourusername.pythonanywhere.com`
   - Test the health check endpoint: `yourusername.pythonanywhere.com/health`
   - Test other API endpoints using Postman or curl

## 6. Monitoring and Maintenance

1. **Check error logs** in PythonAnywhere:
   - Error log: `/var/log/yourusername.pythonanywhere.com.error.log`
   - Access log: `/var/log/yourusername.pythonanywhere.com.access.log`

2. **Set up error notifications**:
```python
# In app.py
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('flask_app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Flask app startup')
```

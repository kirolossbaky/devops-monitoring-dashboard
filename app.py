import os
import logging
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import psutil
import platform
import socket

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# Configuration
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "devops-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///devops.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

db.init_app(app)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/alerts')
def alerts():
    return render_template('alerts.html')

@app.route('/api/metrics')
def get_metrics():
    try:
        metrics = {
            'cpu': psutil.cpu_percent(),
            'memory': psutil.virtual_memory().percent,
            'disk': psutil.disk_usage('/').percent,
            'hostname': socket.gethostname(),
            'platform': platform.platform(),
            'container': os.path.exists('/.dockerenv')
        }
        return jsonify(metrics)
    except Exception as e:
        logger.error(f"Error collecting metrics: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/system-info')
def get_system_info():
    try:
        info = {
            'hostname': socket.gethostname(),
            'platform': platform.platform(),
            'python_version': platform.python_version(),
            'cpu_count': psutil.cpu_count(),
            'total_memory': psutil.virtual_memory().total / (1024 * 1024 * 1024),  # Convert to GB
            'container': os.path.exists('/.dockerenv')
        }
        return jsonify(info)
    except Exception as e:
        logger.error(f"Error collecting system info: {str(e)}")
        return jsonify({'error': str(e)}), 500

with app.app_context():
    import models
    db.create_all()
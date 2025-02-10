import psutil
import time
from app import db
from models import Metric
import logging

logger = logging.getLogger(__name__)

def collect_metrics():
    """Collect system metrics and store in database"""
    try:
        cpu_percent = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        metrics = [
            Metric(name='cpu_usage', value=cpu_percent),
            Metric(name='memory_usage', value=memory.percent),
            Metric(name='disk_usage', value=disk.percent)
        ]

        db.session.bulk_save_objects(metrics)
        db.session.commit()
        logger.info("Metrics collected successfully")
    except Exception as e:
        logger.error(f"Error collecting metrics: {str(e)}")

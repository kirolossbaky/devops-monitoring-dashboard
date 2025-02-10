from app import db
from models import Alert, Metric
import logging

logger = logging.getLogger(__name__)

def check_alerts():
    """Check metrics and generate alerts if thresholds are exceeded"""
    try:
        # Get latest metrics
        cpu = Metric.query.filter_by(name='cpu_usage').order_by(Metric.timestamp.desc()).first()
        memory = Metric.query.filter_by(name='memory_usage').order_by(Metric.timestamp.desc()).first()

        # Check thresholds
        if cpu and cpu.value > 90:
            alert = Alert(
                title='High CPU Usage',
                description=f'CPU usage is at {cpu.value}%',
                severity='critical'
            )
            db.session.add(alert)

        if memory and memory.value > 85:
            alert = Alert(
                title='High Memory Usage',
                description=f'Memory usage is at {memory.value}%',
                severity='warning'
            )
            db.session.add(alert)

        db.session.commit()
    except Exception as e:
        logger.error(f"Error checking alerts: {str(e)}")

import pytest
from monitoring import collect_metrics
from models import Metric
from app import app, db

@pytest.fixture
def app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()

def test_collect_metrics(app_context):
    collect_metrics()
    metrics = Metric.query.all()
    assert len(metrics) > 0
    
    # Check if all required metrics are collected
    metric_names = [m.name for m in metrics]
    assert 'cpu_usage' in metric_names
    assert 'memory_usage' in metric_names
    assert 'disk_usage' in metric_names

import pytest
from app import app, db
from models import Metric, Alert

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_dashboard_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_alerts_route(client):
    response = client.get('/alerts')
    assert response.status_code == 200

def test_metric_model():
    metric = Metric(name='test_metric', value=50.0)
    assert metric.name == 'test_metric'
    assert metric.value == 50.0

def test_alert_model():
    alert = Alert(title='Test Alert', description='Test Description', severity='warning')
    assert alert.title == 'Test Alert'
    assert alert.severity == 'warning'

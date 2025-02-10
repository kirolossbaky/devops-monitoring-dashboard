
# DevOps Monitoring Dashboard

A comprehensive DevOps monitoring and automation project built with Flask and Python, focusing on real-time system metrics, performance tracking, and interactive dashboarding.

## Features

- Real-time system metrics monitoring (CPU, Memory, Disk)
- Interactive dashboard with live updates
- System information display
- Automated alerts for resource thresholds
- RESTful API endpoints for metrics
- Container-aware monitoring
- Dark/light theme support
- Responsive dashboard design
- SQLite database for metrics storage
- Automated testing suite

## Tech Stack

- Backend: Flask, SQLAlchemy
- Frontend: Chart.js, Bootstrap
- Testing: Pytest
- Monitoring: psutil
- Database: SQLite

## API Endpoints

- `/api/metrics` - Get real-time system metrics
- `/api/system-info` - Get system information
- `/alerts` - View system alerts

## Running the Application

```bash
python main.py
```

The application will be available at http://0.0.0.0:5000

## Testing

```bash
pytest tests/
```

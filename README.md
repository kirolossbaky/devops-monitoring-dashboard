# DevOps Monitoring Dashboard

A comprehensive DevOps monitoring and automation project built with Flask and Python, focusing on real-time system metrics, performance tracking, and interactive dashboarding.

## Features

- Real-time system metrics monitoring (CPU, Memory, Disk)
- Container-aware monitoring
- Dark/light theme support
- Responsive dashboard design
- System information display

## Running the Application

### Local Development
```bash
python main.py
```

### Using Docker
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or using Docker directly
docker build -t devops-dashboard .
docker run -p 5000:5000 devops-dashboard
```

The application will be available at http://localhost:5000

## Container Features

- Automatic container detection
- Resource usage monitoring within containers
- System information display
- Health checks for container orchestration

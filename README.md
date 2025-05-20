# BetterGR Setup

This repository contains setup scripts and configuration for the BetterGR project.

## Prerequisites

- Git
- Docker
- Docker Compose
- Python 3.8+
- Go 1.23+
- Node.js 18+

## Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/BetterGR/setup.git
   cd setup
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the setup script:
   ```bash
   python scripts/setup.py
   ```

4. Update the `.env` file with your configurations

## Development

There are two ways to run the project:

### 1. Using Docker (Production-like environment)

Start all services in containers:
```bash
docker-compose -f docker/docker-compose.yml up -d
```

### 2. Local Development

Run services directly on your machine (better for development):
```bash
python scripts/dev.py
```

This will start all services in development mode with hot-reload enabled.

## Project Structure

```
setup/
├── docker-compose.yml    # Production-like environment
├── scripts/
│   ├── setup.py             # Initial setup script
│   └── dev.py              # Local development script
├── .env.example           # Environment variables template
└── README.md
```

## Services and Ports

- Web App (Next.js) - http://localhost:3000
- API Gateway - http://localhost:1234
- Keycloak - http://localhost:8080
- Microservices:
  - Homework Service - :50053
  - Students Service - :50052
  - Courses Service - :50054
  - Staff Service - :50055
  - Grades Service - :50051

## Troubleshooting

If you encounter any issues:

1. Check if all required ports are available
2. Ensure all environment variables are properly set
3. Check service logs using `docker-compose logs <service-name>`
4. For local development, check the terminal output for each service
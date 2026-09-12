# Task 3 – Multi-Stage Docker Containerization & Optimization

Flask + PostgreSQL demo covering multi-stage Docker build, non-root execution,
Docker Compose, health checks, persistent PostgreSQL volume, and CI testing.

## Commands
docker compose up -d --build
docker compose ps
curl http://localhost:5000/health
curl -X POST http://localhost:5000/visit
curl http://localhost:5000/visits
docker image ls task3-docker-app
docker compose down

The named `pgdata` volume preserves database data across container restarts.
The CI workflow performs the real image-size check (<150MB).

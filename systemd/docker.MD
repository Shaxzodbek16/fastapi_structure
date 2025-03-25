# Start services in the background
docker-compose up -d

# Start services with logging in the foreground
docker-compose up

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# List running containers
docker-compose ps


# Build or rebuild services
docker-compose build

# Build a specific service without cache
docker-compose build --no-cache web

# Rebuild and start services
docker-compose up --build

# Execute a command in a running container
docker-compose exec web bash

# Run a one-off command in a service container
docker-compose run web python manage.py migrate

# Open a Python shell in the web container
docker-compose exec web python

# View resource usage of containers
docker-compose top

# Remove all stopped containers
docker-compose rm

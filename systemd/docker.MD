### Start services in the background
```bash
docker-compose up -d
```
### Start services with logging in the foreground
```bash
docker-compose up
```
### Stop all services
```bash
docker-compose down
```
### Stop and remove volumes
```bash
docker-compose down -v
```
### List running containers
```bash
docker-compose ps
```
### Build or rebuild services
```bash
docker-compose build
```
### Build a specific service without cache
```bash
docker-compose build --no-cache web
```
### Rebuild and start services
```bash
docker-compose up --build
```
### Execute a command in a running container
```bash
docker-compose exec web bash
```
### Run a one-off command in a service container
```bash
docker-compose run web python manage.py migrate
```
### Open a Python shell in the web container
```bash
docker-compose exec web python
```
### View resource usage of containers
```bash
docker-compose top
```
### Remove all stopped containers
```bash
docker-compose rm
```
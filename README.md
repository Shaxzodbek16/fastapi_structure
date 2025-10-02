# fastapi_structure

## FastAPI project structure with Docker, Database, SQLAlchemy, Alembic, Pydantic, JWT, Unit tests, GitHub Actions, and more.

# API

- **Repository**: Write database logic (e.g., get, insert, update, delete data).
- **Controller**: Write business logic (e.g., add discount to product, manage cart).
- **Constants**: Define constants (e.g., error messages, success messages).
- **Utils**: Write utility functions (e.g., send email, generate random values).
- **Models**: Define models (e.g., User, Product, Cart, Order).
- **Schemas**: Define schemas (e.g., UserSchema, ProductSchema, CartSchema, OrderSchema).
- **Routes**: Define routes (e.g., /user, /product, /cart, /order).

# Core

- **Database**: Manage database connections.
- **Models**: Define base models (e.g., Base).
- **settings.py**: Configure settings (e.g., database, email, environment variables).
- **Migrations**: Database migrations
- **Utils**: Write general utility functions (e.g., send email, generate random values).

# Server

- **Main**: Main file (e.g., main.py) where all routers are registered.
- **Middleware**: Define middleware (e.g., logging, authentication).

# Tests

- **Tests**: Write test (e.g., test_get_user, test_get_product, test_cart_operations).

# Others

- **Docker**: Write Docker files (e.g., Dockerfile, docker-compose.yml).
- **GitHub Actions**: Configure GitHub Actions (e.g., CI/CD).
- **.gitignore**: Define files and folders to ignore (e.g., .env, .vscode, __pycache__).
- **.env**: Define environment variables (e.g., DATABASE_URL, SECRET_KEY).

# How to run

1. **With Docker**:
   - Clone the repository
   - Create .env file and write environment variables
   - Run `docker-compose up --build`
   - Go to [http://localhost:8000/docs](http://localhost:8000/docs)

2. **Without Docker**:
   - Clone the repository
   - Create .env file and write environment variables
   - Run `pip install -r requirements.txt`
   - Run `alembic upgrade head`
   - Run `./run.sh` or `uvicorn app.server.main:create_app --reload --factory`
   - Go to [http://localhost:8000/docs](http://localhost:8000/docs)

# How to run tests

- Run `pytest -v`

# How to run alembic migrations

1. Run `alembic revision --autogenerate -m "create_user_table"`
2. Run `alembic upgrade head`

# How to use black

- Run `black . --exclude venv` to format all files except the venv folder

# ✅ Check TODOs in Code

- [ ] Perform a full-project search for `TODO`
- [ ] Review each occurrence
- [ ] Adjust or resolve as needed
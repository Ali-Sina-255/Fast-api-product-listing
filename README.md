# Fast-api-prodct-listing

# FastAPI Product Management API

A **FastAPI** project for managing products with **CRUD operations**, built using **SQLModel**, **PostgreSQL**, and **Docker**. This project demonstrates a modern async Python stack with database migrations using **Alembic**.

---

## Project Details

- **Framework:** FastAPI
- **ORM:** SQLModel / SQLAlchemy
- **Database:** PostgreSQL (Dockerized)
- **Migrations:** Alembic
- **Language:** Python 3.13
- **Docker Compose:** Included for PostgreSQL setup
- **API Features:**
  - Create, Read, Update, Delete (CRUD) Products
  - Async database operations
  - Schema validation with Pydantic

---

## Project Structure

.
├── apps/
│ ├── models/ # SQLModel & Pydantic models
│ ├── routes/ # API routes
│ └── server.py # FastAPI app entry
├── alembic/ # Database migrations
│ └── versions/ # Alembic migration files
├── Pipfile # Pipenv dependencies
├── Pipfile.lock
├── docker-compose.yml # PostgreSQL container setup
└── README.md

---

## Requirements

- Docker & Docker Compose
- Python 3.13+
- Pipenv

---

## Setup Instructions

### 1. Clone the repository

bash Terminal
git clone https://github.com/Ali-Sina-255/Fast-api-product-listing.git
cd Fast-api-product-listing

## 2. Create virtual environment & install dependencies

pipenv install
pipenv shell

## 3. Configure environment

.envs/.env.local
POSTGRES_USER=''
POSTGRES_PASSWORD=''
POSTGRES_DB=''
POSTGRES_HOST=''
POSTGRES_PORT=''

## 4. Start PostgreSQL using Docker Compose

docker compose up -d
docker ps

## 5. Run Alembic migrations

alembic upgrade head

## 6. Start FastAPI

uvicorn apps.server:app --reload

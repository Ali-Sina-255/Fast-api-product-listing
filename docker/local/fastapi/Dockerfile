# Dockerfile
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Install pipenv and project dependencies
RUN pip install pipenv
RUN pipenv install --system --deploy

# Copy the rest of the project
COPY . /app

# Expose port FastAPI will run on
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "apps.server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
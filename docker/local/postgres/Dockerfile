# Use official PostgreSQL image as base
FROM postgres:16-bullseye


ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=test_db

# Copy initialization SQL scripts
# Any .sql file in /docker-entrypoint-initdb.d/ will run on first container start
COPY init.sql /docker-entrypoint-initdb.d/

# Expose default PostgreSQL port
EXPOSE 5432

# Use default postgres entrypoint
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["postgres"]
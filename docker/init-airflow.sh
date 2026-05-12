#!/bin/bash

# Generate a Fernet key (if not already set)
if [ -z "$AIRFLOW__CORE__FERNET_KEY" ]; then
  export AIRFLOW__CORE__FERNET_KEY=$(openssl rand -base64 32)
fi

# Initialize Airflow DB
docker-compose -f docker/docker-compose.yml up airflow_postgres -d
sleep 10  # Wait for PostgreSQL to start
docker-compose -f docker/docker-compose.yml run --rm airflow_webserver airflow db init

# Create an admin user
docker-compose -f docker/docker-compose.yml run --rm airflow_webserver \
  airflow users create \
    --username admin \
    --firstname Macphalen \
    --lastname Oduor \
    --role Admin \
    --email mac0duor0fficial@gmail.com \
    --password admin
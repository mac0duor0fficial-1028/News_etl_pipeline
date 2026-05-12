# Use the official Airflow image
FROM apache/airflow:3.2.1

# Switch to the airflow user
USER airflow

# Install Python dependencies
WORKDIR /opt/airflow
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy scripts and configs
COPY scripts/ ./scripts/
COPY config/ ./config/
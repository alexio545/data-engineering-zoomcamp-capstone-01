import os

# POSTGRES PARAMS
user_name = os.getenv("POSTGRES_DOCKER_USER", "localhost")
POSTGRES_URL = f"jdbc:postgresql://postgres-server:5432/postgres"


POSTGRES_PROPERTIES = {
    "user": "postgres",
    "password":"postgres",
    "driver": "org.postgresql.Driver",
}

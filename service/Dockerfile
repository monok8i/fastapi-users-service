ARG PYTHON_VERSION=3.11.7
FROM python:${PYTHON_VERSION}-slim

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y build-essential

RUN python -m pip install poetry

WORKDIR /service/

COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --no-root


RUN chmod +x ./scripts/

ENTRYPOINT ./scripts/docker-entrypoint.sh
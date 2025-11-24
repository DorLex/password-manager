FROM python:3.12.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN python -m pip install -U pip &&  \
    python -m pip install poetry && \
    poetry config virtualenvs.create false

WORKDIR /proj

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root --without dev

COPY ./ ./

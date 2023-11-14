FROM python:3.11-slim as base
LABEL authors="eytes"

ENV POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR ~/db

COPY . ./

RUN apt update -y && \
    apt upgrade -y && \
    apt install -y --no-install-recommends curl build-essential && \
    curl -sSL https://install.python-poetry.org | python3 -

RUN poetry install

CMD ["bash"]

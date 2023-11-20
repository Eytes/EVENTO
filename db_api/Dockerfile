FROM python:3.11
MAINTAINER Eytes

WORKDIR /opt/EVENTO
COPY ./db-api ./db-api

# install poetry
RUN apt install pipx -y \
    && pipx install poetry

# install dependecie
RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--reload"]

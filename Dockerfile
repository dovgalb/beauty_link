FROM python:3.10
WORKDIR /code

EXPOSE 8088

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY . .

RUN poetry install

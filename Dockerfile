#FROM python:3.10
#WORKDIR /code
#
#EXPOSE 8088
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#RUN pip install poetry
#RUN poetry config virtualenvs.create false
#
#COPY . .
#
#RUN poetry install


FROM python:3.10 as requirements-stage

#
WORKDIR /tmp

#
RUN pip install poetry

#
COPY ./pyproject.toml ./poetry.lock* /tmp/

#
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

#
FROM python:3.10

#
WORKDIR /code

#
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY . .

#
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
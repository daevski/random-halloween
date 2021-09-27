FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
ENV POETRY_VERSION=1.1.6

COPY . /app
RUN pip install -r requirements.txt

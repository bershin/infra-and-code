FROM python:alpine3.22

ARG MY_ENV='dev'
ENV APP_ENVIRONMENT=${MY_ENV}

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY templates/ ./templates/

RUN pip install -r requirements.txt

RUN echo "Building for environment ${APP_ENVIRONMENT}"

CMD ["python", "app.py"]
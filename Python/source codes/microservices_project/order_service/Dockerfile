FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn requests
EXPOSE 80
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

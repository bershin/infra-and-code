FROM python:3.10-slim

## Environment Variables: Allows to pass configuration options such as database credentials or API keys into your containers without hardcoding them into your application.
# Prevents Python from generating those pyc files(when python runs it compiles py files into pyc, which are stored in the "pycache" folder) that are not necessary in a Docker environment.
ENV PYTHONDONTWRITEBYTECODE=1
# Forces the standard output and the standard error streams to be unbuffered, which allows you to see your log output in real time.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
# Option is used to prevent Pip from caching the downloaded packages.
# It's saying not to use a cache when downloading or when installing packages.
# So this is basically to reduce your image size.
RUN pip install --no-cache-dir -r requirements.txt 

# COPY app.py /app/
COPY main.py /app/

EXPOSE 8000

# First app refers to the file name of the Python file, which is app.py. So you just use the file name with the extension.
# Second app refers to the application instance created within the file that used to initialize the fast API instance.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
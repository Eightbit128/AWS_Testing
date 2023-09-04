FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

# Define the default command to run when starting the container
CMD ["python", "./reply_generator_django/manage.py", "runserver", "0.0.0.0:8000"]



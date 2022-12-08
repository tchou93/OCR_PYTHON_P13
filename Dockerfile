FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
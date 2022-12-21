FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE $PORT

CMD python manage.py collectstatic
CMD python manage.py runserver 0.0.0.0:$PORT
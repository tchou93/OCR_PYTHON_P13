FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
EXPOSE $PORT

RUN python manage.py collectstatic --noinput
CMD python manage.py runserver 0.0.0.0:$PORT
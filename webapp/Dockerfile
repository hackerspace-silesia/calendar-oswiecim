FROM python:3.9

LABEL org.opencontainers.image.authors="galuszkak@gmail.com"

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "run"]

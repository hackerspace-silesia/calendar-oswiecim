FROM python:3.8

MAINTAINER galuszkak@gmail.com

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "run"]

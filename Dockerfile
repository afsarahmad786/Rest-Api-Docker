FROM python:3.7

WORKDIR /user/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./sqlapp.py /user/src/app

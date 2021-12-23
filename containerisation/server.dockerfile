FROM python:3.10.1-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN export FLASK_APP=server
RUN export FLASK_ENV=development
CMD [ "flask", "run", "--host", "0.0.0.0" ]
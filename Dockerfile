FROM python:3.10-alpine

WORKDIR /log_parser_app

COPY requirements.txt .

COPY app.py .

COPY log_parser.py .

RUN pip install -r requirements.txt

EXPOSE 9999

CMD gunicorn -w 4 -b 0.0.0.0:9999 'app:app'


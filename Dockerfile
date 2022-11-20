FROM python:3.10-alpine

WORKDIR /log_parser_app

COPY requirements.txt .

COPY app.py .

COPY log_parser.py .

RUN pip install -r requirements.txt

EXPOSE 9999

CMD python app.py


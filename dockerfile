FROM python:3.12-alpine

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="svc-key.json"

COPY . .

CMD ["python3", "main.py"]
FROM python:3.12.3-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY portal-sdk.tar.gz portal-sdk.tar.gz
RUN pip install portal-sdk.tar.gz


COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]

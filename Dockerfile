FROM python:3.8

COPY prom_exporter.py /app/prom_exporter.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3", "/app/prom_exporter.py"]

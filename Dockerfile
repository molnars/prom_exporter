FROM python:3.8

COPY prom_exporter.py /app/prom_exporter.py
COPY requirements.txt /app/requirements.txt
COPY inotify-info /app/inotify-info
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x /app/inotify-info
CMD ["python3", "/app/prom_exporter.py"]

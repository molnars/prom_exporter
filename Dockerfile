FROM python:3.9

COPY prom_exporter.py /app/prom_exporter.py
COPY requirements.txt /app/requirements.txt
COPY inotify-info /app/inotify-info

RUN dnf install -y gcc-toolset-12
RUN scl enable gcc-toolset-12 bash

WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x /app/inotify-info
CMD ["python3", "/app/prom_exporter.py"]

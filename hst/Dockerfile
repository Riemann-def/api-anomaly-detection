FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY exporter.py .
COPY model_handler.py .
COPY prometheus_collector.py .
COPY model.pkl .

EXPOSE 8000

CMD ["python", "exporter.py"]

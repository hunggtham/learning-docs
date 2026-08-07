FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py pipeline.py ./
COPY prompts ./prompts
RUN useradd --create-home --uid 1000 worker && mkdir -p /data && chown -R worker:worker /data /app
USER worker
EXPOSE 8090
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8090"]

FROM python:3.11-slim

WORKDIR /app

COPY ExtractPython/requirements .

RUN pip install --no-cache-dir -r requirements

COPY ExtractPython/ /app/

CMD ["python", "main.py"]



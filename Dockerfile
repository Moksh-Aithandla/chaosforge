FROM python:3.12-slim

WORKDIR /app

COPY app/api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/api/ .

EXPOSE 8080

CMD ["python", "app.py"]
FROM python:3.12-slim

WORKDIR /app

COPY app/api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8080

CMD ["python", "-m", "app.api.app"]
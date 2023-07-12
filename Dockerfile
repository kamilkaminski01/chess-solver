FROM python:3.8-slim

EXPOSE 5000

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app .

CMD ["python", "app.py"]

FROM python:latest

WORKDIR /app

COPY app.py /app/app.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python","app.py"]

EXPOSE 5000
FROM python:3.10-alpine

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements
COPY . .

ENTRYPOINT [ "python3", "main.py" ]
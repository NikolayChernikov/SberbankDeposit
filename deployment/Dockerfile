FROM python:3.10-alpine

COPY deployment/requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app/src

ENTRYPOINT ["python","main.py"]
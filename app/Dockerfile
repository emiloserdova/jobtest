FROM python:3.9-alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["uvicorn", "--factory", "app.main:create_app", "--port=8000", "--host=0.0.0.0"]

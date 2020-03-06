FROM python:3.8-alpine
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN apk add --no-cache libffi-dev libressl-dev
COPY ./authentication /app
RUN pip3 install -r requirements.txt
RUN apk del .build-deps gcc musl-dev
CMD python3 main.py
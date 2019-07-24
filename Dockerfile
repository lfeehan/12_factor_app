FROM python:3.6.7-alpine

ARG http_proxy
ARG https_proxy

WORKDIR /usr/src/app

# Required for cython & pycrypto libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev

#for dev
RUN apk add --no-cache bash curl

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./run.py" ]

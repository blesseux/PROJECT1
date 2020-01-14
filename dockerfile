FROM alpine:3.7
RUN apk add python3 git
RUN mkdir /APP
WORKDIR /APP
RUN git clone https://github.com/blesseux/PROJECT1.git

FROM alpine:3.7
RUN apk add python3 git
RUN pip3 install requests
RUN mkdir /APP
WORKDIR /APP
RUN git clone https://github.com/blesseux/PROJECT1.git

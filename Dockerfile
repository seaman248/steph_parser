FROM python:3.5-alpine

ADD . /steph_parser
WORKDIR /steph_parser

RUN pip3 install -r requirements.txt

CMD python3 parse.py
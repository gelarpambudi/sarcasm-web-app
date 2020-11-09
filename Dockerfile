FROM python:3.8 

COPY . /sarcasm-web-app

WORKDIR /sarcasm-web-app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["main.py"]
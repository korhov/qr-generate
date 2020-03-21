FROM python:3.7

ENV HTTP_HOST 0.0.0.0
ENV HTTP_PORT 80
EXPOSE 80

RUN mkdir -p /home/qr

COPY requirements.txt /home/qr/requirements.txt

WORKDIR /home/qr/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY main.py /home/qr/main.py

CMD ["python", "./main.py"]

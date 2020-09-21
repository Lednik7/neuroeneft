FROM python:3.7

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN apt-get install libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev

RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "site/main.py"]

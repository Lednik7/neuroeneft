FROM python:3.7

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

COPY site /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "site/main.py"]

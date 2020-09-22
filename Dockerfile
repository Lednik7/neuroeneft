FROM python:3.7

RUN mkdir -p /usr/src/app/models/

COPY /site /usr/src/app/
COPY /models /usr/src/app/models/
COPY /logs /usr/src/app/logs/

RUN apt-get install libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev

RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir numpy==1.19.2
RUN pip3 install --no-cache-dir pandas==1.1.2
RUN pip3 install --no-cache-dir convertdate==2.2.2
RUN pip3 install --no-cache-dir LunarCalendar==0.0.9
RUN pip3 install --no-cache-dir holidays==0.10.3
RUN pip3 install --no-cache-dir pystan==2.19.1.1
RUN pip3 install --no-cache-dir SQLAlchemy==1.3.19
RUN pip3 install --no-cache-dir Flask-Login==0.5.0
RUN pip3 install --no-cache-dir Flask==1.1.2
RUN pip3 install --no-cache-dir matplotlib==3.3.2
RUN pip3 install --no-cache-dir fbprophet==0.6
RUN pip3 install --no-cache-dir gunicorn==20.0.4

WORKDIR /usr/src/app/

EXPOSE 10000
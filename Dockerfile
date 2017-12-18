FROM python:2.7

RUN \
  easy_install pip && \
  pip install bottle

COPY . /srvr/

EXPOSE 8888

CMD ["python", "/srvr/customerserver.py"]

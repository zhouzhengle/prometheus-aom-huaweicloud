FROM python:3.9-alpine
WORKDIR /usr/local/order-server
COPY requirements.txt /usr/local/order-server
COPY order-server.py /usr/local/order-server
# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5001
CMD [ "python", "order-server.py"]
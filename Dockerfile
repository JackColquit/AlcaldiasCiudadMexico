FROM python:3.9
COPY . .
RUN pip3 install mysql-connector-python
CMD ["python3", "metrobus.py"]

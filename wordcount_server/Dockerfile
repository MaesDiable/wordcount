FROM python:3.7.13-alpine3.15
COPY . /app
WORKDIR /app
RUN python3 -m venv ./
RUN pip3 install flask==2.1.1
EXPOSE 5000
CMD ["python","app.py"]
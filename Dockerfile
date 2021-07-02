FROM python:3.7-alpine
COPY .  /src
WORKDIR /src
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","src/main.py"]

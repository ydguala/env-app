FROM python:3.8.2-slim-buster

LABEL maintainer="ydguala"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN useradd -u 1000 user1
RUN chown -R user1 /app
USER user1

EXPOSE 8080/tcp

CMD [ "python3", "-u","api-server.py"]
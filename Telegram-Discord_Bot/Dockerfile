FROM python:3.12



# Install.
RUN \
  apt-get update && \
  apt-get -y dist-upgrade && \
  apt-get install -y python3 python3-pip redis

RUN pip install pyTelegramBotAPI typing datetime

WORKDIR /app
COPY . /app

USER root


# Start non-daemonized webserver
CMD ["python3", "Chatterbox.py"]

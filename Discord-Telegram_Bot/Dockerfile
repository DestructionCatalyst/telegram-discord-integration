FROM python:3.11


# Install/
RUN \
 apt-get update && \
 apt-get -y dist-upgrade && \
 apt-get install -y python3 python3-pip redis

RUN pip install discord.py
RUN pip install datetime
RUN pip install typing
RUN pip install redis

WORKDIR /app
COPY . /app

USER root
#ENTRYPOINT ["/bin/sh", "-c"]

# Start non-daemonized webserver
CMD ["python3", "./main.py"]

FROM debian:wheezy
MAINTAINER mdye <m-github@divisive.info>

RUN apt-get update && apt-get install -y python-dev python-pip

# copy project source into container
ADD python /src
RUN cd /src && python setup.py install

# copy data to-serve into container
ADD data /srv

# write configuration file
RUN echo "[server]\ndata_dir = /srv" > /etc/pgn_serve.ini

EXPOSE 8000
CMD ["python", "-m", "pgn_serve"]

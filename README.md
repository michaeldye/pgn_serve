# pgn_serve

This project is a tiny, self-contained Python webserver that serves PGN-formatted histortical Chess games. It is deployed in a [Docker](http://docker.io) container on the [Debian Wheezy](https://www.debian.org/releases/stable/) GNU/Linux system.

## Usage

### Mac OS Docker setup

Before executing Docker examples below, you'll need to set up a Docker environment to work in. If you'd like to run a Docker environment locally, try [Boot2Docker](https://docs.docker.com/installation/mac/). If you'd prefer to set up a remote service, consider [DigitalOcean](https://www.digitalocean.com/).

### Running the Container

Note that using Boot2Docker and the `-v` option to mount a data volume from the host container may require some fiddling, see https://github.com/boot2docker/boot2docker.

        docker run -i --rm -p 8000:8000 -v $(realpath data):/srv -t mdye/pgn_serve

Note that this command runs the container in the foreground, not as a daemon. A more realistic use of the `run` command uses the `-d` option to daemonize the container and `docker start` / `docker stop` commands to manipulate instances (see https://docs.docker.com/reference/run/). Note that daemonized instances retain state between stopping and starting again.

### Using the Service

        curl -i http://localhost:8000/pgn/random

## Building the Container Yourself

        docker build -t mdye/pgn_serve .

## Links

PGN-formatted Chess game files obtained from http://chessproblem.my-free-games.com/chess/games/Download-PGN.php

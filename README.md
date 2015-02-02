# pgn_serve

This project is a tiny, self-contained Python webserver that serves PGN-formatted histortical Chess games. It is deployed in a [Docker](http://docker.io) container on the [Debian Wheezy](https://www.debian.org/releases/stable/) GNU/Linux system.

## Usage

### Running the Container

        docker run -d --name pgn_serve -p 8000:8000 -t mdye/pgn_serve

### Using the Service

        curl -i http://localhost:8080/pgn/random

## Building the Container Yourself

        docker build --rm -t mdye/pgn_serve .

## Links

PGN-formatted Chess game files obtained from http://chessproblem.my-free-games.com/chess/games/Download-PGN.php

#!/usr/bin/env python2
# -*- coding: latin-1 -*-
""" HTTP Server for pgn_serve. """

__author__ = 'michael dye <m-github@divisive.info>'
__copyright__ = '2015 michael dye'
__license__ = 'GPL v3'

import pgnservice
import logging
from flask import Flask, request, make_response, jsonify, abort

app = Flask(__name__)
logger = logging.getLogger('pgn_serve.server')

def initialize(config):
    """ Initialize collaborating services for server """

    with app.app_context():
        # initialize PGNRepository with data directory to read from
        app.pgnRepository = pgnservice.PGNRepository(config.get('server', 'data_dir'))

@app.errorhandler(500)
def error(error):
    """ HTTP status code 500 error """

    return _api_ret({'error': 'server error'}, 500)

@app.errorhandler(404)
def not_found(error):
    """ HTTP status code 404 error """

    return _api_ret({'error': 'not found'}, 404)

@app.route('/pgn/random', methods=['GET'])
def pgn_random():
    """ Returns randomly-selected game. All attributes will be serialized as JSON if not None. """

    game = app.pgnRepository.random_game()
    return (jsonify({'game': dict((k,v) for k,v in game.__dict__.iteritems() if v is not None) }))

def _api_ret(payload, status=200):
    """ Prepares an HTTP response with JSON content type. """

    response = make_response(jsonify(payload), status)
    response.headers['Content-Type'] = 'application/json'
    return response

# vim: set ts=4 sw=4 expandtab:

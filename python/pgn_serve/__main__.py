#!/usr/bin/env python2
# -*- coding: latin-1 -*-
""" Entry point for pgn_serve server. """

__author__ = 'michael dye <m-github@divisive.info>'
__copyright__ = '2015 michael dye'
__license__ = 'GPLv3'

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import sys
import logging
import argparse
import ConfigParser

import server

def __main__():
    """ Starts pgn_serve webserver on port 8000. """

    # parse CLI args, config files; set up app then start it
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--configfile', type=str, default='/etc/pgn_serve.ini', help='path to configuration file')

    args = parser.parse_args()
    config = ConfigParser.ConfigParser()

    try:
        with open(args.configfile, 'r'):
            config.read(args.configfile)
    except IOError:
        print >>sys.stderr, 'Unable to read config file {}'.format(args.configfile)
        sys.exit(1)

    # establish logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logger = logging.getLogger('pgn_serve.main')

    # start app
    server.initialize(config)
    http_server = HTTPServer(WSGIContainer(server.app))
    http_server.listen(8000)
    logger.info('pgn_serve server starting')

    IOLoop.instance().start()


if __name__ == '__main__':
    __main__()

# vim: set ts=4 sw=4 expandtab:

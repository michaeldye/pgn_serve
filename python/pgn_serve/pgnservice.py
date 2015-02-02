#!/usr/bin/env python2
# -*- coding: latin-1 -*-
""" Handles PGN-formatted Chess game files for pgn_server """

__author__ = 'michael dye <m-github@divisive.info>'
__copyright__ = '2015 michael dye'
__license__ = 'GPL v3'

import os
from sets import Set
import logging
import random

import pgn

logger = logging.getLogger('pgn_serve.pgnservice')

class PGNRepository(object):
    """ A Repository for PGN-formatted Chess game files. Instantiation requires a path to a data directory from which PGN files can be read. """

    def __init__(self, dataDir):
        """ Construct PGNRepository.

        :param dataDir: Path to a directory from which PGN-formatted data files can be read.
        """

        self._games = []

        # read .pgn files and store PGNGame objects in self._games list
        for _, _, files in os.walk(dataDir):
            for fname in files:
                if fname.endswith('.pgn'):
                    try:
                        fpath = str(os.path.join(os.path.abspath(dataDir), fname))
                        self._games.extend(PGNRepository.read_pgn(fpath))
                    except Error as e:
                        logger.error('Failed to import games from file {}. Error: {}'.format(fpath, e))

        logger.info('Read {} games from dataDir {}'.format(len(self._games), dataDir))

    def random_game(self):
        """ Returns a random game from Repository. """

        game = self._games[random.randrange(0, len(self._games) + 1)]
        logger.info('Selected random game: {}'.format(game.dumps()))
        return game

    @staticmethod
    def read_pgn(fpath):
        """ Loads file at given fpath and returns list of PGNGame objects from it.

        :param fpath: Path to file containing PGN-formatted games
        """

        try:
            with open(fpath, 'r') as data:
                return pgn.loads(data.read())
        except IOError as e:
            raise RuntimeError('Unable to read PGN input file {}, {}'.format(fpath, e))

# vim: set ts=4 sw=4 expandtab:

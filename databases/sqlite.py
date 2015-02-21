#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import sqlite3
sys.path.append(os.path.dirname(__file__))
from .geanypysqldb import GeanyPySQLDB
sys.path.remove(os.path.dirname(__file__))

class GPS_sqlite(GeanyPySQLDB):

    def __init__(self, path=None):
        self.path = path

    def connect(self):
        if self.path is not None:
            self.connection = conn = sqlite3.connect(self.path)
        else:
            self.connection = None

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def connect_dialog(self):
		pass

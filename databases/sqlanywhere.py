#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import geany
import gtk

import sqlanydb
sys.path.append(os.path.dirname(__file__))
from .geanypysqldb import GeanyPySQLDB
sys.path.remove(os.path.dirname(__file__))


class GPS_sqlanywhere(GeanyPySQLDB):
    """ Special class for SAP Sybases SQLAnywhere and IQ databases based
        upon sqlanydb-python-driver. """

    def __init__(self, uid=None, pwd=None, server=None):
        self.userid = uid
        self.password = pwd
        self.server = server

    def connect(self):
        if self.connection is None:
            self.connection = sqlanydb.connect( userid=self.userid,
                                    password=self.password,
                                    server=self.server)

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import geany
import gtk

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

    def connect_dialog_box(self):
        self.vbox = gtk.VBox()
        self.hbox = gtk.HBox()
        self.vbox.pack_start(self.hbox,False, False, 0)

        label = gtk.Label("Please specify path of SQLite database")
        entry = gtk.Entry()

        self.hbox.pack_start(label,False, False, 0)
        self.hbox.pack_end(entry,False, False, 0)

        self.vbox.show_all()

        return self.vbox



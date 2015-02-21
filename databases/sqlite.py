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

    def connect_dialog(self):

        db_path = geany.dialogs.show_input(
            title="Path of sqlite DB",
            parent=geany.main_widgets.window,
            label_text="Please specify path of SQLite database")
        if os.path.isfile(db_path):
            self.path = db_path
            try:
                self.connect()
                print "Connected"
            except:
                geany.dialogs.show_msgbox("Could not create connection", gtk.MESSAGE_ERROR)
        else:
            geany.dialogs.show_msgbox("Seems not to be a valid path", gtk.MESSAGE_ERROR)



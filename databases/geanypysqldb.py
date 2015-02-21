#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GeanyPySQLDB():
    """ A generic class all database classes should inherit from to
        ensure an idendical api at minimum level.
        This is not really implementing anything. """
    connection = None

    def __init__(self, userid = None, password = None, host = None,
            database = None, odbc = None ):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def configuration_dialog(self):
        pass

    def connect_dialog(self):
        geany.dialogs.show_msgbox("Not yet implemented", gtk.MESSAGE_ERROR)



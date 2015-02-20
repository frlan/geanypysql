#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
import geany


try:
    import sqlanydb
    sqla = True
except:
    sqla = False




class GeanyPySQLDB():

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


class GPS_sqlanywhere(GeanyPySQLDB):

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


class GeanyPySQL(geany.Plugin):

    __plugin_name__ = "GeanyPySQL"
    __plugin_version__ = "0.1"
    __plugin_description__ = "Making an SQL client out of Geany"
    __plugin_author__ = "Frank Lanitz <frank@frank.uvena.de>"

    db = None
    cursor = None

    def __init__(self):

        # Logging
        geany.Plugin.__init__(self)

        # Adding menu entries
        # Add main menu entry for pluin and show it
        self.root_menu = gtk.MenuItem("_GeanyPySQL")
        self.root_menu.show_all()
        geany.main_widgets.tools_menu.append(self.root_menu)

        # Creating submenu
        plugin_menu = gtk.Menu()

        # And add submenu to global one
        self.root_menu.set_submenu(plugin_menu)

        # Now adding items to submenu
        mi_connect = gtk.MenuItem("_Connect")
        plugin_menu.append(mi_connect)

        mi_disconnect = gtk.MenuItem("_Disconnect")
        plugin_menu.append(mi_disconnect)

        # And callbacks
        mi_connect.connect("activate", self.on_click_connect, None)
        mi_disconnect.connect("activate", self.on_click_disconnect, None)

        plugin_menu.show_all()

    def cleanup(self):
        self.root_menu.destroy()

    def on_click_connect(self, widget, data):
        self.db = GPS_sqlanywhere(uid='dba', pwd='sql', server='foo')
        self.db.connect()

    def on_click_disconnect(self, widget, data):
        self.db.disconnect()


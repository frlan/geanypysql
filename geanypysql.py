#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
import geany
import sys
import os

# Will be used as kind of a plugin system for different database types
available_databases = {}

# This is a workaround to make Python find the submodules due to the way,
# GeanyPy is loading the Python plugins.
# After path has been updated, manually checking for database specific
# stuff.
sys.path.append(os.path.dirname(__file__))
try:
    from databases.sqlite import GPS_sqlite
    available_databases["SQLite3"] = {
             "name" : "SQLite3",
             "class" : GPS_sqlite}
except:
    print "failed: SQLite"

try:
    from databases.sqlanywhere import GPS_sqlanywhere

    available_databases["SQLAnywhere"] = {
         "name" : "SQLAnywhere",
         "class" : GPS_sqlanywhere}
except:
    print "failed: SQLAnywhere"


sys.path.remove(os.path.dirname(__file__))

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

        # Now adding submenus for each database typ
        # Not sure whether this really is good in reality
        # or it just sucks. We will see.
        for supported_database in available_databases.keys():
            # creating submenu for database typ
            tmp_db_mi = gtk.MenuItem(available_databases[supported_database]["name"])
            tmp_db_submenu = gtk.Menu()
            tmp_db_mi.set_submenu(tmp_db_submenu)

            # Adding basic functions to submenu
            tmp_connect = gtk.MenuItem("_Connect1")
            tmp_db_submenu.append(tmp_connect)

            tmp_disconnect = gtk.MenuItem("_Disconnect")
            tmp_db_submenu.append(tmp_disconnect)

            # Connecting callbacks
            tmp_connect.connect("activate", self.on_click_connect, supported_database)
            tmp_disconnect.connect("activate", self.on_click_disconnect, supported_database)

            plugin_menu.append(tmp_db_mi)

        # Finally, show all items
        plugin_menu.show_all()

    def cleanup(self):
        self.root_menu.destroy()

    def on_click_connect(self, widget, data):
        self.db = available_databases[data]["class"]()
        self.db.connect_dialog()

    def on_click_disconnect(self, widget, data):
        self.db.disconnect()


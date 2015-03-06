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

from ui import UI_connection_dialog

try:
    from databases.sqlite import GPS_sqlite
    available_databases["SQLite3"] = {
             "name" : "SQLite3",
             "class" : GPS_sqlite}
except:
    print "Could not load: SQLite"

try:
    from databases.sqlanywhere import GPS_sqlite

    available_databases["SQLAnywhere"] = {
             "name" : "SQLAnywhere",
             "class" : GPS_sqlanywhere}
except:
    print "Could not load: SQLAnywhere"


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

        # Adding basic functions to submenu
        mi_connect = gtk.MenuItem("_Connect")
        mi_disconnect = gtk.MenuItem("_Disconnect")
        mi_execute = gtk.MenuItem("_Execute")

        # Connecting callbacks
        mi_connect.connect("activate", self.on_click_connect)
        mi_disconnect.connect("activate", self.on_click_disconnect)
        mi_execute.connect("activate", self.on_click_execute)

        plugin_menu.append(mi_connect)
        plugin_menu.append(mi_disconnect)
        plugin_menu.append(mi_execute)

        # Finally, show all items
        plugin_menu.show_all()

    def cleanup(self):
        self.root_menu.destroy()

    def on_click_connect(self, widget):
        dialog = UI_connection_dialog(available_databases)
        dialog.dialog.run()

    def on_click_disconnect(self, widget, data):
        self.db.disconnect()

    def on_click_execute(self, widget, data):
        self.run_query()

    def run_query(self, *args):
        """ Actually run a query and return results"""
        query = geany.document.get_current().editor.scintilla.get_selection_contents()
        if len(query) == 0:
            query = geany.document.get_current().editor.scintilla.get_contents()
        try:
            return self.db.execute_query(query)
        except Exception, e:
            print e
            return None

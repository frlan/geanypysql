#!/usr/bin/env python
# -*- coding: utf-8 -*-

import geany
import gtk

class UI_connection_dialog():
    choosed_database = None
    database_vbox = None

    def __init__(self, available_databases):
        self.available_databases = available_databases
        self.dialog = gtk.Dialog(title="SQL Chooser",
                parent=geany.main_widgets.window,
                flags=0, buttons=None)
        combobox = gtk.combo_box_new_text()
        combobox.append_text('Please choose')
        for supported_database in self.available_databases.keys():
            combobox.append_text(supported_database)
            print supported_database
        combobox.set_active(0)
        combobox.connect('changed', self.changed_cb)
        self.dialog.vbox.add(combobox)
        self.dialog.vbox.set_resize_mode(gtk.RESIZE_IMMEDIATE)
        self.dialog.show_all()

    def changed_cb(self, combobox):
        model = combobox.get_model()
        index = combobox.get_active()
        if index:
            choosed_database = self.available_databases[model[index][0]]
            db = choosed_database["class"]()
            vbox = db.connect_dialog_box()
            self.dialog.vbox.add(vbox)
            self.database_vbox = vbox
        if not index:
            if self.database_vbox is not None:
                self.dialog.vbox.remove(self.database_vbox)
                self.database_vbox = None
            choosed_database = None
        return




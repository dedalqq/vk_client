from gi.repository import Gtk, GdkPixbuf, Gdk, WebKit


class gui_controller:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('gui/main.glade')
        self.builder.connect_signals(self)

        main_window = self.builder.get_object('main')
        users_list = self.builder.get_object('users_list')

        rendererText = Gtk.CellRendererText()

        column = Gtk.TreeViewColumn('name', rendererText, text=0)
        users_list.append_column(column)

        #store = self.builder.get_object('users')
        store = Gtk.ListStore(str)

        main_window.connect("destroy", self.destroy)
        main_window.show_all()




    def gtk_main(self):
        Gtk.main()

    def getGtk(self):
        return Gtk

    def destroy(window, self):
        Gtk.main_quit()

    def loadUsers(self):
        store = Gtk.ListStore(str)

        #for user in users:
        #    store.append(user)

        return store

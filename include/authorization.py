from gi.repository import Gtk, GdkPixbuf, Gdk, WebKit
import json
import os.path


class authorization:

    file_name = 'user_dara/user_info.json'

    def __init__(self, vk_api):
        self.vk_api = vk_api

    def showLoginWindow(self):
        wd = Gtk.Window()
        wd.set_title("example browser")
        wd.resize(600, 400)
        htm = WebKit.WebView()
        htm.open(self.vk_api.getLoginUrl())
        wd.connect("destroy", Gtk.main_quit)
        wd.add(htm)
        wd.show_all()

        Gtk.main()

    def getCurrentUser(self):
        if os.path.isfile(self.file_name) == False:
            return None
        user_profile_file = open(self.file_name)
        user_data = user_profile_file.read()
        return json.loads(user_data)

from gi.repository import Gtk, GdkPixbuf, Gdk, WebKit
import json
import os.path
import urlparse

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
        htm.connect("load-finished", self.onLoad)

        wd.connect("destroy", Gtk.main_quit)
        wd.add(htm)
        wd.show_all()

        Gtk.main()

    def onLoad(webview, frame, a):
        url = frame.get_uri()
        parsed = urlparse.urlparse(url)
        url_data = urlparse.parse_qs(parsed.query)
        #if 'access_token' in url_data:
        print url_data.access_token

    def getCurrentUser(self):
        if os.path.isfile(self.file_name) == False:
            return None
        user_profile_file = open(self.file_name)
        user_data = user_profile_file.read()
        return json.loads(user_data)

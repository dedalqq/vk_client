from gi.repository import Gtk, GdkPixbuf, Gdk, WebKit
import json
import os.path

class authorization:

    file_name = 'user_dara/user_info.json'

    def __init__(self, vk_api):
        self.vk_api = vk_api

    def showLoginWindow(self):
        self.wd = Gtk.Window()
        self.wd.set_title("example browser")
        self.wd.resize(600, 400)

        htm = WebKit.WebView()
        htm.open(self.vk_api.getLoginUrl())
        htm.connect("load-finished", self.onLoad)

        self.wd.connect("destroy", Gtk.main_quit)
        self.wd.add(htm)
        self.wd.show_all()

        Gtk.main()

    def onLoad(self, frame, a):
        url = frame.get_uri()
        data = url.split('#')
        print data
        for parameters in data[1].split('&'):
            vars = parameters.split('=')
            if vars[0] == 'access_token':
                self.vk_api.token = vars[1]
                self.getAndSaveUserInfo(self.vk_api.token)
                self.wd.destroy()
                Gtk.main_quit()

    def getAndSaveUserInfo(self, token):
        user_data = {
            'token': token
        }
        file = open(self.file_name, 'w')
        file.write(json.dumps(user_data))
        file.close()
        return None

    def getCurrentUser(self):
        if os.path.isfile(self.file_name) == False:
            return None
        user_profile_file = open(self.file_name)
        user_data = user_profile_file.read()
        data = json.loads(user_data)
        self.vk_api.token = data['token']
        return data

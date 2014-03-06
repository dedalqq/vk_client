#!/usr/bin/python

from gi.repository import Gtk, GdkPixbuf, Gdk, WebKit
import os, sys
import pprint
import json

import urllib2

users = ['omg', 'qq', 'ppc']

class GUI:
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

	if 0:
		vk = vk_api('')
		friends = vk.getFriends()

		for user in friends['response']:
		    store.append([user['last_name'] + ' ' + user['first_name']])

		users_list.set_model(store)
	else:
		wd = Gtk.Window()
		wd.set_title("example browser")
		wd.resize(600, 400)
		htm = WebKit.WebView()
		htm.open('https://oauth.vk.com/authorize?client_id=4089597&scope=messages%2Caudio%2Coffline%2Cstatus%2Cdocs%2Cnotes&redirect_uri=blank.html&display=popup&response_type=token')
		wd.add(htm)
		wd.show_all()







    def destroy(window, self):
        Gtk.main_quit()

    def loadUsers(self):
        store = Gtk.ListStore(str)

        for user in users:
            store.append(user)

        return store


class vk_api:

    token = ''

    API_URL = 'https://api.vk.com/method'

    def __init__(self, token):
        self.token = token

    def getUrl(self, method, param):
        parameters = []
        for name, value in param.iteritems():
            parameters.append(name + '=' + value)
        return self.API_URL + '/' + method + '?' + '&'.join(parameters)

    def getFriends(self):
        url = self.getUrl(
            'friends.get',
            {
                'access_token': self.token,
                'fields': 'uid,first_name,last_name,nickname'
            }
        )
        response = urllib2.urlopen(url)
        return json.loads(response.read())#.response
        #data = response.read())


def main():
    app = GUI()
    Gtk.main()


if __name__ == "__main__":
    sys.exit(main())


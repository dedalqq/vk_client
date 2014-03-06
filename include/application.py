from vk_api import vk_api
from gui_controller import gui_controller
from authorization import authorization

class application:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(application. cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def main(self):

        self.vk = vk_api()

        auth = authorization(self.vk)

        user_info = auth.getCurrentUser()

        self.gui = gui_controller()

        if user_info is None:
            auth.showLoginWindow()
            user_info = auth.getCurrentUser()

        self.init_app()




        self.gui.getGtk().main()


        return None

    def init_app(self):

        user_info = self.vk.getUserInfo()
        self.gui.setUserInfo(user_info)

        friends = self.vk.getFriends()
        #print friends
        return None
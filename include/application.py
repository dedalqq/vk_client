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

        vk = vk_api()

        auth = authorization(vk)

        user_info = auth.getCurrentUser()

        if user_info is None:
            auth.showLoginWindow()
        else:
            print 2



        gui = gui_controller()


        gui.getGtk().main()


        return None
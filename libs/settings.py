from dragonlib.settings.settings import Settings
from .const import SERVER_PREFIX


class MySettings(Settings):

    def get_prefix(self):
        '''
        override prefix
        '''
        return SERVER_PREFIX

settings = MySettings()
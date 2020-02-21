import json
import logging
from datetime import datetime
from dragonlib.web.web import APIHandler, SessionAPI
from libs.const import ERR_PREFIX
from libs.const import LANGUAGE_MAP
from libs.mymodels import Session

logger = logging.getLogger(__name__)


class BaseMixin(object):

    @property
    def redis(self):
        return self.application.settings['redis']
    
    @property
    def now(self):
        return datetime.now()

class BaseAPI(APIHandler, BaseMixin):
    ERR_PREFIX = ERR_PREFIX
    LANGUAGE_MAP = LANGUAGE_MAP


class UserSessionAPI(SessionAPI, BaseMixin):
    ERR_PREFIX = ERR_PREFIX
    LANGUAGE_MAP = LANGUAGE_MAP

    def get_current_user(self):
        if not self.sessionid:
            return None

        session = Session.get_first(id=self.sessionid)
        if not session:
            return
        return session.user
    
    @property
    def sessionid(self):
        return self.request.headers.get('sessionid', None)

    @property
    def userid(self):
        return str(self.current_user.id)
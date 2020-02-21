import logging
import requests
import json
import uuid
import random
from libs.base_handler import BaseAPI, UserSessionAPI
from datetime import datetime
from libs.settings import settings
from libs import const
from libs.handler_utils import require_parameters

logger = logging.getLogger(__name__)
errcode = '1107'

class GetAPI(UserSessionAPI):

    def api(self, params):
        return {
            "result": "ok"
        }

    def get(self, *args, **kwargs):
        self.write("ok")
        self.flush()
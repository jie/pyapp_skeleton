import json
import addict
import hashlib
import logging
from uuid import uuid4
from datetime import datetime
from unittest.mock import MagicMock
from base import BaseTest
from bson.objectid import ObjectId
from libs.const import ERR_PREFIX
from bson import ObjectId

logger = logging.getLogger(__name__)


class TestAppAPI(BaseTest):

    def setUp(self):
        super(TestAppAPI, self).setUp()
        self.init_admin(create_session=True)
        self.sessionid = str(self.session.id)

import sys
from os import path
sys.path.append(path.join(path.dirname(path.abspath(__file__)), ".."))
import os
import json
import unittest
import requests
import logging
from dragonlib.testing.testing import TestBase as Base
from libs.settings import settings
from libs.service import MicroService
from libs.const import SERVER_PREFIX


logger = logging.getLogger(__name__)

class TestService(MicroService):
    def init_database(self):
        pass


class BaseTest(Base):

    def setUp(self):
        super(BaseTest, self).setUp()
        self.redis = None
        self.init_redis()

    def tearDown(self):
        if self.redis:
            self.redis.client.flushdb()
        super(BaseTest, self).tearDown()

    def get_app(self):
        from routes import routes
        from libs import const

        micro_service = TestService(
            const.SERVER_NAME,
            routes,
            port=const.SERVER_PORT,
            settings=settings,
            autoreload=True,
            debug=True,
            prefix=const.SERVER_PREFIX
        )
        self.application = micro_service.application
        return self.application

    def init_redis(self):
        import redis
        from dragonlib.utils.redis_utils import RedisUtils
        pool = redis.ConnectionPool(
            host=self.getSetting('REDIS_HOST'),
            port=int(self.getSetting('REDIS_PORT')),
            db=self.getSetting('REDIS_DB'),
            decode_responses=True
        )
        redis_service = RedisUtils(pool)
        redis_service.get_client()
        self.redis = redis_service

    def getSetting(self, name):
        return getattr(settings, '%s%s' % (SERVER_PREFIX, name))



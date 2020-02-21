import tornado
import os
import logging
from dragonlib.web.micro_service import MicroService as MyMicroService

logger = logging.getLogger(__name__)

class MicroService(MyMicroService):

    def init_database(self):
        pass
    def start(self):
        port = self.port or self.getSetting('PORT')
        self.application.listen(port, xheaders=True)
        print('@starting development: %s' % port)
        tornado.ioloop.IOLoop.instance().start()

    def init_logger(self):
        super(MicroService, self).init_logger()
        # if self.getSetting('SENTRY_URL') and self.getSetting('DEPLOY') == 'production':
        #     import sentry_sdk
        #     sentry_sdk.init(self.getSetting('SENTRY_URL'))

import fire
from libs.settings import settings
from libs.service import MicroService
from routes import routes
from libs.const import ERR_PREFIX
from libs.const import SERVER_PREFIX

class WebServer(object):
    def start(self, name="pyapp", port=None, server_prefix="CONF_", err_prefix=10):
        ERR_PREFIX = err_prefix
        SERVER_PREFIX = server_prefix
        micro_service = MicroService(
            name,
            routes,
            settings=settings,
            autoreload=True,
            debug=True,
            port=port,
            prefix=server_prefix
        )
        micro_service.start()

if __name__ == "__main__":
    fire.Fire(WebServer)

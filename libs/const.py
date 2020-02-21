ERR_PREFIX = 10
SERVER_PREFIX = "CONF_"


ENABLE_STATUS = {
    'disable': 0,
    'enable': 1
}

LANGUAGE_MAP = {
    'en-US': {
        'application_not_found': 'Application not found',
    },
    'zh-CN': {
        'application_not_found': '应用不存在',
    }
}

def get_errcode(code):
    return ERR_PREFIX + code
import functools
import logging

logger = logging.getLogger(__name__)


def require_parameters(errcode, required=[], required_one=[]):
    def parameters_wraps(method):
        @functools.wraps(method)
        def wrapper(self, params):
            class_name = type(self).__name__
            logger.info("[REQ][%s]:%s" % (class_name, params))
            for param in required:
                if param not in params:
                    return self.fail(code=errcode, message='%s_required' % param)

            for items in required_one:
                all_result = []
                param_names = []
                for item in items:
                    param_names.append(item)
                    if item not in params:
                        all_result.append(False)
                    else:
                        all_result.append(True)
                if True not in all_result:
                    param_names.sort()
                    return self.fail(code=errcode, message='%s_required' % '_or_'.join(param_names))
            return method(self, params)
        return wrapper
    return parameters_wraps

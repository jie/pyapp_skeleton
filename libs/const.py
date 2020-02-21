ERR_PREFIX = 10
SERVER_PREFIX = "CONF_"


ENABLE_STATUS = {
    'disable': 0,
    'enable': 1
}

LANGUAGE_MAP = {
    'en-US': {
        'application_not_found': 'Application not found',
        'event_registed_error': 'You have successfully registered and do not need to register again',
        'user_unfocused_error': 'Please register after following the public number',
        'employee_id_name_not_matched': 'EmployeeID does not match name',
        'employee_not_found': 'EmployeeID does not exist',
        'registration_required': 'registration required',
        'event_poster_not_set': 'Poster template not found',
        'registration_error': 'Registration Error',
        'wait_to_create_poster': 'wait to create poster',
        'fail_to_create_poster': 'fail to create poster',
        'registration_poster_expired': 'Registration poster expired',
        'operating_too_frequent': 'Operating too frequent',
        'user_rank_not_found': 'User rank not found',
        'employee_status_error': 'Employee status error',
        'employee_full_name_required': 'Employee name length error'
    },
    'zh-CN': {
        'application_not_found': '应用不存在',
        'event_registed_error': '您已报名成功无需再次报名',
        'user_unfocused_error': '请关注公众号后报名 (如您已经关注公众号仍显示此错误，请重新关注)',
        'employee_id_name_not_matched': '员工号与姓名不匹配',
        'employee_not_found': '员工号不存在',
        'registration_required': '您还没有报名活动',
        'event_poster_not_set': '尚未设置活动海报模版',
        'registration_error': '报名错误，请联系管理员',
        'wait_to_create_poster': '正在生成海报...',
        'fail_to_create_poster': '生成海报时发生错误',
        'registration_poster_expired': '二维码海报已过期',
        'operating_too_frequent': '操作频繁，请稍后再试',
        'user_rank_not_found': '未找到您的排名',
        'employee_status_error': '员工状态错误',
        'employee_full_name_required': '名字长度最小为两个字符'
    }
}

def get_errcode(code):
    return ERR_PREFIX + code
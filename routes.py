from handlers import app_handler

routes = [
    # admin.menu_api
    (r'/hns/get', app_handler.GetAPI),
]
export CONF_DEPLOY=dev
export CONF_PORT=8084
export CONF_REDIS_HOST=127.0.0.1
export CONF_REDIS_PORT=6379
export CONF_REDIS_DB=0
export CONF_SENTRY_URL=https://3a91cbc190b3455f9ce57cd1a4420976@www.explorium.cn:9000/8
export CONF_WX_SHOWQRCODE="http://127.0.0.1:8080/cgi-bin/showqrcode?ticket={ticket}"
export CONF_WX_CREATESCENEQRCODE="http://127.0.0.1:8080/cgi-bin/qrcode/create?access_token={access_token}"
export CONF_WX_MENUCREATE="http://127.0.0.1:8080/cgi-bin/menu/create?access_token={access_token}"
export CONF_WX_GET_CURRENT_SELFMENU_INFO="http://127.0.0.1:8080/cgi-bin/get_current_selfmenu_info?access_token={access_token}"
export CONF_WX_MENUDELETE="http://127.0.0.1:8080/cgi-bin/menu/delete?access_token={access_token}"
export CONF_WX_AUTHORIZE_URL="http://open.weixin.qq.com/connect/oauth2/authorize?appid={appid}&redirect_uri={redirect_uri}&response_type=code&scope={scope}&state={state}#wechat_redirect"
export CONF_WX_ACCESS_URL="http://127.0.0.1:8080/sns/oauth2/access_token?appid={appid}&secret={secret}&code={code}&grant_type=authorization_code"
export CONF_WX_REFRESH_URL="http://127.0.0.1:8080/sns/oauth2/refresh_token?appid={appid}&grant_type=refresh_token&refresh_token={refresh_token}"
export CONF_WX_USERINFO_URL="http://127.0.0.1:8080/sns/userinfo?access_token={access_token}&openid={openid}&lang=zh_CN"
export CONF_WX_CLIENT_CREDENTIAL_URL="http://127.0.0.1:8080/cgi-bin/token?grant_type={grant_type}&appid={appid}&secret={secret}"
export CONF_WX_JSAPI_TICKET_URL="http://127.0.0.1:8080/cgi-bin/ticket/getticket?access_token={access_token}&type=jsapi"
export CONF_WX_JSCODE2SESSION_URL="http://127.0.0.1:8080/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code"
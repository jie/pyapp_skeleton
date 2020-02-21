# source dev.config.sh && nose2 -s  tests test_account.TestAccount -v
# source dev.config.sh && nose2 -s  tests test_user.TestUser -v
source test.config.sh && nose2 -s  tests test_wechat_api.TestWechatAPI -v

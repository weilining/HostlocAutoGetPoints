# -*- coding: utf8 -*-
from hostlocgetpoints import HostlocGetPoints
import os
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# python3 -m pip install -i https://pypi.python.org/simple python-telegram-bot pyaes requests --upgrade -t .
# python3 -m pip install -i https://pypi.python.org/simple -r requirements.txt -t .
# pip3 install -U requests pyaes python-telegram-bot
# 您可以使用 pip freeze > requirements.txt 生成本地环境下所有依赖的 requirements.txt 文件。
# 在 IDE 的终端中执行 pip install -r requirements.txt -t . 即可根据 requirements.txt 的配置安装依赖包。
# 我们还需要导出依赖，方便别人也能够用啊！很简单，进入到 virtual env，运行如下命令：pip freeze > requirements.txt
# 别人用的时候，pip install -r requirements.txt就可以安装对应的依赖啦。
# install
# python3 -m pip install --upgrade pip
# pip3 freeze > requirements.txt
# pip3 install -r requirements.txt -t .
def main_handler(event, context):
    usernames = os.environ["HOSTLOC_USERNAME"]
    passwords = os.environ["HOSTLOC_PASSWORD"]
    botToken = os.environ["BOT_TOKEN"]
    chatId = os.environ["CHAT_ID"]
    h = HostlocGetPoints()
    h.hostloc_get_points(usernames, passwords, botToken, chatId)


if __name__ == "__main__":
    main_handler("", "")

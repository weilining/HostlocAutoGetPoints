# -*- coding: utf8 -*-
from hostlocgetpoints import HostlocGetPoints
from printmyip import PrintMyIp
import telegram
from pyaes import AESModeOfOperationCBC
from urllib import parse
import requests
import textwrap
import re
import random
import time
import os
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


# python3 -m pip install -i https://pypi.python.org/simple pyaes requests python-telegram-bot --upgrade -t .
# python3 -m pip install -i https://pypi.python.org/simple -r requirements.txt -t .
# python3 -m pip install -U autopep8
# 您可以使用 pip freeze > requirements.txt 生成本地环境下所有依赖的 requirements.txt 文件。
# 在 IDE 的终端中执行 pip install -r requirements.txt -t . 即可根据 requirements.txt 的配置安装依赖包。
# 我们还需要导出依赖，方便别人也能够用啊！很简单，进入到 virtual env，运行如下命令：pip freeze > requirements.txt
# 别人用的时候，pip install -r requirements.txt就可以安装对应的依赖啦。


def main_handler(event, context):
    usernames = os.environ['HOSTLOC_USERNAME']
    passwords = os.environ['HOSTLOC_PASSWORD']
    botToken = os.environ['BOT_TOKEN']
    chatId = os.environ['CHAT_ID']
    h = HostlocGetPoints()
    h.hostloc_get_points(usernames, passwords, botToken, chatId)
    # return("Hello World")


if __name__ == "__main__":
    main_handler("", "")

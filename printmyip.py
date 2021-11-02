# -*- coding: utf-8 -*-
import requests

import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


class PrintMyIp():
    text = ''
    # 打印输出当前ip地址

    def print_my_ip(self):
        api_url = 'https://api.ipify.org/'
        try:
            res = requests.get(url=api_url)
            res.raise_for_status()
            res.encoding = 'utf-8'
            self.text = self.text + '当前使用 ip 地址：'+res.text+'\n'
            print('当前使用 ip 地址：' + res.text)
        except Exception as e:
            print("获取当前 ip 地址失败：" + str(e))
            self.text = self.text + '获取当前 ip 地址失败：' + str(e) + '\n'

    def returnIp(self):
        self.print_my_ip()
        return self.text
    # https://github.com/zaeval/freenom-dns-manage-library/blob/master/fnml.py

    def get_my_public_ip(self):
        ip_address = requests.get("http://ipecho.net/plain").text
        print(ip_address)
        # return ip_address


def main_handler(event, context):
    print("Hello World")


if __name__ == "__main__":
    main_handler("", "")

import telegram
from urllib import parse
import requests
import time


class TGPost():
    # TG推送
    def tgPost(self, botToken, chatId, text):
        try:
            print('开始推送')
            bot = telegram.Bot(token=botToken)
            bot.send_message(text=text, chat_id=chatId)
            print('推送成功')
        except Exception as e:
            # bot.send_message(text=str(e), chat_id=chat_id)
            print("推送失败"+str(e))


# TG推送
def post(bot_api, chat_id, text):
    print('开始推送')
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
    text = parse.quote(text)
    # 修改为自己的bot api token
    post_url = 'https://api.telegram.org/bot{}/sendMessage' \
        '?parse_mode=MarkdownV2&chat_id={}&text={}'.format(
            bot_api, chat_id, text)
    try:
        requests.get(post_url, headers=headers)
        print('推送成功')
    except Exception:
        print("推送失败")
        time.sleep(3)
        # 避免推送死循环
        try:
            requests.get(post_url, headers=headers)
        except Exception:
            pass


def main_handler(event, context):
    print("Hello World")


if __name__ == "__main__":
    main_handler("", "")

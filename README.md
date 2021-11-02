# HostlocAutoGetPoints

# 此代码是在inkuang大佬的基础上稍作改变，增加了TG推送。目前原库已GG，感谢MJJ的贡献

[inkuang/hostloc-auto-get-points: 自动获取 Hostloc 论坛的积分（由于 GitHub 使用政策的更新，原先在 GitHub 的仓库被封禁了，这里是备份） - hostloc_get_points.py at master - hostloc-auto-get-points - Ming's Git Server](https://git.inkuang.com/inkuang/hostloc-auto-get-points/src/branch/master/hostloc_get_points.py)

### 推送结果

![image](https://user-images.githubusercontent.com/64535826/118832486-3c1c8d80-b8f3-11eb-9d42-77bbd3b56e90.png)



### Actions secrets 设置
'HOSTLOC_USERNAME'  用户名，多个用','英文逗号隔开

'HOSTLOC_PASSWORD'  密码，多个用','英文逗号隔开，与用户名一一对应，不对应和上下数量不一致会报错。

'BOT_TOKEN'  TG机器人的TOKEN

'CHAT_ID'  你自己的chat_id

### TOKEN在@BotFather申请，chat_id可以通过机器人@userinfobot发送任意消息获取，返回的id即是chat_id

### 建议搬到私人库自己使用

![image](https://user-images.githubusercontent.com/64535826/118836731-b8fd3680-b8f6-11eb-8601-101e10c0533c.png)

![image](https://user-images.githubusercontent.com/64535826/118837247-3628ab80-b8f7-11eb-97c8-d6cf4bc84926.png)



### Action workflow设置
![image](https://user-images.githubusercontent.com/64535826/118829855-13939400-b8f1-11eb-8c95-44745e1242f5.png)

![image](https://user-images.githubusercontent.com/64535826/118829933-25753700-b8f1-11eb-9846-d0b983936763.png)

![image](https://user-images.githubusercontent.com/64535826/118830246-5eada700-b8f1-11eb-86b5-ca3c8547863f.png)

左边的删除，然后写入

    name: 'HostlocAutoGetPoints'
    
    on:
      push:
        branches: 
          - main
      schedule:
        - cron: '0 16 * * *'
    
    jobs:
      get_points:
        runs-on: ubuntu-latest
        steps:
        - name: 'Checkout codes'
          uses: actions/checkout@v2
        - name: 'Set python'
          uses: actions/setup-python@v1
          with:
            python-version: '3.x'
        - name: 'Install dependencies'
          run: python3 -m pip install -U requests pyaes telegram
        - name: 'Get points'
          env:
            HOSTLOC_USERNAME: ${{ secrets.HOSTLOC_USERNAME }}
            HOSTLOC_PASSWORD: ${{ secrets.HOSTLOC_PASSWORD }}
            BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
            CHAT_ID: ${{ secrets.CHAT_ID }}
          run: python3 index.py

![image](https://user-images.githubusercontent.com/64535826/118830589-a7656000-b8f1-11eb-9c2f-e1287a41ab11.png)

设置好Actions secrets后就可以在Action中运行了。如不运行在库中进行任意提交触发Action即可
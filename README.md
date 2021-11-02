## 推荐腾讯云函数

### 注册登录

微信扫描快速注册登录

[注册 - 腾讯云 (tencent.com)](https://cloud.tencent.com/register)

[登录 - 腾讯云 (tencent.com)](https://cloud.tencent.com/login)

### 创建scf

[新建scf](https://console.cloud.tencent.com/scf/list-create)

### 通过腾讯云函数（SCF）部署

------

#### 1、下载 SCF 版本的压缩包

此版本为特别版，支持通过腾讯云函数部署，并且将与主分支同步维护更新，推荐没有自己 VPS 服务器的用户使用，最新版本号为`v0.3.1_scf`。下载地址： https://github.com/luolongfei/freenom/releases/download/v0.3.1_scf/freenom-0.3.1_scf.zip

下载后你将得到一个 zip 文件，将 zip 文件放到你能找到的任意目录，后面我们将以 zip 文件的形式上传到腾讯云函数。

#### 2、创建腾讯云函数

直接访问腾讯云函数控制台创建云函数： https://console.cloud.tencent.com/scf/list-create ， 按照下图所示的说明进行创建。如果无法看清图片，可访问： https://github.com/luolongfei/freenom/blob/main/resources/screenshot/scf.png 或者 https://z3.ax1x.com/2021/10/14/5lMweU.png 查看原图。

[![scf01](https://camo.githubusercontent.com/3d69e3543159f7113e01343bd78b09829f92bfc51458be894136a97a40f82bc6/68747470733a2f2f7a332e617831782e636f6d2f323032312f31302f31342f356c4d7765552e706e67)](https://z3.ax1x.com/2021/10/14/5lMweU.png)

按照上图所示部署完成后，可以点击云函数的名称进入云函数管理画面，管理画面点击函数代码，然后往下翻可看到`部署`与`测试`按钮，点击`测试`，稍等几秒钟，即可看到输出日志， 根据输出日志判断配置以及部署是否正确。

[![scf02](https://camo.githubusercontent.com/5430efa8d5a6b8b3f7151738b7345e3763eac5b916153e4690f863b317b8ccb4/68747470733a2f2f7a332e617831782e636f6d2f323032312f31302f31342f356c336f48662e706e67)](https://z3.ax1x.com/2021/10/14/5l3oHf.png)

*有关腾讯云函数部署的内容结束。*

## GitHub Action

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

## 参考文献

此代码是在inkuang大佬的基础上稍作改变，增加了TG推送。目前原库已GG，感谢MJJ的贡献

[inkuang/hostloc-auto-get-points: 自动获取 Hostloc 论坛的积分（由于 GitHub 使用政策的更新，原先在 GitHub 的仓库被封禁了，这里是备份） - hostloc_get_points.py at master - hostloc-auto-get-points - Ming's Git Server](https://git.inkuang.com/inkuang/hostloc-auto-get-points/src/branch/master/hostloc_get_points.py)

### 
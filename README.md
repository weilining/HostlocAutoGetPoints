## 通过腾讯云函数（SCF）部署

### 注册登录

微信扫描快速注册登录

[注册 - 腾讯云 (tencent.com)](https://cloud.tencent.com/register)

[登录 - 腾讯云 (tencent.com)](https://cloud.tencent.com/login)

### 下载 SCF 版本的压缩包

[Releases · weilining/HostlocAutoGetPoints (github.com)](https://github.com/weilining/HostlocAutoGetPoints/releases)

下载后你将得到一个 zip 文件，将 zip 文件放到你能找到的任意目录，后面我们将以 zip 文件的形式上传到腾讯云函数。

#### 创建腾讯云函数

直接访问腾讯云函数控制台创建云函数：[新建 scf](https://console.cloud.tencent.com/scf/list-create) ， 按照下图所示的说明进行创建。如果无法看清图片，可访问： https://github.com/luolongfei/freenom/blob/main/resources/screenshot/scf.png 或者 https://z3.ax1x.com/2021/10/14/5lMweU.png 查看原图。

下图`php`改成`python3.6`，执行超时时间改为 900 秒

环境变量

```
'HOSTLOC_USERNAME'  用户名，多个用','英文逗号隔开
'HOSTLOC_PASSWORD'  密码，多个用','英文逗号隔开，与用户名一一对应，不对应和上下数量不一致会报错。
'BOT_TOKEN'  TG机器人的TOKEN
'CHAT_ID'  你自己的chat_id
```

TOKEN 在@BotFather 申请，chat_id 可以通过机器人@userinfobot 发送任意消息获取，返回的 id 即是 chat_id

[![scf01](https://camo.githubusercontent.com/3d69e3543159f7113e01343bd78b09829f92bfc51458be894136a97a40f82bc6/68747470733a2f2f7a332e617831782e636f6d2f323032312f31302f31342f356c4d7765552e706e67)](https://z3.ax1x.com/2021/10/14/5lMweU.png)

### 安装依赖

在“函数管理”页面中，选择**函数代码** > **代码编辑**，查看并编辑函数。

在 IDE 顶部的菜单栏**终端**中选择**新终端**，打开终端窗口。

在 IDE 的终端中执行 `pip install -r requirements.txt -t .` 即可根据 `requirements.txt` 的配置安装依赖包。

```bash
cd src  # 依赖库需要安装在与函数入口文件同一级的目录下，即需要进入`src`目录后再执行依赖安装操作。
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt -t .
```

安装完成后，在 IDE 左侧的文件树中查看已安装的依赖库。

单击**部署**后依赖库即可与函数代码一同打包上传到云端。

按照上图所示部署完成后，可以点击云函数的名称进入云函数管理画面，管理画面点击函数代码，然后往下翻可看到`部署`与`测试`按钮，点击`测试`，稍等几秒钟，即可看到输出日志， 根据输出日志判断配置以及部署是否正确。

[![scf02](https://camo.githubusercontent.com/5430efa8d5a6b8b3f7151738b7345e3763eac5b916153e4690f863b317b8ccb4/68747470733a2f2f7a332e617831782e636f6d2f323032312f31302f31342f356c336f48662e706e67)](https://z3.ax1x.com/2021/10/14/5l3oHf.png)

### 结果

_有关腾讯云函数部署的内容结束。_

## GitHub Action

封号警告！！！！

### 推送结果

![image](https://user-images.githubusercontent.com/64535826/118832486-3c1c8d80-b8f3-11eb-9d42-77bbd3b56e90.png)

### GitHub Actions secrets 设置

```
'HOSTLOC_USERNAME'  用户名，多个用','英文逗号隔开
'HOSTLOC_PASSWORD'  密码，多个用','英文逗号隔开，与用户名一一对应，不对应和上下数量不一致会报错。
'BOT_TOKEN'  TG机器人的TOKEN
'CHAT_ID'  你自己的chat_id
```

TOKEN 在@BotFather 申请，chat_id 可以通过机器人@userinfobot 发送任意消息获取，返回的 id 即是 chat_id

### 建议搬到私人库自己使用

![image](https://user-images.githubusercontent.com/64535826/118836731-b8fd3680-b8f6-11eb-8601-101e10c0533c.png)

![image](https://user-images.githubusercontent.com/64535826/118837247-3628ab80-b8f7-11eb-97c8-d6cf4bc84926.png)

### Action workflow 设置

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
          run: pip3 install -U requests pyaes python-telegram-bot
        - name: 'Get points'
          env:
            HOSTLOC_USERNAME: ${{ secrets.HOSTLOC_USERNAME }}
            HOSTLOC_PASSWORD: ${{ secrets.HOSTLOC_PASSWORD }}
            BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
            CHAT_ID: ${{ secrets.CHAT_ID }}
          run: python3 index.py

![image](https://user-images.githubusercontent.com/64535826/118830589-a7656000-b8f1-11eb-9c2f-e1287a41ab11.png)

设置好 Actions secrets 后就可以在 Action 中运行了。如不运行在库中进行任意提交触发 Action 即可

## 参考文献

此代码是在 inkuang 大佬的基础上稍作改变，增加了 TG 推送。目前原库已 GG，感谢 MJJ 的贡献

[inkuang/hostloc-auto-get-points: 自动获取 Hostloc 论坛的积分（由于 GitHub 使用政策的更新，原先在 GitHub 的仓库被封禁了，这里是备份） - hostloc_get_points.py at master - hostloc-auto-get-points - Ming's Git Server](https://git.inkuang.com/inkuang/hostloc-auto-get-points/src/branch/master/hostloc_get_points.py)

###

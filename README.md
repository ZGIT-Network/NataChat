# NataChat
一个简单的，支持 AES 加密通信的 HTML+Python 匿名在线聊天室

[DEMO](https://natachat.zyghit.cn) | [English](https://github.com/ZGIT-Network/NataChat/blob/main/README_en.md) | 中文

前端使用了MDUI，后端仅作消息转发，使用Python编写

### 部署服务端
#### 安装依赖项
``sudo apt-get install build-essential libssl-dev``

``pip3 install -r requirements.txt``
#### 启动服务端：
``python main.py``

服务端最低运行Python版本:  **Python3.10及以上版本** 

### 部署客户端
#### Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/zgit-network/natachat)

#### Github Pages
[Fork Repo](https://github.com/zgit-network/natachat/fork)

Start Settings > Pages > Branch > main > Save

#### 关于客户端：

目前,有两个客户端,分别为``standard client``和``client``两个版本

``client``版本目前是不开放公测的

[standard client](/) | [client](https://github.com/zgit-network/)

部署时需要注意：

如果网页配置了ssl证书，那么后端Server也应当配置SSL证书以便于通过wss链接，否则可能会出现问题。
***
欢迎协助编写本库，如果觉得有意思麻烦给个star呗！

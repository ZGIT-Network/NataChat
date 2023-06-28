# NataChat
一个简单的，支持 AES 加密通信的 HTML+Python 匿名在线聊天室

[DEMO](https://natachat.zyghit.cn) | [English](https://github.com/ZGIT-Network/NataChat/blob/main/README_en.md) | 中文

前端使用了MDUI，后端仅作消息转发，使用Python编写

***
#### 安装依赖项
``sudo apt-get install build-essential libssl-dev``

``pip3 install -r requirements.txt``
#### 启动服务端：
``python main.py``

服务端最低运行Python版本:  **Python3.10及以上版本** 

#### 关于客户端：

代码库内的``index.html``即标准客户端，仅包含在线客户端的使用更多功能请自行编写

部署时需要注意：

如果网页配置了ssl证书，那么后端Server也应当配置SSL证书以便于通过wss链接，否则可能会出现问题。
***
欢迎协助编写本库，如果觉得有意思麻烦给个star呗！

# NataChat

A simple HTML+Python anonymous online chat room that supports AES encrypted communication. Start Chat-Server.py directly.

[中文](README.md) | [繁体中文](README_tc.md) | [English](README_en.md)
 
 The front end uses [MDUI](https://mdui.org), and the back end only forwards messages. It is written in Python.

The code is relatively basic. The work of novice noob should not be sprayed by the boss.

Demo Site:[https://natachat.zyghit.cn/](https://natachat.zyghit.cn/)

***
#### Server side startup command:

``python Chat-Server.py``

Server Python version: **Python version above 3.10**

**Note: ** Please use ** pip install ** to install the following module dependencies before using:
````
asyncio
websockets
wheel
prompt_toolkit
logging
pycryptodome
pyDes
split
````

Or use this command:

``pip3 install  asyncio websockets wheel prompt_toolkit logging pycryptodome pyDes split``


****
#### About the client:

The ``index. html`` in the code base is the client, which only includes the use of online clients. If you need more, you can develop it yourself.

***

You are welcome to help write this library. If you find it interesting, please give it to a star!

Attention shall be paid during deployment:

If the web page is configured with an SSL certificate, the backend server should also be configured with an SSL certificate to facilitate linking through wss. Otherwise, problems may occur.

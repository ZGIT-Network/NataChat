# NataChat

A simple HTML5 + Python online chat room. Start main.py directly.

English|[中文](https://github.com/ZGIT-Network/NataChat)

The code is relatively basic. The work of novice Xiaobai should not be sprayed by the boss.

Demo Site:[https://natachat.zyghit.cn/](https://natachat.zyghit.cn/)

***
#### Server side startup command:

``python main.py``

Server Python version: **Python version above 3.10**

**Note: ** Please use ** pip install ** to install the following module dependencies before using:

````
asyncio
websockets
wheel
prompt_ toolkit
logging
````

Or use this command:

``pip install asyncio websockets wheel prompt_toolkit logging``

****
#### About the client:

The '` index. html' 'in the code base is the client, which only includes the use of online clients. If you need more, you can develop it yourself.

***

You are welcome to help write this library. If you find it interesting, please give it to a star!

Attention shall be paid during deployment:

If the web page is configured with an SSL certificate, the backend server should also be configured with an SSL certificate to facilitate linking through wss. Otherwise, problems may occur.

# NataChat
一個簡單的，支持AES加密通信的HTML+Python匿名線上聊天室，直接啟動Chat-Server.py即可

中文| [繁體中文]（README_tc.md）| [English]（README_en.md）

程式碼比較基礎，新手小白作品，大佬勿噴

前端使用了MDUI，後端僅作消息轉發，使用Python編寫

演示網站：[https://natachat.zyghit.cn/]（https://natachat.zyghit.cn/）

***
#### Server端啟動指令：
``python Chat-Server.py``

Server端Python版本：**Python3.10以上版本**

**注意：**使用前請使用**pip install**安裝下列模塊依賴：
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
或使用此指令：

``pip3 install -r requirements.txt``

****
####關於用戶端：

代碼庫內的``index.html``即用戶端，僅包含線上用戶端的使用，有更多需要可自行開發

網頁用戶端默認語言為英文，可自行翻譯或提交issue讓我搞個中文版

***
歡迎大佬協助編寫本庫，如果覺得有意思麻煩給個star唄！

部署時需要注意：
如果網頁配寘了ssl證書，那麼後端Server也應當配寘SSL證書以便於通過wss連結，否則可能會出現問題。

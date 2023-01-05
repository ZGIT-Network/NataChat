import websockets
import asyncio
import time
import atexit
import logging
from prompt_toolkit import prompt
import random
import string
from urllib.parse import unquote
import split
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


log_time = time.strftime('[%y-%m-%d %H:%M:%S]')
msg_time = time.strftime('[%Y-%m-%d %H:%M:%S]')

cs = {}

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '%s'
    return str.encode(value)
    
async def talk(websockets, path):
    try:
        while True:
            if (not websockets in cs.keys()):  # 新的访问申请
                LocalAESKEY = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
                userinfo = unquote(str(path[6:]),'utf-8')
                username = userinfo.split('||')[0]
                subaeskey = userinfo.split('||')[1]
                cs[websockets] = username
                msg = msg_time + 'Hello Welcome to Natachat Server! User ' + username
                print(log_time + 'New client connected, User IP' + websockets.remote_address[0] + ' Username '+username+'\nSubmitted AESKEY:'+subaeskey )
                logging.info('New client connected, User IP' + websockets.remote_address[0] + ' Username '+username+'\nSubmitted AESKEY:'+subaeskey )
                
                
            else:
                message = str(await websockets.recv())
                # AES-256-ECB
                key = subaeskey
                text = message
                aes = AES.new(add_to_16(key), AES.MODE_ECB)
                base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
                decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('%s','') 
                msg = f"{msg_time} {cs[websockets]} ({websockets.remote_address[0]}) #   { decrypted_text }"
                print("Not decrypted: "+message)
                print("Decrypted: "+msg)
                
            await asyncio.wait([ws.send(msg) for ws in cs.keys()])
    except Exception as err:
        logging.error(err)
        del cs[websockets]
        print(log_time + 'A WebSocket Client Disconnected. IP: ' + websockets.remote_address[0])
        logging.info('A WebSocket Client Disconnected. IP: ' + websockets.remote_address[0])


print(log_time + 'server running on [localhost:8765]')
logging.info('server running on [localhost:8765]')



start_server = websockets.serve(talk, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

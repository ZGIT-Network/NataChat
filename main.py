import websockets
import asyncio
import time
import atexit
from prompt_toolkit import prompt
import logging


log_time = time.strftime('\033[1m[%y-%m-%d %H:%M:%S]\033[0m')
msg_time = time.strftime('[%Y-%m-%d %H:%M:%S]')

cs = set()

async def talk(websockets, path):
    try:
        while True:

            if (not websockets in cs):  # 新的访问申请
                cs.add(websockets)
                msg = msg_time + 'Hello Welcome to Natachat Server! User' + str(websockets.remote_address)
                print(log_time + 'New client connected, User IP' + str(websockets.remote_address))
                logging.info('New client connected, User IP' + str(websockets.remote_address))
            else:
                msg = msg_time + ' User ' + str(websockets.remote_address) + 'Say: ' + str(await websockets.recv())

                print(msg)
            await asyncio.wait([ws.send(msg) for ws in cs])
    except Exception as err:
        cs.remove(websockets)
        print(log_time + 'A WebSocket Client Disconnected. IP' + str(websockets.remote_address))
        logging.info('A WebSocket Client Disconnected. IP' + str(websockets.remote_address))


print(log_time + 'server running on \033[7m[localhost:8765]\033[0m')
logging.warning('server running on \033[7m[localhost:8765]\033[0m')



start_server = websockets.serve(talk, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

import websockets
import asyncio
import time
import atexit
import logging
from prompt_toolkit import prompt



log_time = time.strftime('[%y-%m-%d %H:%M:%S]')
msg_time = time.strftime('[%Y-%m-%d %H:%M:%S]')

cs = {}

async def talk(websockets, path):
    try:
        while True:
            if (not websockets in cs.keys()):  # 新的访问申请
                username = path[6:]
                cs[websockets] = username
                msg = msg_time + 'Hello Welcome to Natachat Server! User ' + username
                print(log_time + 'New client connected, User IP' + websockets.remote_address[0] + ' Username '+username)
                logging.info('New client connected, User IP' + websockets.remote_address[0] + ' Username '+username)
            else:
                msg = f"{msg_time} {cs[websockets]} {websockets.remote_address[0]} Say: {str(await websockets.recv())}"
                print(msg)
            await asyncio.wait([ws.send(msg) for ws in cs.keys()])
    except Exception as err:
        logging.error(err)
        del cs[websockets]
        print(log_time + 'A WebSocket Client Disconnected. IP' + websockets.remote_address[0])
        logging.info('A WebSocket Client Disconnected. IP' + websockets.remote_address[0])


print(log_time + 'server running on [localhost:8765]')
logging.info('server running on [localhost:8765]')



start_server = websockets.serve(talk, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

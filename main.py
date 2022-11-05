import websockets
import asyncio
import time
log_time = time.strftime('[%y-%m-%d %H:%M:%S]')
msg_time = time.strftime('[%Y-%m-%d %H:%M:%S]')

cs = set()

async def talk(websockets, path):
    try:
        while True:
            if (not websockets in cs):   #新的访问申请
                cs.add(websockets)
                msg = msg_time +'Hello Welcome to Natachat Server! User' + str(websockets.remote_address)
                print(log_time +'New client connected, User IP'+ str(websockets.remote_address))
            else:
                msg = msg_time + ' User '+str(websockets.remote_address)+'Say:' +str(await websockets.recv())

                print(msg)
            await asyncio.wait([ws.send(msg) for ws in cs])
    except Exception as err:
        cs.remove(websockets)

print(log_time+'server running on [localhost:8765]')

start_server = websockets.serve(talk, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


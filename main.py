import websockets
import asyncio
import random
import string
from urllib.parse import unquote
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class ChatServer:
    def __init__(self, host, port, aes_key_length):
        self.host = host
        self.port = port
        self.aes_key_length = aes_key_length
        self.cs = {}

    async def start(self):
        print(f'Server running on {self.host}:{self.port}')
        start_server = websockets.serve(self.talk, self.host, self.port)
        async with start_server:
            await start_server.serve_forever()

    async def talk(self, websocket, path):
        try:
            if not self.is_valid_path(path):
                raise ValueError('Invalid path format')

            username, subaeskey = self.extract_user_info(path)
            if not self.is_valid_aes_key(subaeskey):
                raise ValueError('Invalid AES key length')

            async with websocket:
                if not self.is_new_user(websocket):
                    await websocket.send('Please enter a valid username and AES key to connect')
                    return

                self.add_user(websocket, username, subaeskey)

                while True:
                    message = await websocket.recv()

                    key = subaeskey.encode('utf-8')
                    text = message

                    try:
                        aes = AES.new(key, AES.MODE_ECB)
                        base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
                        decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('%s', '')
                        print(f"[{username}] ({websocket.remote_address[0]}) # {decrypted_text}")
                        await asyncio.wait([ws.send(decrypted_text) for ws in self.cs.keys()])
                    except ValueError as e:
                        print(f"[{username}] ({websocket.remote_address[0]}) # Invalid message format: {e}")
                        await websocket.send('Invalid message format')
                    except Exception as e:
                        print(f"[{username}] ({websocket.remote_address[0]}) # Error decrypting message: {e}")
                        await websocket.send('Error decrypting message')

        except ValueError as e:
            print("Invalid path or user info")
            await websocket.send("Invalid path or user info")
        except Exception as e:
            print("Error processing message")
            await websocket.send("Error processing message")
        finally:
            self.remove_user(websocket)

    def is_valid_path(self, path):
        return path.startswith('/chat/') and path.count('||') == 1

    def extract_user_info(self, path):
        userinfo = unquote(path[6:], 'utf-8')
        username, subaeskey = userinfo.split('||')
        return username, subaeskey

    def is_valid_aes_key(self, subaeskey):
        return len(subaeskey) == self.aes_key_length

    def is_new_user(self, websocket):
        return websocket not in self.cs.keys()

    def add_user(self, websocket, username, subaeskey):
        self.cs[websocket] = username
        print(f'New client connected, User IP {websocket.remote_address[0]} Username {username} Submitted AESKEY: {subaeskey}')

    def remove_user(self, websocket):
        if websocket in self.cs:
            print(f"A WebSocket Client Disconnected. IP: {websocket.remote_address[0]} Username: {self.cs[websocket]}")
            del self.cs[websocket]


if __name__ == '__main__':
    chat_server = ChatServer('localhost', 8765, 32)
    try:
        asyncio.run(chat_server.start())
    except Exception as e:
        print(e)

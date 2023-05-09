import aiohttp
import os
import random
import asyncio
import json
import aiofiles


class ChessClient:
    def __init__(self, loop) -> None:
        self.loop = loop or asyncio.get_event_loop()

        self.session = None

        self.local_username = ""

        self.access_token = ""
        self.server_username = ""
        self.rating = ""

        self.check_settings_file()

    def check_settings_file(self) -> None:
        if not os.path.exists(os.path.expanduser('~/Documents/MathsChess')):
            os.mkdir(os.path.expanduser('~/Documents/MathsChess'))

        if not os.path.exists(os.path.expanduser('~/Documents/MathsChess/GameSettings.ini')):
            with open(os.path.expanduser('~/Documents/MathsChess/GameSettings.ini'), 'w') as f:
                f.write(f"""[SETTINGS]
Username=Guest{random.randint(10000, 99999)}""")

        with open(os.path.expanduser('~/Documents/MathsChess/GameSettings.ini')) as fp:
            for line in fp:
                if line.startswith('Username='):
                    self.local_username = line.split('=')[1]

    async def update_settings(self, username: str) -> None:
        self.local_username = username

        async with aiofiles.open(os.path.expanduser('~/Documents/MathsChess/GameSettings.ini'), mode='w') as fp:
            await fp.write(f"""[SETTINGS]
Username={username}""")

    async def login(self, username: str) -> None:
        self.session = aiohttp.ClientSession()

        async with self.session.request(
            method="POST",
            url="http://mathschess.com/api/login",
            headers={
                "Authorization": self.local_username
            }
        ) as request:
            data = await request.json()
            print(json.dumps(data, sort_keys=False, indent=4))

            self.access_token = data['access_token']
            self.server_username = data['username']
            self.rating = data['rating']

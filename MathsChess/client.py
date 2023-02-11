import aiohttp


class ChessClient:
    def __init__(self) -> None:
        self.session = None

        self.access_token = ""
        self.username = ""
        self.rating = ""

    async def login(self, username: str) -> None:
        self.session = aiohttp.ClientSession()

        async with self.session.request(
            method="POST",
            url="http://localhost/api/login",
            headers={
                "Authorization": username
            }
        ) as request:
            data = await request.json()

            self.access_token = data['access_token']
            self.username = data['username']
            self.rating = data['rating']

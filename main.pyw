import MathsChess
import asyncio


client = MathsChess.ChessClient()


async def main() -> None:
    await client.login(username="mistxoli")

    window = MathsChess.GUI(client=client)
    window.resizable(width=False, height=False)

    await window.updater()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

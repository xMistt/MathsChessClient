# Hellew.
import MathsChess
import asyncio

loop = asyncio.get_event_loop()
client = MathsChess.ChessClient(loop=loop)


async def main() -> None:
    await client.login()

    window = MathsChess.GUI(client=client)
    window.resizable(width=False, height=False)

    await window.updater()


loop.run_until_complete(main())
loop.close()

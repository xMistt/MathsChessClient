import tkinter
import asyncio

from .mainmenu import MainMenu
from .settings import Settings
from .game import Game


class GUI(tkinter.Tk):
    def __init__(self, client: "ChessClient") -> None:
        tkinter.Tk.__init__(self)
        self.client = client

        self.geometry('800x600')
        self.configure(bg='#262422')
        self.title('MathsChess')

        photo = tkinter.PhotoImage(file="assets/icon.png")
        self.iconphoto(False, photo)

        self._frame = None
        self.frames = {
            "MainMenu": MainMenu,
            "Settings": Settings,
            "Game": Game
        }

        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class) -> None:
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    async def updater(self) -> None:
        while True:
            self.update()
            await asyncio.sleep(1/120)

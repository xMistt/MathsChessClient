import tkinter
import asyncio
import aiohttp

from tkinter import messagebox


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

            print(self.username)


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


class MainMenu(tkinter.Frame):
    def __init__(self, master) -> None:
        tkinter.Frame.__init__(self, master)
        canvas = tkinter.Canvas(
            self,
            bg='#262422',
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief='ridge'
        )
        canvas.place(x=0, y=0)

        self.logo = tkinter.PhotoImage(file='assets/logo.png')
        canvas.create_image(400.0, 57.0, image=self.logo)

        self.play_online_button_image = tkinter.PhotoImage(file='assets/online.png')
        play_online_button = tkinter.Button(
            image=self.play_online_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: messagebox.showerror(title='Error', message='Not implemented yet.'),
            relief='flat',
            bg='#262422',
            activebackground='#262422'
        )
        play_online_button.place(x=247.0, y=170.0, width=307.0, height=70.0)

        self.play_bots_button_image = tkinter.PhotoImage(file='assets/bots.png')
        play_bots_button = tkinter.Button(
            image=self.play_bots_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: messagebox.showerror(title='Error', message='Not implemented yet.'),
            relief='flat',
            bg='#262422',
            activebackground='#262422'
        )
        play_bots_button.place(x=247.0, y=265.0, width=307.0, height=70.0)

        self.settings_button_image = tkinter.PhotoImage(file='assets/settings.png')
        settings_button = tkinter.Button(
            image=self.settings_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: messagebox.showerror(title='Error', message='Not implemented yet.'),
            relief='flat',
            bg='#262422',
            activebackground='#262422'
        )
        settings_button.place(x=247.0, y=360.0, width=307.0, height=70.0)

        canvas.create_text(
            10,
            580,
            anchor='w',
            text=f'Logged in as: {master.client.username}',
            fill='#FFFFFF',
            font=('Montserrat ExtraBold', -23)
        )

        canvas.create_text(
            790,
            580,
            anchor='e',
            text=f'Rating: {master.client.rating}',
            fill='#FFFFFF',
            font=('Montserrat ExtraBold', -23)
        )

        canvas.pack()


client = ChessClient()


async def main() -> None:
    await client.login(username="mistxoli")

    window = GUI(client=client)
    window.resizable(width=False, height=False)

    await window.updater()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

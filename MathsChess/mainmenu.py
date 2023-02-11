import tkinter

from tkinter import messagebox


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
            command=lambda: master.switch_frame(master.frames["Settings"]),
            relief='flat',
            bg='#262422',
            activebackground='#262422'
        )
        settings_button.place(x=247.0, y=360.0, width=307.0, height=70.0)

        canvas.create_text(
            10,
            580,
            anchor='w',
            text=f'Logged in as: {master.client.server_username}',
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
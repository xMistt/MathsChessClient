import tkinter

from tkinter import messagebox


class Settings(tkinter.Frame):
    def __init__(self, master) -> None:
        tkinter.Frame.__init__(self, master)
        canvas = tkinter.Canvas(
            self,
            bg="#262422",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        self.logo = tkinter.PhotoImage(file='assets/logo.png')
        canvas.create_image(400.0, 57.0, image=self.logo)

        canvas.create_text(
            22,
            130,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Montserrat ExtraBold", 28 * -1)
        )

        edit_username = tkinter.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000000",
            highlightthickness=0,
            font=("Montserrat ExtraBold", -25)
        )
        edit_username.insert(0, master.client.server_username)
        edit_username.place(x=200, y=130, width=271, height=41)

        self.back_button_image = tkinter.PhotoImage(file='assets/back.png')
        back_button = tkinter.Button(
            image=self.back_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(master.frames["MainMenu"]),
            relief="flat",
            bg='#262422',
            activebackground='#262422'
        )
        back_button.place(x=7.0, y=510.0, width=145.0, height=71.0)

        self.apply_button_image = tkinter.PhotoImage(file='assets/apply.png')
        apply_button = tkinter.Button(
            image=self.apply_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.client.loop.create_task(self.change_username(username=edit_username.get())),
            relief="flat",
            bg='#262422',
            activebackground='#262422'
        )
        apply_button.place(x=327.0, y=510.0, width=145.0, height=71.0)

        canvas.pack()

    async def change_username(self, username: str) -> None:
        print(username)
        messagebox.showinfo(title='Error', message='Applied settings.')

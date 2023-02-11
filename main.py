import tkinter

window = tkinter.Tk()

window.geometry('800x600')
window.configure(bg='#262422')

canvas = tkinter.Canvas(window, bg='#262422', height=600, width=800, bd=0, highlightthickness=0, relief='ridge')
canvas.place(x=0, y=0)

logo = tkinter.PhotoImage(file='assets/logo.png')
displayed_logo = canvas.create_image(400.0, 57.0, image=logo)

play_online_button_image = tkinter.PhotoImage(file='assets/online.png')
play_online_button = tkinter.Button(
    image=play_online_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('button_3 clicked'),
    relief='flat',
    bg='#262422',
    activebackground='#262422'
)
play_online_button.place(x=247.0, y=170.0, width=307.0, height=70.0)

play_bots_button_image = tkinter.PhotoImage(file='assets/bots.png')
play_bots_button = tkinter.Button(
    image=play_bots_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('button_2 clicked'),
    relief='flat',
    bg='#262422',
    activebackground='#262422'
)
play_bots_button.place(x=247.0, y=265.0, width=307.0, height=70.0)

settings_button_image = tkinter.PhotoImage(file='assets/settings.png')
settings_button = tkinter.Button(
    image=settings_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('button_1 clicked'),
    relief='flat',
    bg='#262422',
    activebackground='#262422'
)
settings_button.place(x=247.0, y=360.0, width=307.0, height=70.0)

canvas.create_text(
    579.0,
    567.0,
    anchor='nw',
    text='RATING: 2859',
    fill='#FFFFFF',
    font=('Montserrat ExtraBold', 23 * -1)
)

canvas.create_text(
    4.0,
    562.0,
    anchor='nw',
    text='Logged in as: Magnus_Carlsen',
    fill='#FFFFFF',
    font=('Montserrat ExtraBold', 23 * -1)
)

window.resizable(width=False, height=False)
window.mainloop()

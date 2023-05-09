import tkinter

from tkinter import messagebox

chess_board = {
    'A1': {'x_y': (0, 0), 'default_piece': 'rook', 'colour': 'white', 'board_colour': 'dark'},
    'B1': {'x_y': (0, 0), 'default_piece': 'knight', 'colour': 'white', 'board_colour': 'light'},
    'C1': {'x_y': (0, 0), 'default_piece': 'bishop', 'colour': 'white', 'board_colour': 'dark'},
    'D1': {'x_y': (0, 0), 'default_piece': 'queen', 'colour': 'white', 'board_colour': 'light'},
    'E1': {'x_y': (0, 0), 'default_piece': 'king', 'colour': 'white', 'board_colour': 'dark'},
    'F1': {'x_y': (0, 0), 'default_piece': 'bishop', 'colour': 'white', 'board_colour': 'light'},
    'G1': {'x_y': (0, 0), 'default_piece': 'knight', 'colour': 'white', 'board_colour': 'dark'},
    'H1': {'x_y': (0, 0), 'default_piece': 'rook', 'colour': 'white', 'board_colour': 'light'},
    'A2': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'white', 'board_colour': 'dark'},
    'B2': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'white', 'board_colour': 'light'},
    'C2': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'white', 'board_colour': 'dark'},
    'D2': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'white', 'board_colour': 'light'},
    'E2': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'white', 'board_colour': 'dark'},
    'F2': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'white', 'board_colour': 'dark'},
    'G2': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'white', 'board_colour': 'light'},
    'H2': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'white', 'board_colour': 'dark'},
    'A3': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'B3': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'C3': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'D3': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'E3': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'F3': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'G3': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'H3': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'E4': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'F4': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'G4': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'H4': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'E5': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'F5': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'G5': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'H5': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'E6': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'F6': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'G6': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'dark'},
    'H6': {'x_y': (0, 0), 'default_piece': None, 'colour': None, 'board_colour': 'light'},
    'A7': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'black', 'board_colour': 'dark'},
    'B7': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'black', 'board_colour': 'light'},
    'C7': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'black', 'board_colour': 'dark'},
    'D7': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'black', 'board_colour': 'light'},
    'E7': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'black', 'board_colour': 'dark'},
    'F7': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'black', 'board_colour': 'light'},
    'G7': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'black', 'board_colour': 'dark'},
    'H7': {'x_y': (0, 0), 'default_piece': 'pawn', 'colour': 'black', 'board_colour': 'light'},
    'A8': {'x_y': (0, 0), 'default_piece': 'rook', 'colour': 'black', 'board_colour': 'light'},
    'B8': {'x_y': (0, 0), 'default_piece': 'knight', 'colour': 'black', 'board_colour': 'dark'},
    'C8': {'x_y': (0, 0), 'default_piece': 'bishop', 'colour': 'black', 'board_colour': 'light'},
    'D8': {'x_y': (0, 0), 'default_piece': 'queen', 'colour': 'black', 'board_colour': 'dark'},
    'E8': {'x_y': (0, 0), 'default_piece': 'king', 'colour': 'black', 'board_colour': 'light'},
    'F8': {'x_y': (0, 0), 'default_piece': 'bishop', 'colour': 'black', 'board_colour': 'dark'},
    'G8': {'x_y': (0, 0), 'default_piece': 'knight', 'colour': 'black', 'board_colour': 'light'},
    'H8': {'x_y': (0, 0), 'default_piece': 'rook', 'colour': 'black', 'board_colour': 'dark'}
}

class Game(tkinter.Frame):
    def __init__(self, master) -> None:
        self.master = master

        tkinter.Frame.__init__(self, master)
        canvas = tkinter.Canvas(
            self,
            bg = "#262422",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        self.board = tkinter.PhotoImage(file="assets/board.png")
        canvas.create_image(
            600.0,
            200.0,
            image=self.board
        )

        self.pawn = tkinter.PhotoImage(file="assets/pawn.png")
        a1_piece = tkinter.Button(
            image=self.pawn,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            bg='#262422',
            activebackground='#262422'
        )
        a1_piece.place(
            x=400.0,
            y=350.0,
            width=50.0,
            height=50.0
        )

        self.logo = tkinter.PhotoImage(file="assets/logo.png")
        canvas.create_image(
            705.0,
            575.0,
            image=self.logo
        )

        canvas.create_text(
            8.0,
            523.0,
            anchor="nw",
            text="You:\nmistxoli (390)",
            fill="#FFFFFF",
            font=("Montserrat ExtraBold", 28 * -1)
        )
        # window.resizable(False, False)
        # window.mainloop()
        canvas.pack()

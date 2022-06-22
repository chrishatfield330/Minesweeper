from cgitb import grey
from tkinter import *
import Settings
import Utilities
from Cell import Cell



root = Tk()
root.configure(bg="black")
root.geometry(f'{Settings.Width}x{Settings.Height}')
root.title("Minesweeper")
#root.resizable(False,False)

top_frame = Frame(
    root,
    bg='black',
    width= Utilities.widthPercentage(100),
    height= Utilities.heightPercentage(25)
)

top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper",
    font=('', 48)
)

game_title.place(
    x = Utilities.widthPercentage(25), y=0
)


left_frame = Frame(
    root,
    bg='black',
    width=Utilities.widthPercentage(25),
    height=Utilities.heightPercentage(75)
)

left_frame.place(x=0,
    y=Utilities.heightPercentage(25)
)

center_frame = Frame(
    root,
    bg='black',
    width=Utilities.widthPercentage(25),
    height=Utilities.heightPercentage(75)
)

center_frame.place(x=Utilities.widthPercentage(25),
    y=Utilities.heightPercentage(25)
)

for x in range(Settings.Grid_Size):
    for y in range(Settings.Grid_Size):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column= x,
            row= y
        )

Cell.randomize_mines()
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
    )


root.mainloop()
from tkinter import Button, Label
import random
import Settings
import ctypes
import sys


class Cell:
    all = []
    cell_count = Settings.Cell_Count
    cell_count_label_object = None
    def __init__(self, x, y, is_mine=False):
      self.is_mine = is_mine 
      self.is_opened = False
      self.is_marked = False
      self.cell_btn_object = None
      self.x = x
      self.y = y

      Cell.all.append(self)

    
    
    def create_btn_object(self, location):
        btn = Button(
            location,
            width = 12,
            height = 4,

        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text = f"Cells Left:{Cell.cell_count}",
            bg="black",
            fg="white",
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl
    
    
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == Settings.Mines_Count:
                ctypes.windll.user32.MessageBoxW(
            0,
            "Woo Hoo You Win!!",
            "Game Over",
            0
            )
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    
    def right_click_actions(self, event):
        if not self.is_marked:
            self.cell_btn_object.configure(
                bg="orange"
            )
            self.is_marked = True
        else:
            self.cell_btn_object.configure(
                bg="SystemButtonFace"
            )
            self.is_marked = False

    
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(
            0,
            "You clicked on a mine",
            "Game Over",
            0
            )
        
        #sys.exit()
        

    
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    
    @property
    def surrounded_cells_mines_length(self):
        i = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                i += 1
        return i

    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(
                text = self.surrounded_cells_mines_length
            )
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                )
            self.cell_btn_object.configure(
                bg="SystemButtonFace"
            )
        self.is_opened = True
    
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [
            cell for cell in cells if cell is not None
        ]
        return cells

    
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            Settings.Mines_Count
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
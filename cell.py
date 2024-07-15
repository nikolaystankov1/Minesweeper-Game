from tkinter import Button
import random

import settings

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button_object = None
        self.x = x  
        self.y = y

        Cell.all.append(self)



    def create_button_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-3>', self.right_click_actions) # Right Click

        self.cell_button_object = btn


    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def get_cell_by_axix(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell


    def show_cell(self):
        surrounded_cells = [
            self.get_cell_by_axix(self.x - 1, self.y -1),
            self.get_cell_by_axix(self.x - 1, self.y),
            self.get_cell_by_axix(self.x - 1, self.y + 1),
            self.get_cell_by_axix(self.x, self.y - 1),
            self.get_cell_by_axix(self.x + 1, self.y - 1),
            self.get_cell_by_axix(self.x + 1, self.y),
            self.get_cell_by_axix(self.x + 1, self.y + 1),
            self.get_cell_by_axix(self.x, self.y + 1),
        ]

        print(surrounded_cells)

    def show_mine(self):
        self.cell_button_object.configure(bg='red')

    def right_click_actions(self, event):
        print(event)
        print('I am right cliked!')


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self) -> str:
        return f'Cell({self.x}, {self.y})'
    

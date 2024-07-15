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
            text=f'{self.x},{self.y}'
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-3>', self.right_click_actions) # Right Click

        self.cell_button_object = btn


    def left_click_actions(self, event):
        print(event)
        print('I am left cliked!')

    def right_click_actions(self, event):
        print(event)
        print('I am right cliked!')


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.al, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self) -> str:
        return f'Cell({self.x}, {self.y})'
    

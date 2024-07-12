from tkinter import Button

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_button_object = None


    def create_button_object(self, location):
        btn = Button(
            location,
            text='Text',
        )
        self.cell_button_object = btn
"""Application for choosing dinners from databases and preparing needed ingredients for whole week"""

from tkinter import *
from tkinter_apps.DinnerApp.data import dinners_dict, dinners


class Dinner(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master.geometry("400x400")
        self.master.title("Our Family dinners")
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self.master, text="List of possible dinners:", font="bold, 18")
        self.lbl.grid(row=0, column=0, columnspan=4, pady=(10, 0))

        for index, dinner in enumerate(dinners_dict):
            self.lbl = Label(self.master, text=f'- {dinner["name"]}')
            self.lbl.grid(row=index + 1, column=0, padx=5, sticky=W)
            self.btn = Button(
                master=self.master,
                text="+",
                command=lambda ing=dinner["ingredients"]: self.ingredients_get(ing),
            )
            self.btn.grid(row=index + 1, column=1, pady=(5, 5))

    def ingredients_get(self, ingredients):
        dinner_counter = len(dinners_dict)
        for index, ingredient in enumerate(ingredients):
            self.name = Label(self.master, text=ingredient[0])
            self.name.grid(row=1+dinner_counter+index, column=0, columnspan=4, sticky=W)
            self.unit = Label(self.master, text=ingredient[2], width=5)
            self.unit.grid(row=1+dinner_counter+index, column=1, columnspan=4)
            self.quantity = Label(self.master, text=ingredient[1], width=5)
            self.quantity.grid(row=1+dinner_counter+index, column=2, columnspan=4)


if __name__ == "__main__":
    root = Tk()
    app = Dinner(master=root)
    app.mainloop()

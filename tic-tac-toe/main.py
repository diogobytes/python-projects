# Tic tac toe game

from tkinter import *

class TicTacToe:

  def __init__(self):
    root = Tk()
    root.title("Tic-Tac-Toe Game")
    self.create_grid(root)
    root.mainloop()

  def create_grid(self,root):
    for row in range(3):
      for col in range(3):
        btn = Button(root,text="",font="normal 20 bold",width=5,height=2)
        btn.grid(row=row,column=col)
  








if __name__ == '__main__':
  game = TicTacToe()
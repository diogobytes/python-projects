# Tic tac toe game

from tkinter import *
import random
class TicTacToe:

  def __init__(self):
    root = Tk()
    root.title("Tic-Tac-Toe Game")
    self.player = 'X'
    self.buttons = {}
    self.create_grid(root)
    root.mainloop()

  def create_grid(self,root):
    for row in range(3):
      for col in range(3):
        #test =  random.choice(self.moves)
        btn = Button(root, text="", font="normal 20 bold", width=5, height=2,
                             command=lambda r=row, c=col: self.on_button_click(r, c))
        btn.grid(row=row, column=col)
        self.buttons[(row, col)] = btn  # Store button reference for each position
  
  def on_button_click(self, row, col):
        btn = self.buttons[(row, col)]  # Get the button clicked
        if btn["text"] == "":  # If the button is not already clicked
            btn["text"] = self.player  # Set the text to the current player ("X" or "O")
            # Toggle between players
            self.player = 'O' if self.player == 'X' else 'X'
        self.game_over()

  #TODO: Game over results
  def game_over(self):

    # iterate over the same line
    for row in range(3):
      print(row)
      if self.buttons[(row,0)]["text"] == self.buttons[(row,1)]["text"] == self.buttons[(row,2)]["text"] != "":
       print("Game Over")
    
   

        
     
  

if __name__ == '__main__':
  game = TicTacToe()
  
  
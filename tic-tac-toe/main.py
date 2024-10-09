# Tic tac toe game

from tkinter import *
import random
NORM_FONT = ("Helvetica", 10)
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

  def winners_msg(self,msg):
    popup = Tk()
    popup.wm_title("Game over!")
    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Ok", command = popup.destroy)
    B1.pack()
    popup.mainloop()

  #TODO: Game over results
  def game_over(self):
    msg = f"The Winner is "
    # iterate over the rows
    for row in range(3):
      if self.buttons[(row,0)]["text"] == self.buttons[(row,1)]["text"] == self.buttons[(row,2)]["text"] != "":
        winner = self.buttons[(row,0)]["text"]
        self.winners_msg(msg + winner)
    # iterate over the cols
    for col in range(3):
      if self.buttons[(0,col)]["text"] == self.buttons[(1,col)]["text"] == self.buttons[(2,col)]["text"] != "":
        winner = self.buttons[(0,col)]["text"]
        self.winners_msg(msg + winner)
    if self.buttons[(0,0)]["text"] == self.buttons[(1,1)]["text"] == self.buttons[(2,2)]["text"] != "":
      winner = self.buttons[(0,0)]["text"]
      self.winners_msg(msg + winner)
    if self.buttons[(0,2)]["text"] == self.buttons[(1,1)]["text"] == self.buttons[(2,0)]["text"] != "":
      winner = self.buttons[(0,2)]["text"]     
      self.winners_msg(msg + winner)
      

if __name__ == '__main__':
  game = TicTacToe()
  
  
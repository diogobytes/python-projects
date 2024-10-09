# Tic tac toe game

from tkinter import *

PLAYER_X = "X"
PLAYER_O = "O"
NORM_FONT = ("Helvetica", 10)
GRID_SIZE = 3
class TicTacToe:

  def __init__(self):
    self.root = Tk()
    self.root.title("Tic-Tac-Toe Game")
    self.player = 'X'
    self.buttons = {}
    self.create_grid(self.root)
    self.root.mainloop()
    
  def create_grid(self,root):
    for row in range(GRID_SIZE):
      for col in range(GRID_SIZE):
        #test =  random.choice(self.moves)
        btn = Button(root, text="", font="normal 20 bold", width=5, height=2,
                             command=lambda r=row, c=col: self.on_button_click(r, c))
        btn.grid(row=row, column=col)
        self.buttons[(row, col)] = btn  # Store button reference for each position
  
  def on_button_click(self, row, col):
        btn = self.buttons[(row, col)]  # Get the button clicked
        if btn["text"] == "":  # If the button is not already clicked
            btn["text"] = self.player  # Set the text to the current player ("X" or "O")
            if self.check_winner(row,col):
               self.winners_msg(f"The winner is {self.player}")
            # Toggle between players
            self.player = PLAYER_O if self.player == PLAYER_X else PLAYER_X
        

  def winners_msg(self, msg):
      popup = Toplevel(self.root)
      popup.wm_title("Game Over!")
      label = Label(popup, text=msg, font=NORM_FONT)
      label.pack(side="top", fill="x", pady=10)
      B1 = Button(popup, text="Play Again", command=lambda: [self.reset_game(), popup.destroy()])
      B1.pack()

  def reset_game(self):
     print("Reset game")

  #TODO: Game over results
  def check_winner(self,row,col):
    print(row,col)
    # iterate over the rows
    if all(self.buttons[(r,col)]["text"] == self.player for r in range(GRID_SIZE)):
      return True
    # iterate over the cols
    if all(self.buttons[(row,c)]["text"] == self.player for c in range(GRID_SIZE)):
        return True

    if all( row == col and self.buttons[(i,i)]["text"] == self.player for i in range(GRID_SIZE)):
       return True 
    
      

if __name__ == '__main__':
  game = TicTacToe()
  
  
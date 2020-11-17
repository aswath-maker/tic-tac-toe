#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello world!')


# In[1]:


from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

#The variables we require to mention the players:
userA = StringVar()
userB = StringVar()
play1 = StringVar()
play2= StringVar()

#Information of Names to get from the user:
player1_name = Entry(tk, textvariable=play1, bd=7)
player1_name.grid(row=1, column=1, columnspan=9)
player2_name = Entry(tk, textvariable=play2, bd=7)
player2_name.grid(row=2, column=1, columnspan=9)

#Initializing some conditions:
click = True
initial = 0

#Initial state of the buttons before clicking:
def disabled():
  gameBtn1.configure(state=DISABLED)
  gameBtn2.configure(state=DISABLED)
  gameBtn3.configure(state=DISABLED)
  gameBtn4.configure(state=DISABLED)
  gameBtn5.configure(state=DISABLED)
  gameBtn6.configure(state=DISABLED)
  gameBtn7.configure(state=DISABLED)
  gameBtn8.configure(state=DISABLED)
  gameBtn9.configure(state=DISABLED)

#Defining message box for a particular input:
def btnClick(buttons):
  global click, initial, player2_name, player1_name, userA,userB
  if buttons["text"] == " " and click == True:
    	buttons["text"] = "X"
    	click = False
    	userB = play2.get() + " Wins!"
    	userA = play1.get() + " Wins!"
    	winCondition()
    	initial += 1


  elif buttons["text"] == " " and click == False:
    	buttons["text"] = "O"
    	click = True
    	winCondition()
    	initial += 1
  else:
    	tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Pressed!")

        #Defining conditions for winning the game:
def winCondition():
  if (gameBtn1['text'] == 'X' and gameBtn2['text'] == 'X' and gameBtn3['text'] == 'X' or
    	gameBtn4['text'] == 'X' and gameBtn5['text'] == 'X' and gameBtn6['text'] == 'X' or
    	gameBtn7['text'] =='X' and gameBtn8['text'] == 'X' and gameBtn9['text'] == 'X' or
    	gameBtn1['text'] == 'X' and gameBtn5['text'] == 'X' and gameBtn9['text'] == 'X' or
    	gameBtn3['text'] == 'X' and gameBtn5['text'] == 'X' and gameBtn7['text'] == 'X' or
    	gameBtn1['text'] == 'X' and gameBtn2['text'] == 'X' and gameBtn3['text'] == 'X' or
    	gameBtn1['text'] == 'X' and gameBtn4['text'] == 'X' and gameBtn7['text'] == 'X' or
    	gameBtn2['text'] == 'X' and gameBtn5['text'] == 'X' and gameBtn8['text'] == 'X' or
    	gameBtn7['text'] == 'X' and gameBtn6['text'] == 'X' and gameBtn9['text'] == 'X'):
    	disabled()
    	tkinter.messagebox.showinfo("Tic-Tac-Toe", userA)

  elif initial == 8:
    	tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a Tie")

  elif (gameBtn1['text'] == 'O' and gameBtn2['text'] == 'O' and gameBtn3['text'] == 'O' or
      	gameBtn4['text'] == 'O' and gameBtn5['text'] == 'O' and gameBtn6['text'] == 'O' or
      	gameBtn7['text'] == 'O' and gameBtn8['text'] == 'O' and gameBtn9['text'] == 'O' or
      	gameBtn1['text'] == 'O' and gameBtn5['text'] == 'O' and gameBtn9['text'] == 'O' or
      	gameBtn3['text'] == 'O' and gameBtn5['text'] == 'O' and gameBtn7['text'] == 'O' or
      	gameBtn1['text'] == 'O' and gameBtn2['text'] == 'O' and gameBtn3['text'] == 'O' or
      	gameBtn1['text'] == 'O' and gameBtn4['text'] == 'O' and gameBtn7['text'] == 'O' or
      	gameBtn2['text'] == 'O' and gameBtn5['text'] == 'O' and gameBtn8['text'] == 'O' or
      	gameBtn7['text'] == 'O' and gameBtn6['text'] == 'O' and gameBtn9['text'] == 'O'):
    	disabled()
    	tkinter.messagebox.showinfo("Tic-Tac-Toe", userB)
 
buttons = StringVar()

label = Label( tk, text="Player 1:", font='Arial', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)

label = Label( tk, text="Player 2:", font='Arial', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

# Styling the Game Buttons:

gameBtn1 = Button(tk, text=" ", font='Arial', bg='black', fg='white', height=5, width=10, command=lambda: btnClick(gameBtn1))
gameBtn1.grid(row=3, column=0)

gameBtn2 = Button(tk, text=' ', font='Arial', bg='black', fg='white', height=5, width=10, command=lambda: btnClick(gameBtn2))
gameBtn2.grid(row=3, column=1)

gameBtn3 = Button(tk, text=' ',font='Arial', bg='black', fg='white', height=5, width=10, command=lambda: btnClick(gameBtn3))
gameBtn3.grid(row=3, column=2)

gameBtn4 = Button(tk, text=' ', font='Arial', bg='black', fg='white', height=5, width=10, command=lambda: btnClick(gameBtn4))
gameBtn4.grid(row=4, column=0)

gameBtn5 = Button(tk, text=' ', font='Arial', bg='black', fg='white', height=5, width=10, command=lambda: btnClick(gameBtn5))
gameBtn5.grid(row=4, column=1)

gameBtn6 = Button(tk, text=' ', font='Arial', bg='black', fg='white', height=5, width=10,command=lambda: btnClick(gameBtn6))
gameBtn6.grid(row=4, column=2)

gameBtn7 = Button(tk, text=' ', font='Arial', bg='black', fg='white', height=5, width=10, command=lambda: btnClick(gameBtn7))
gameBtn7.grid(row=5, column=0)

gameBtn8 = Button(tk, text=' ', font='Arial', bg='black', fg='white', height=5, width=10, command=lambda: btnClick(gameBtn8))
gameBtn8.grid(row=5, column=1)

gameBtn9 = Button(tk, text=' ', font='Arial', bg='black', fg='white', height=5, width=10, command=lambda: btnClick(gameBtn9))
gameBtn9.grid(row=5, column=2)

#To display the created graphic window:

tk.mainloop()


# In[ ]:





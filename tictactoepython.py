
from tkinter import *
from tkinter import messagebox
#from gtts import gTTS
root=Tk()
root.title("Tic Tac Toe")
global bclick
bclick=True

def close():
    exit()

def reset():
    button1["text"]=""
    button2["text"]=""
    button3["text"]=""
    button4["text"]=""
    button5["text"]=""
    button6["text"]=""
    button7["text"]=""
    button8["text"]=""
    button9["text"]=""


def winMethod():
      if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
          button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
          button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
          button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
          button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
          button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" or
          button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
          button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"
          ):


          messagebox.showinfo( "Winning Message", "X is WINNER")
          reset()
      if (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
          button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
          button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
          button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
          button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
          button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" or
          button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
          button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"
          ):
         messagebox.showinfo( "Winning Message", "O is WINNER")
         reset()

def tictactoe(buttons):
    global bclick
    if buttons["text"]=="" and bclick==True:
        buttons["text"]="X"
        bclick=False
        winMethod()
    elif buttons["text"]=="" and bclick==False:
        buttons["text"]="O"
        bclick=True
        winMethod()



button1=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button1))
button1.grid(row=1,column=0)
button2=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button2))
button2.grid(row=1,column=1)
button3=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button3))
button3.grid(row=1,column=2)
button4=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button4))
button4.grid(row=2,column=0)
button5=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button5))
button5.grid(row=2,column=1)
button6=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button6))
button6.grid(row=2,column=2)
button7=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button7))
button7.grid(row=3,column=0)
button8=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button8))
button8.grid(row=3,column=1)
button9=Button(root,text="",font=('Arial 30 bold'),height=1,width=2,command=lambda :tictactoe(button9))
button9.grid(row=3,column=2)

button10=Button(root,text="Reset Game ",font=('Arial 9 bold'),height=1,width=6,command=reset)
button10.grid(row=4,column=0,columnspan=3,sticky=S+N+E+W)
button11=Button(root,text="Exit Game ",font=('Arial 9 bold'),height=1,width=6)
button11.grid(row=5,column=0,columnspan=3,sticky=S+N+E+W)

root.resizable(0,0)  # Dsabling WIndow Resize

root.mainloop()

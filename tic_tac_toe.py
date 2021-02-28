import tkinter as tk
import tkinter.messagebox
from tkinter import *

root = tk.Tk()
# root.geometry("1350x750+0+0")
root.title("Tic-Tac-Toe Game!!!")
root.configure(background="Cadet Blue")

roo1 = tk.Tk()  # new window for menu options: 1- computer vs player 2- player vs player

Tops = Frame(root, bg='Cadet Blue', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

Main_game_title = Label(Tops, font=('arial', 50, 'bold'), text="Advanced Tic-Tac-Toe Game!", bd=21, bg="Cadet Blue",
                        fg="Cornsilk", justify=CENTER)
Main_game_title.grid(row=0, column=0)

MainFrame = Frame(root, bg='Powder Blue', bd=10, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
RightFrame.pack(side=RIGHT)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
RightFrame2.grid(row=1, column=0)

PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

Label_PlayerX = Label(RightFrame1, font="arial", text="Player 1 (X): ", padx=2, pady=2, bg="Cadet Blue")
Label_PlayerX.grid(row=0, column=0, sticky=W)
Text_PlayerX = Label(RightFrame1, font="arial", fg="black", textvariable=PlayerX, width=14,
                     justify=LEFT).grid(row=0, column=1)

Label_PlayerO = Label(RightFrame1, font="arial", text="Player 2 (O): ", padx=2, pady=2, bg="Cadet Blue")
Label_PlayerO.grid(row=1, column=0, sticky=W)
Text_PlayerO = Label(RightFrame1, font="arial", fg="black", textvariable=PlayerO, width=14,
                     justify=LEFT).grid(row=1, column=1)

bclick = True
flag = 1

buttons = tk.StringVar()


def disableButtons():
    button1.configure(state="disabled")
    button2.configure(state="disabled")
    button3.configure(state="disabled")
    button4.configure(state="disabled")
    button5.configure(state="disabled")
    button6.configure(state="disabled")
    button7.configure(state="disabled")
    button8.configure(state="disabled")
    button9.configure(state="disabled")


def btn_click(buttons):
    global bclick, flag, player1_name, player2_name, player_a, player_b

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        player_b = "Player 2 Wins!!!"
        player_a = "Player 1 Wins!!!"
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1

    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already clicked!")


def reset():
    global flag
    flag = 0
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background="grey")
    button2.configure(background="grey")
    button3.configure(background="grey")
    button4.configure(background="grey")
    button5.configure(background="grey")
    button6.configure(background="grey")
    button7.configure(background="grey")
    button8.configure(background="grey")
    button9.configure(background="grey")

    if PlayerX.get() == 3:
        tk.messagebox.showinfo("Tic-Tac-Toe", "PlayerX won the game!")
        exit(-1)
    if PlayerO.get() == 3:
        tk.messagebox.showinfo("Tic-Tac-Toe", "PlayerO won the game!")
        exit(-1)

def newGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)


def showMessage(player):
    if player is player_a:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", player_a)
        PlayerX.set(PlayerX.get() + 1)
        reset()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", player_b)
        PlayerO.set(PlayerO.get() + 1)
        reset()


def checkForWin():
    global bclick

    if bclick == False:
        color = "red"
        character = "X"
        player = player_a
    else:
        color = "green"
        character = "O"
        player = player_b

    if button1["text"] == character and button2["text"] == character and button3["text"] == character:
        button1.configure(background=color)
        button2.configure(background=color)
        button3.configure(background=color)
        showMessage(player)

    elif button1["text"] == character and button5["text"] == character and button9["text"] == character:
        button1.configure(background=color)
        button5.configure(background=color)
        button9.configure(background=color)
        showMessage(player)

    elif button1["text"] == character and button4["text"] == character and button7["text"] == character:
        button1.configure(background=color)
        button4.configure(background=color)
        button7.configure(background=color)
        showMessage(player)

    elif button2["text"] == character and button5["text"] == character and button8["text"] == character:
        button2.configure(background=color)
        button5.configure(background=color)
        button8.configure(background=color)
        showMessage(player)

    elif button3["text"] == character and button6["text"] == character and button9["text"] == character:
        button3.configure(background=color)
        button6.configure(background=color)
        button9.configure(background=color)
        showMessage(player)

    elif button3["text"] == character and button5["text"] == character and button7["text"] == character:
        button3.configure(background=color)
        button5.configure(background=color)
        button7.configure(background=color)
        showMessage(player)

    elif button4["text"] == character and button5["text"] == character and button6["text"] == character:
        button4.configure(background=color)
        button5.configure(background=color)
        button6.configure(background=color)
        showMessage(player)

    elif button7["text"] == character and button8["text"] == character and button9["text"] == character:
        button7.configure(background=color)
        button8.configure(background=color)
        button9.configure(background=color)
        showMessage(player)

    elif flag == 9:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a tie!!!")
        reset()


button_reset = tk.Button(RightFrame2, text="Reset", font="Times 26 bold", height=3, width=20,
                         bg='gainsboro', command=lambda: reset())
button_reset.grid(row=0, column=0, padx=6, pady=11)

button_NewGame = tk.Button(RightFrame2, text="New Game", font="Times 26 bold", height=3, width=20,
                           bg='gainsboro', command=lambda: newGame())
button_NewGame.grid(row=1, column=0, padx=6, pady=10)

button1 = tk.Button(LeftFrame, text=" ", font="Times 26 bold", bg="grey", fg="black", height=3, width=8,
                    command=lambda: btn_click(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = tk.Button(LeftFrame, text=" ", font="Times 26 bold", bg="grey", fg="black", height=3, width=8,
                    command=lambda: btn_click(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = tk.Button(LeftFrame, text=" ", font="Times 26 bold", bg="grey", fg="black", height=3, width=8,
                    command=lambda: btn_click(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = tk.Button(LeftFrame, text=" ", font="Times 26 bold", bg="grey", fg="black", height=3, width=8,
                    command=lambda: btn_click(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = tk.Button(LeftFrame, text=" ", font="Times 26 bold", bg="grey", fg="black", height=3, width=8,
                    command=lambda: btn_click(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = tk.Button(LeftFrame, text=" ", font="Times 26 bold", bg="grey", fg="black", height=3, width=8,
                    command=lambda: btn_click(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = tk.Button(LeftFrame, text=" ", font="Times 26 bold", bg="grey", fg="black", height=3, width=8,
                    command=lambda: btn_click(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = tk.Button(LeftFrame, text=" ", font="Times 26 bold", bg="grey", fg="black", height=3, width=8,
                    command=lambda: btn_click(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = tk.Button(LeftFrame, text=" ", font="Times 26 bold", bg="grey", fg="black", height=3, width=8,
                    command=lambda: btn_click(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

root.mainloop()


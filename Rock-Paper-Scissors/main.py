from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root=Tk()
root.title="Rock Paper Scissors"
root.configure(background="lightgreen")
root.geometry("680x250") 

#picture
rock_img = ImageTk.PhotoImage(Image.open("images/rockuser.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("images/paperuser.png").resize((100, 100)))
sciss_img = ImageTk.PhotoImage(Image.open("images/scissuser.png").resize((100, 100)))
rockcomp_img = ImageTk.PhotoImage(Image.open("images/rockcomp.png").resize((100, 100)))
papercomp_img = ImageTk.PhotoImage(Image.open("images/papercomp.png").resize((100, 100)))
scisscomp_img = ImageTk.PhotoImage(Image.open("images/scisscomp.png").resize((100, 100)))

#inserting picture
user_label=Label(root, image=paper_img, bg="lightgreen")
comp_label=Label(root, image=papercomp_img, bg="lightgreen")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores
playerScore=Label(root, text=0, font=100, bg="lightgreen", fg="black")
computerScore=Label(root, text=0, font=100, bg="lightgreen", fg="black")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indicators
user_indicator=Label(root, font=50, text="USER", bg="lightgreen", fg="black")
comp_indicator=Label(root, font=50, text="COMPUTER", bg="lightgreen", fg="black")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

#messages
msg=Label(root, font=100, bg="lightgreen", fg="black")
msg.grid(row=4, column=2)

#update messages
def updateMessage(x):
    msg['text'] = x

#update score
def updateUserScore():
    score=int(playerScore["text"])
    score+=1
    playerScore["text"]=str(score)

def updateComputerScore():
    score=int(computerScore["text"])
    score+=1
    computerScore["text"]=str(score)

#check for winner
def CheckWinner(player, computer):
    if player==computer:
        updateMessage("It's a tie!")
    elif player=="rock":
        if computer=="paper":
            updateMessage("Oops, you lose!")
            updateComputerScore()
        else:
            updateMessage("Yay, you win!!!")
            updateUserScore()
    elif player=="paper":
        if computer=="scissor":
            updateMessage("Oops, you lose!")
            updateComputerScore()
        else:
            updateMessage("Yay, you win!!!")
            updateUserScore()
    else:
        if computer=="rock":
            updateMessage("Oops, you lose!")
            updateComputerScore()
        else:
            updateMessage("Yay, you win!!!")
            updateUserScore()

#update choices

choices=["rock","paper","scissor"]

def updateChoice(x):

    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rockcomp_img)
    elif compChoice=="paper":
        comp_label.configure(image=papercomp_img)
    else:
        comp_label.configure(image=scisscomp_img)

    #for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=sciss_img) 
    CheckWinner(x,compChoice)

def finalResult():
    player_score = int(playerScore["text"])
    computer_score = int(computerScore["text"])
    
    if player_score > computer_score:
        updateMessage("Result: You Win!")
    elif player_score < computer_score:
        updateMessage("Result: You Lose!")
    else:
        updateMessage("Result: It's a Tie!")

#buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#de5d83", fg="black", command=lambda:updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FFE900", fg="black", command=lambda:updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#05C3DD", fg="black", command=lambda:updateChoice("scissor")).grid(row=2, column=3)

finish_button = Button(root, width=20, height=2, text="FINISH", bg="#ff007f", fg="black", command=finalResult)  
finish_button.grid(row=3, column=2)

root.mainloop()
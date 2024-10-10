from tkinter import *
from PIL import Image, ImageTk

#main window
root=Tk()
root.title="Rock Paper Scissors"
root.configure(background="lightgreen")

rock_img=ImageTk.PhotoImage(Image.open("rockuser.png"))
paper_img=ImageTk.PhotoImage(Image.open("paperuser.png"))
sciss_img=ImageTk.PhotoImage(Image.open("scissuser.png"))
rockcomp_img=ImageTk.PhotoImage(Image.open("rockcomp.png"))
papercomp_img=ImageTk.PhotoImage(Image.open("papercomp.png"))
scisscomp_img=ImageTk.PhotoImage(Image.open("scisscomp.png"))

user_label=Label(root, image=paper_img, bg="lightgreen")
comp_label=Label(root, image=papercomp_img, bg="lightgreen")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

playerScore=Label(root, text=0, font=100, bg="lightgreen", fg="black")
computerScore=Label(root, text=0, font=100, bg="lightgreen", fg="black")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

rock = Button(root, width=20, height=2, text="ROCK", fg="black").grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", fg="black").grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", fg="black").grid(row=2, column=3)

root.mainloop()
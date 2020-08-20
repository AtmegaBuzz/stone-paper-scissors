from tkinter import *


import random
window = Tk()
window.iconbitmap(r'E:\\programming\\stonepapersissors\\game.ico')
window.title("Stone Paper Scissors")
height = 620
width = 700
window.geometry(f'{width}x{height}')

# images of stone ,paper and scissors
stone_image = PhotoImage(file="E:\programming\stonepapersissors\stone.png")
paper_image = PhotoImage(file="E:\programming\stonepapersissors\paper.png")
scissors_image = PhotoImage(file="E:\programming\stonepapersissors\scissors.png")

# designing window
c1 = Canvas(window,borderwidth = 2,relief="groove").place(relheight=1,relwidth=1)
f1 = Frame(c1,bg="red",borderwidth=2,relief="groove").place(relheight = 0.06,relwidth=1,rely=0.97)

heading = Label(c1,text="Stone, Paper & Scissors",font="Helvetica 14 bold",borderwidth=2,relief="groove",bg="#ff5733").place(relheight=0.06,relwidth=0.4,relx=0.32,rely=0.017)


# opponent screen
computer= Frame(c1,borderwidth=1,relief="sunken").place(relheight=0.35,relwidth=0.35,relx=0.06,rely=0.1)
lcomputer = Label(computer,text="Computer",font="Helvetica 10 bold").place(relheight=0.04,relwidth=0.1,relx=0.1,rely=0.12)

you= Frame(c1,borderwidth=1,relief="sunken").place(relheight=0.35,relwidth=0.35,relx=0.46,rely=0.1)
lyou = Label(you,text="You",font="Helvetica 10 bold").place(relheight=0.04,relwidth=0.04,relx=0.48,rely=0.12)


# making of functions
your_choice = 0
def stone():
    global your_choice
    pic1 = Label(you,image = stone_image).place(relheight=0.1,relwidth=0.09,relx=0.6,rely=0.2)
    your_choice = 1
def paper():
    global your_choice
    pic1 = Label(you,image = paper_image).place(relheight=0.1,relwidth=0.09,relx=0.6,rely=0.2)
    your_choice=2
def scissors():
    global your_choice
    pic1 = Label(you,image = scissors_image).place(relheight=0.1,relwidth=0.09,relx=0.6,rely=0.2)
    your_choice = 3

# clear function
def clear():
    clear_c =Label(computer,text=" ").place(relheight=0.1,relwidth=0.09,relx=0.16,rely=0.2)
    clear_y =Label(you,text=" ").place(relheight=0.1,relwidth=0.09,relx=0.6,rely=0.2)
    result = Label(c1,text=" ",font="Helvetica 15 bold").place(relheight=0.05,relwidth=0.39,relx=0.4,rely=0.5)
# start function
def computer_turn():
    computer_choice = random.randint(1,3)
    computer = 0
    
    if computer_choice==1:
        pic =Label(computer,image = stone_image).place(relheight=0.1,relwidth=0.09,relx=0.16,rely=0.2)
        computer = 1
    elif computer_choice==2:
        pic = Label(computer,image = paper_image).place(relheight=0.1,relwidth=0.09,relx=0.16,rely=0.2)
        computer = 2
    elif computer_choice==3:
        pic = Label(computer,image = scissors_image).place(relheight=0.1,relwidth=0.09,relx=0.16,rely=0.2)
        computer= 3

    # draw
    if your_choice == computer_choice:
        result = Label(c1,text="Its a Draw",font="Helvetica 15 bold").place(relheight=0.05,relwidth=0.15,relx=0.44,rely=0.5)
    # stone win/loose
    elif your_choice==1 and computer_choice==2:
        result = Label(c1,text="Bad Luck",font="Helvetica 15 bold").place(relheight=0.05,relwidth=0.15,relx=0.44,rely=0.5)
    elif your_choice==1 and computer_choice==3:
        result = Label(c1,text="BOOM** YOU WON :)",font="Helvetica 15 bold").place(relheight=0.05,relwidth=0.35,relx=0.44,rely=0.5)
    
    # paper win/loose4
    elif your_choice==2 and computer_choice==1:
        result = Label(c1,text="BOOM** YOU WON :)",font="Helvetica 15 bold").place(relheight=0.05,relwidth=0.35,relx=0.44,rely=0.5)
    elif your_choice==2 and computer_choice==3:
        result = Label(c1,text="Bad Luck",font="Helvetica 15 bold").place(relheight=0.05,relwidth=0.15,relx=0.44,rely=0.5)
    
    # scissors win/loose
    elif your_choice==3 and computer_choice==1:
        result = Label(c1,text="Bad Luck",font="Helvetica 15 bold").place(relheight=0.05,relwidth=0.15,relx=0.44,rely=0.5)
    elif your_choice==3 and computer_choice==2:
        result = Label(c1,text="BOOM** YOU WON :)",font="Helvetica 15 bold").place(relheight=0.05,relwidth=0.35,relx=0.44,rely=0.5)


choose_frame = Frame(c1,borderwidth=1,relief="sunken").place(relheight=0.35,relwidth=0.75,relx=0.061,rely=0.45)

# choosing options
choose= Label(choose_frame,text="Choose an Option",font="Helvetica 14 bold underline").place(relheight=0.05,relwidth=0.3,relx=0.08,rely=0.46)
stone = Button(choose_frame,text="Stone",font="Helvetica 14 bold",command=stone).place(relheight=0.05,relwidth=0.1,relx=0.15,rely=0.52)
paper = Button(choose_frame,text="Paper",font="Helvetica 14 bold",command=paper).place(relheight=0.05,relwidth=0.1,relx=0.15,rely=0.59)
scissors= Button(choose_frame,text="Scissors",font="Helvetica 14 bold",command=scissors).place(relheight=0.05,relwidth=0.13,relx=0.14,rely=0.662)

start = Button(c1,text="Start",font="Helvetica 14 bold",command=computer_turn).place(relheight=0.05,relwidth=0.1,relx=0.14,rely=0.8)
clear = Button(c1,text="Play Again",font="Helvetica 14 bold",command=clear).place(relheight=0.05,relwidth=0.2,relx=0.6,rely=0.8)




window.mainloop()
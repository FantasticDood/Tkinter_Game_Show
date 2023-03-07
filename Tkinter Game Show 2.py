## Daniel's game show.
## NOTE: YOU HAVE TO INSTALL pillow, pygame, AND tkinter (but it should already be installed)
## In a terminal: pip3 install pillow pygame

import tkinter as tk

window = tk.Tk()

window.geometry('800x600')

window.configure(background='#EDEADE')

try:
    from PIL import ImageTk, Image
    from pygame import mixer
except ModuleNotFoundError:
    def bru():
        questionlabel4 = tk.Label(
                master=window,
                text='PLEASE RUN "pip3 install pillow pygame" IN A TERMINAL',
                foreground='red',
                background='#EDEADE',
                font=('Arial',30)
                )
        questionlabel4.place(x=0,y=300)
    questionlabel3 = tk.Label(
        master=window,
        text='YOU ARE MISSING SOME MODULES REQUIRED',
        foreground='red',
        background='#EDEADE',
        font=('Arial',33)
        )
    questionlabel3.place(x=20,y=200)
    window.after(1,bru)
    def e():
        quit()
    window.after(9000,e)

import os
import random
import sys

points = 0

opt1 = 0
opt2 = 0
opt3 = 0
opt4 = 0
twox = False

def options(option1,option2,option3,option4):
    global option_a
    global option_b
    global option_c
    global option_d
    ## Option A

    def y():
        global points
        global twox
        print('debug')
        buttons_hide()
        questionhide()
        if twox == True:
            if points < 0:
                questionlabel('Shouldnt have chosen double :>',80,190,50,'red')
            else:
                questionlabel('Double Points! Good Job!',100,190,50,'green')
            points = points * 2
            twox = False
        else:
            questionlabel('Correct! +200 points',160,190,50,'green')
            points = points + 200
        otherhide()
        otherlabel('Points: ' + str(points),600,20)
        window.after(2500,func)

    def n():
        global points
        global twox
        print('debug')
        buttons_hide()
        questionhide()
        if twox == True:
            questionlabel('Oh No! ZERO POINTS :(',160,190,50,'red')
            points = 0
            twox = False
        else:
            questionlabel('Incorrect! -200 points',160,190,50,'red')
            points = points - 200
        otherhide()
        otherlabel('Points: ' + str(points),600,20)
        window.after(2500,func)
                    
    def press_1():
        global opt1
        global opt2
        global opt3
        global opt4
        if opt1 == 1:
            n()
            imagehide(Image1)
        if opt1 == 2:
            n()
            imagehide(Image2)
        if opt1 == 3:
            n()
            imagehide(Image3)
        if opt1 == 4:
            y()
            imagehide(Image4)
        if opt1 == 5:
            n()
            imagehide(Image5)
            
    option_a = tk.Button(
        master=window,
        text=option1,
        fg='black',
        bg='black',
        height=5,
        width=10,
        font=("Arial", 20),
        activeforeground='black',
        command=press_1
        )

    def press_2():
        global opt1
        global opt2
        global opt3
        global opt4
        if opt2 == 1:
            n()
            imagehide(Image1)
        if opt2 == 2:
            n()
            imagehide(Image2)
        if opt2 == 3:
            y()
            imagehide(Image3)
        if opt2 == 4:
            n()
            imagehide(Image4)
        if opt2 == 5:
            y()
            imagehide(Image5)
            
    ## Option B
    option_b = tk.Button(
        master=window,
        text=option2,
        foreground='black',
        background='white',
        height=5,
        width=10,
        font=("Arial", 20),
        activeforeground='black',
        command=press_2
        )

    def press_3():
        global opt1
        global opt2
        global opt3
        global opt4
        if opt3 == 1:
            n()
            imagehide(Image1)
        if opt3 == 2:
            y()
            imagehide(Image2)
        if opt3 == 3:
            n()
            imagehide(Image3)
        if opt3 == 4:
            n()
            imagehide(Image4)
        if opt3 == 5:
            n()
            imagehide(Image5)
            
    ## Option C
    option_c = tk.Button(
        master=window,
        text=option3,
        foreground='black',
        background='white',
        height=5,
        width=10,
        font=("Arial", 20),
        activeforeground='black',
        command=press_3
        )

    def press_4():
        global opt1
        global opt2
        global opt3
        global opt4
        if opt4 == 1:
            y()
            imagehide(Image1)
        if opt4 == 2:
            n()
            imagehide(Image2)
        if opt4 == 3:
            n()
            imagehide(Image3)
        if opt4 == 4:
            n()
            imagehide(Image4)
        if opt4 == 5:
            n()
            imagehide(Image5)
            
    ## Option D
    option_d = tk.Button(
        master=window,
        text=option4,
        foreground='black',
        background='white',
        height=5,
        width=10,
        font=("Arial", 20),
        activeforeground='black',
        command=press_4
        )

##########################################################

## Place Buttons
def buttons_place():
    option_a.place(x=30,y=450)
    option_b.place(x=230,y=450)
    option_c.place(x=430,y=450)
    option_d.place(x=630,y=450)

def buttons_hide():
    option_a.place_forget()
    option_b.place_forget()
    option_c.place_forget()
    option_d.place_forget()

## question label
def questionlabel(question_text,pos_x,pos_y,size,color):
    global question_label
    question_label = tk.Label(
        master=window,
        text=question_text,
        foreground=color,
        background='#EDEADE',
        font=('Arial',size)
        )
    question_label.place(x=pos_x,y=pos_y)

def questionlabel2(question_text,pos_x,pos_y,size,color):
    global question_label
    question_label2 = tk.Label(
        master=window,
        text=question_text,
        foreground=color,
        background='#EDEADE',
        font=('Arial',size)
        )
    question_label2.place(x=pos_x,y=pos_y)


## Other label
def otherlabel(other_text,x_pos,y_pos):
    global other_label
    other_label = tk.Label(
        master=window,
        text=other_text,
        foreground='black',
        background='#EDEADE',
        font=('Arial',30)
        )
    other_label.place(x=x_pos,y=y_pos)

def otherhide():
    other_label.place_forget()

def questionhide():
    question_label.place_forget()

def questionhide2():
    question_label2.place_forget()

## Imaging thing    

img = ImageTk.PhotoImage(Image.open('Tower.jpeg'))
Image1 = tk.Label(window, image = img)
img2 = ImageTk.PhotoImage(Image.open('White_house.jpeg'))
Image2 = tk.Label(window, image = img2)
img3 = ImageTk.PhotoImage(Image.open('edinburgh.jpeg'))
Image3 = tk.Label(window, image = img3)
img4_open = Image.open('andorra.jpeg')
resize_img4 = img4_open.resize((300,150))
resized_img4 = ImageTk.PhotoImage(resize_img4)
Image4 = tk.Label(window, image = resized_img4)
img5 = ImageTk.PhotoImage(Image.open('dna.jpeg'))
Image5 = tk.Label(window, image = img5)

def imagehide(imagever):
    imagever.pack_forget()

##########################################################

## Start Game

mixer.init()
def sound(filename):
    mixer.music.load(filename)
    mixer.music.play()    

sound('Music/3.mp3')

questionlabel("Welcome to Daniel's Gameshow!",30,180,50,'black')

otherlabel('Points: ' + str(points),600,20)

def func1():
    global opt1
    global opt2
    global opt3
    global opt4
    questionhide()
    Image1.pack()
    questionlabel("What building is this?",150,330,50,'black')
    options('Paris','China','Burg Khalifa','Eiffel Tower')
    opt1 = 1
    opt2 = 1
    opt3 = 1
    opt4 = 1
    buttons_place()

def func2():
    global opt1
    global opt2
    global opt3
    global opt4
    questionhide()
    questionlabel('What is the capital of the US?',80,200,50,'black')
    Image2.pack()
    options('Washington','New York','Washington, DC','Dubai')
    opt1 = 2
    opt2 = 2
    opt3 = 2
    opt4 = 2
    buttons_place()

def func3():
    global opt1
    global opt2
    global opt3
    global opt4
    questionhide()
    questionlabel('What is the capital of Scotland?',80,200,50,'black')
    Image3.pack()
    options('Moscow','Edinburgh','Washington, DC','Berlin')
    opt1 = 3
    opt2 = 3
    opt3 = 3
    opt4 = 3
    buttons_place()

def func4():
    global opt1
    global opt2
    global opt3
    global opt4
    questionhide()
    questionlabel('Which country is "sandwiched" between France and Spain?',0,200,30,'black')
    Image4.pack()
    options('Andorra','Scotland','Slovakia','Switzerland')
    opt1 = 4
    opt2 = 4
    opt3 = 4
    opt4 = 4
    buttons_place()

def func5():
    global opt1
    global opt2
    global opt3
    global opt4
    questionhide()
    questionlabel('What does DNA stand for?',100,350,50,'black')
    Image5.pack()
    options('Dynamic Nucleoid' + '\n' 'Anagram','Deoxyribonucleic' + '\n'  + 'Acid','Demersanicnucleoider Analasys','Daniel is cool')
    opt1 = 5
    opt2 = 5
    opt3 = 5
    opt4 = 5
    buttons_place()


def double():
    global twox
    twox = True
    func()
        
def double1():
    global yesbutton
    global nobutton
    questionhide()
    questionlabel('Would you like to do a double-or-nothing round?',20,200,35,'violetred1')
    yesbutton = tk.Button(master=window,
                          text='YES',
                          foreground='black',
                          background='white',
                          font=('Arial',50),
                          command=double
                          )
    nobutton = tk.Button(master=window,
                          text='NO',
                          foreground='black',
                          background='white',
                          font=('Arial',50),
                          command=func
                          )
    yesbutton.place(x=230,y=450)
    nobutton.place(x=430,y=450)

funcs = [func1,func2,func3,func4,func5]

def ending():
    score = str((points/3400)*100)
    questionhide()
    questionlabel(f'Your score was: {score}%!',110,180,60,'black')
    questionlabel('Thanks for playing!',140,300,60,'black')
    window.after(5000,quit)

funcing = 0

def func():
    global double1
    global funcing
    global funcs
    global yesbutton
    global nobutton
    funcing = funcing + 1
    print(funcing)
    try:
        yesbutton.place_forget()
    except:
        pass
    try:
        nobutton.place_forget()
    except:
        pass
    if not bool(funcs) or funcs and all(elem == double1 for elem in funcs):
        print('asdasdasdasdasdasd')
        ending()
    if funcing == 3:
        run = double1
    elif funcing == 7:
        run = double1
    else:
        run = random.choice(funcs)
        funcs.remove(run)
    run()
    
window.after(3000,func)

window.mainloop()

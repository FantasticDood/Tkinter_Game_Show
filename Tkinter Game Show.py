import tkinter as tk
from PIL import ImageTk, Image
import os
from pygame import mixer

points = 0

window = tk.Tk()

window.geometry('800x600')

opt1 = 0
opt2 = 0
opt3 = 0
opt4 = 0

def options(option1,option2,option3,option4):
    global option_a
    global option_b
    global option_c
    global option_d
    ## Option A

    def y():
        global points
        print('debug')
        buttons_hide()
        questionhide()
        questionlabel('Correct! +200 points',160,190,50,'green')
        points = points + 200
        otherhide()
        otherlabel('Points: ' + str(points),600,20)
        

    def n():
        global points
        print('debug')
        buttons_hide()
        questionhide()
        questionlabel('Incorrect! -200 points',160,190,50,'red')
        points = points - 200
        otherhide()
        otherlabel('Points: ' + str(points),600,20)
        
    def press_1():
        global opt1
        global opt2
        global opt3
        global opt4
        opt1 = opt1+1
        opt2 = opt2+1
        opt3 = opt3+1
        opt4 = opt4+1
        if opt1 == 1:
            n()
            imagehide(Image1)
            window.after(2500,func2)
        if opt1 == 2:
            n()
            imagehide(Image2)
            window.after(2500,double1)
        
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
        opt1 = opt1+1
        opt2 = opt2+1
        opt3 = opt3+1
        opt4 = opt4+1
        if opt2 == 1:
            n()
            imagehide(Image1)
            window.after(2500,func2)
        if opt2 == 2:
            n()
            imagehide(Image2)
            window.after(2500,double1)

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
        opt1 = opt1+1
        opt2 = opt2+1
        opt3 = opt3+1
        opt4 = opt4+1
        if opt3 == 1:
            n()
            imagehide(Image1)
            window.after(2500,func2)
        if opt3 == 2:
            y()
            imagehide(Image2)
            window.after(2500,double1)

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
        opt1 = opt1+1
        opt2 = opt2+1
        opt3 = opt3+1
        opt4 = opt4+1
        if opt4 == 1:
            y()
            imagehide(Image1)
            window.after(2500,func2)
        if opt4 == 2:
            n()
            imagehide(Image2)
            window.after(2500,double1)

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

## Imaging thing    

img = ImageTk.PhotoImage(Image.open('Path/To/Image.jpeg'))
Image1 = tk.Label(window, image = img)
img2 = ImageTk.PhotoImage(Image.open('White_house.jpeg'))
Image2 = tk.Label(window, image = img2)

def imagehide(imagever):
    imagever.pack_forget()
    
## Configure background
window.configure(background='#EDEADE')

##########################################################

## Start Game

## Music Functionality (needs fix on stopping when program exits)
mixer.init()
def sound(filename):
    mixer.music.load(filename)
    mixer.music.play()    

sound('Path/To/Music.mp3')

questionlabel("Intro_Text",X-pos,Y-pos,Font-Size,'Color')

otherlabel('Points: ' + str(points),600,20)

def func1():
    questionhide()
    Your_image_variable.pack()
    questionlabel("Question",X-pos,Y-pos,Font-Size,'Color')
    options('Option 1 (e.g Paris)','Option 2','Option 3','Option 4')
    buttons_place()

## Example Question/Function:
    
def func2():
    questionhide()
    questionlabel('What is the capital of the US?',80,200,50,'black')
    Image2.pack()
    options('Washington','New York','Washington, DC','Dubai')
    buttons_place()

def func3():
## Function here

def func4():
## Other Function here

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
                          command=func3
                          )
    nobutton = tk.Button(master=window,
                          text='NO',
                          foreground='black',
                          background='white',
                          font=('Arial',50),
                          command=func4
                          )
    yesbutton.place(x=230,y=450)
    nobutton.place(x=430,y=450)
    
window.after(3000,func1)

window.mainloop()

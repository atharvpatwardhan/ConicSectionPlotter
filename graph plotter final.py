# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:51:00 2020


@author: asus
"""
from tkinter import Tk,Label,StringVar,ttk
import matplotlib.pyplot as plt
import numpy as np

def circle():
    c1 = ccolor.get()
    R= radius.get()
    R1 = int(R)
    n=1000000
    t=np.linspace(0,2*np.pi,n+1)
    x=R1*np.cos(t)
    y=R1*np.sin(t)

    plt.axis("equal")
    plt.grid()
    plt.plot(x,y,color = c1)

    plt.show()
    
def ellipse():
    c3 = ecolor.get()
    t=np.linspace(0,360,360)
    a= ellipsemajor.get()
    a1 = int(a)
    b=ellipseminor.get()
    b1 = int(b)
    x=a1*np.cos(t)
    y=b1*np.sin(t)    
    plt.grid()
    plt.plot(x,y,color = c3)
    plt.show()

def parabola():
    c = pcolor.get()
    a = paramajoraxis.get()
    a1 = int(a)
    y = np.linspace(-10,10,10)
    x = y**2 / 4*a1

    plt.plot(x,y,color = c)
    plt.grid()
    plt.show()

def hyperbola():
    c2 = h1color.get()
    c4 = h2color.get()
    t = np.linspace(-np.pi/3, np.pi/3, 200)
    a = hypermajor.get()
    a1 = int(a)
    b = hyperminor.get()
    b1 = int(b)
    y = a1/np.cos(t) 
    x = b1*np.tan(t)
    plt.plot(x,y,color = c2)

    t = np.linspace(np.pi-np.pi/3, np.pi+np.pi/3, 200) 
    y = a1/np.cos(t) 
    x = b1*np.tan(t)
    plt.plot(x,y,color = c4)
    
    plt.grid()

    plt.show()
    
def leave():
    quit()
    screen.destroy()
 
screen = Tk()
screen.configure(bg = "red4")
screen.geometry("500x600")
screen.title("Graph Plotter")

paramajoraxis = StringVar()
radius = StringVar()
ellipsemajor = StringVar()
ellipseminor  = StringVar()
hypermajor = StringVar()
hyperminor = StringVar()
pcolor = StringVar()
pcolor.set("Blue")
ccolor = StringVar()
ccolor.set("Blue")
ecolor = StringVar()
ecolor.set("Blue")
h1color = StringVar()
h1color.set("Blue")
h2color = StringVar()
h2color.set("Blue")


colors = ["Red","Yellow","Orange","Coral","Blue","MediumBlue","DarkBlue","Navy","Green","Lime","Cyan","Purple","Pink","Magenta","DarkMagenta","Olive","Brown","LightGrey","Grey","Black"]
parabola_entry = ttk.Entry(textvariable = paramajoraxis)#,bg = "Lightsalmon1")
parabola_entry.place(x=15,y=110)

paracolor_label = Label(text = "Color :",bg = "DarkOrange1")
paracolor_label.place(x=15,y=140)
paracolor_combo = ttk.Combobox(textvariable = pcolor,value = colors)
paracolor_combo.place(x=15,y=170)

parabola_text = Label(text = "Parabola :",bg = "DarkOrange1")
paramajor_text = Label(text = "Major Axis :",bg = "DarkOrange1")
parabola_text.place(x=15,y=50)
paramajor_text.place(x=15,y=85)
circle_text = Label(text = "Circle :",bg = "DarkOrange1")
circleradius_text = Label(text = "Radius :",bg = "DarkOrange1")
circle_text.place(x=300,y=50)
circleradius_text.place(x=300,y=85)
ellipse_text = Label(text = "Ellipse :",bg = "DarkOrange1")
ellipsemajor_text = Label(text = "Major Axis :",bg = "DarkOrange1")
ellipseminor_text = Label(text = "Minor Axis :",bg = "DarkOrange1")
ellipsecolor_text = Label(text = "Color :",bg = "DarkOrange1")
ellipsecolor_text.place(x=15,y=430)
ellipse_text.place(x=15,y=270)
ellipsemajor_text.place(x=15,y=310)
ellipseminor_text.place(x=15,y=370)
ellipsecolor_combo = ttk.Combobox(textvariable = ecolor,value = colors)
ellipsecolor_combo.place(x=15,y=460)

hyperbola_text = Label(text = "Hyperbola :",bg = "DarkOrange1")
hypermajor_text = Label(text = "Major Axis :",bg = "DarkOrange1")
hyperminor_text = Label(text = "Minor Axis :",bg = "DarkOrange1")
hyperbola_text.place(x=300,y=270)
hypermajor_text.place(x=300,y=310)
hyperminor_text.place(x=300,y=370)
hypercolor1_text = Label(text = "Color 1:",bg = "DarkOrange1")
hypercolor1_combo = ttk.Combobox(textvariable = h1color,value = colors,width = "7")
hypercolor1_text.place(x=300,y=430)
hypercolor1_combo.place(x=300,y=460)
hypercolor2_text = Label(text = "Color 2:",bg = "DarkOrange1")
hypercolor2_combo = ttk.Combobox(textvariable = h2color,value = colors,width = "7")
hypercolor2_text.place(x=410,y=430)
hypercolor2_combo.place(x=410,y=460)

heading_label1 = Label(text = "To plot the graph of the conic please enter the required constraints in the boxes given under")
heading_label1.place(x=1,y=1)
heading_label2 = Label(text = "the name of the conic section ")
heading_label2.place(x=1,y=23)

circle_entry = ttk.Entry(textvariable = radius)
circle_entry.place(x=300,y=110)
circlecolor_label = Label(text = "Color :",bg = "DarkOrange1")
circlecolor_label.place(x=300,y=140)
circle_combo = ttk.Combobox(textvariable = ccolor,value = colors)
circle_combo.place(x=300,y=170)

ellipsemajor_entry = ttk.Entry(textvariable  = ellipsemajor)
ellipseminor_entry = ttk.Entry(textvariable  = ellipseminor)
ellipsemajor_entry.place(x=15,y=340)
ellipseminor_entry.place(x=15,y=400)


hypermajor_entry = ttk.Entry(textvariable = hypermajor)
hyperminor_entry = ttk.Entry(textvariable = hyperminor)
hypermajor_entry.place(x=300,y=340)
hyperminor_entry.place(x=300,y=400)

parabola_button = ttk.Button(text = "Plot",command = parabola)
circle_button = ttk.Button(text = "Plot",command = circle)
ellipse_button = ttk.Button(text = "Plot",command = ellipse)
hyperbola_button = ttk.Button(text = "Plot",command = hyperbola)
exit_button = ttk.Button(text = "           Exit           ",command = leave)

parabola_button.place(x=15,y=200)
circle_button.place(x=300,y=200)
ellipse_button.place(x=15,y=490)
hyperbola_button.place(x=300,y=490)
exit_button.place(x = 180,y = 540)

screen.mainloop()
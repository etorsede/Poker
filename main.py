# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Import the required libraries
#from tkinter import *
import time
from tkinter import messagebox
#from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
from PIL import Image
from PIL import ImageTk

import packaging
import customtkinter as ctk
import tkinter.messagebox as tkmb


# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("Light")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

win = ctk.CTk()
win.geometry("400x400")
win.title("Scrum Poker")
count = 0

def login():
    global count
    count = count + 1
    #username = "me"
    #password = "123"

    player_nick = user_entry.get()
    room(player_nick, count)
    #if user_entry.get() == username and user_pass.get() == password:

    #elif user_entry.get() == username and user_pass.get() != password:
    #    tkmb.showwarning(title='Wrong password',message='Please check your password')
    #elif user_entry.get() != username and user_pass.get() == password:
    #    tkmb.showwarning(title='Wrong username',message='Please check your username')
    #else:
    #    tkmb.showerror(title="Login Failed",message="Invalid Username and password")


label = ctk.CTkLabel(win,text="Please enter a nickname")

label.pack(pady=20)


frame = ctk.CTkFrame(master=win)
frame.pack(pady=20,padx=40,fill='both',expand=True)

label = ctk.CTkLabel(master=frame,text='Login portal')
label.pack(pady=12,padx=10)


user_entry= ctk.CTkEntry(master=frame,placeholder_text="Enter a nickname")
user_entry.pack(pady=12,padx=10)

#user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
#user_pass.pack(pady=12,padx=10)


button = ctk.CTkButton(master=frame,text='Enter',command=login)
button.pack(pady=12,padx=10)

#checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
#checkbox.pack(pady=12,padx=10)


#app.mainloop()



#win = tk.Tk()

numb1 = [1, 2, 3, 5, 8]
player_value1 = 0
player_value2 = 0
player_value3 = 0
player_value4 = 0

results = [4]
fib2 = [0, 0, 0, 0, 0]

imag2 = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\2.png")
photo2 = ImageTk.PhotoImage(imag2)

imag1 = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\1.png")
photo1 = ImageTk.PhotoImage(imag1)

imag3 = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\3.png")
photo3 = ImageTk.PhotoImage(imag3)

imag5 = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\5.png")
photo5 = ImageTk.PhotoImage(imag5)

imag8 = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\8.png")
photo8 = ImageTk.PhotoImage(imag8)

imag9 = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\backside.png")
photo9 = ImageTk.PhotoImage(imag9)

imag10 = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\outline.png")
photo10 = ImageTk.PhotoImage(imag10)

#Horizontals
imag2_h = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\g.png")
photo2_h = ImageTk.PhotoImage(imag2_h)

imag1_h = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\1_h.png")
photo1_h = ImageTk.PhotoImage(imag1_h)

imag3_h = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\3h.png")
photo3_h = ImageTk.PhotoImage(imag3_h)

imag5_h = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\5_h.png")
photo5_h = ImageTk.PhotoImage(imag5_h)

imag8_h = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\8_h.png")
photo8_h = ImageTk.PhotoImage(imag8_h)

#Highlighted

imag2_high = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\2high.png")
photo2_high = ImageTk.PhotoImage(imag2_high)

imag1_high = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\1_high.png")
photo1_high = ImageTk.PhotoImage(imag1_high)

imag3_high = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\3high.png")
photo3_high = ImageTk.PhotoImage(imag3_high)

imag5_high = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\5high.png")
photo5_high = ImageTk.PhotoImage(imag5_high)

imag8_high = Image.open(r"C:\Users\eric9\Desktop\Projekt\Poker\8high.png")
photo8_high = ImageTk.PhotoImage(imag8_high)

# Set the size of the tkinter window

# Define a function to show the popup message


# label with image
#b = tk.Button(win, image=photo, command=on_button_click())
#b.pack()


#label.pack()
#label.place(relx = 0.6,
#                   rely = 0.5)

def room(p, c):


    win2 = ctk.CTkToplevel(win)
    win2.title("New Window")
    win2.geometry("350x150")
    ctk.CTkLabel(win2, text="room").pack()

    label3=tk.Label(win2, image=photo10)
    label3.pack()
    label3.place(relx = 0.3,
                   rely = 0.39)



    label4=tk.Label(win2, image=photo10)
    label4.pack()
    label4.place(relx = 0.6,
                   rely = 0.39)

    label6=tk.Label(win2, image=photo10)
    label6.pack()
    label6.place(relx = 0.4,
                   rely = 0.39)

    label7=tk.Label(win2, image=photo10)
    label7.pack()
    label7.place(relx = 0.5,
                   rely = 0.39)

    if c == 1:
        nick1 = tk.Label(win2, text=f"{p}")
        nick1.pack()
        nick1.place(relx=0.49,
                rely=0.68)
    elif c == 2:
        nick2 = tk.Label(win2, text=f"{p}")
        nick2.pack()
        nick2.place(relx=0.49,
                rely=0.32)
    elif c == 3:
        nick3 = tk.Label(win2, text=f"{p}")
        nick3.pack()
        nick3.place(relx=0.15,
                rely=0.68)
    elif c == 4:
        nick4 = tk.Label(win2, text=f"{p}")
        nick4.pack()
        nick4.place(relx=0.77,
                rely=0.68)

    # Player 1
    def on_button_click2():
        global player_value1
        player_value1 = 2
        label3.config(image=photo9)

    def on_button_click3():
        global player_value1
        player_value1 = 3
        # label.config(text=f"You've voted: {player_value} story points")
        label3.config(image=photo9)

    def on_button_click5():
        global player_value1
        player_value1 = 5
        # label.config(text=f"You've voted: {player_value} story points")
        label3.config(image=photo9)

    def on_button_click8():
        global player_value1
        player_value1 = 8
        # label.config(text=f"You've voted: {player_value} story points")
        label3.config(image=photo9)

    def on_button_click1():
        global player_value1
        player_value1 = 1
        # label.config(text=f"You've voted: {player_value} story points")
        label3.config(image=photo9)

    # Player 2

    def on_button_click2_2():
        global player_value2
        player_value2 = 2
        # label2.config(text=f"You've voted: {player_value2} story points")
        label4.config(image=photo9)

    def on_button_click3_2():
        global player_value2
        player_value2 = 3
        # label2.config(text=f"You've voted: {player_value2} story points")
        label4.config(image=photo9)

    def on_button_click5_2():
        global player_value2
        player_value2 = 5
        # label2.config(text=f"You've voted: {player_value2} story points")
        label4.config(image=photo9)

    def on_button_click8_2():
        global player_value2
        player_value2 = 8
        # label2.config(text=f"You've voted: {player_value2} story points")
        label4.config(image=photo9)

    def on_button_click1_2():
        global player_value2
        player_value2 = 1
        # label2.config(text=f"You've voted: {player_value2} story points")
        label4.config(image=photo9)

    # Player3

    def on_button_click1_3():
        global player_value3
        player_value3 = 1
        # label.config(text=f"You've voted: {player_value} story points")
        label6.config(image=photo9)

    def on_button_click2_3():
        global player_value3
        player_value3 = 2
        # label2.config(text=f"You've voted: {player_value2} story points")
        label6.config(image=photo9)

    def on_button_click3_3():
        global player_value3
        player_value3 = 3
        # label2.config(text=f"You've voted: {player_value2} story points")
        label6.config(image=photo9)

    def on_button_click5_3():
        global player_value3
        player_value3 = 5
        # label2.config(text=f"You've voted: {player_value2} story points")
        label6.config(image=photo9)

    def on_button_click8_3():
        global player_value3
        player_value3 = 8
        # label2.config(text=f"You've voted: {player_value2} story points")
        label6.config(image=photo9)

    def on_button_click1_3():
        global player_value3
        player_value3 = 1
        # label2.config(text=f"You've voted: {player_value2} story points")
        label6.config(image=photo9)

    # Player4

    def on_button_click1_4():
        global player_value4
        player_value4 = 1
        # label.config(text=f"You've voted: {player_value} story points")
        label7.config(image=photo9)

    def on_button_click2_4():
        global player_value4
        player_value4 = 2
        # label2.config(text=f"You've voted: {player_value2} story points")
        label7.config(image=photo9)

    def on_button_click3_4():
        global player_value4
        player_value4 = 3
        # label2.config(text=f"You've voted: {player_value2} story points")
        label7.config(image=photo9)

    def on_button_click5_4():
        global player_value4
        player_value4 = 5
        # label2.config(text=f"You've voted: {player_value2} story points")
        label7.config(image=photo9)

    def on_button_click8_4():
        global player_value4
        player_value4 = 8
        # label2.config(text=f"You've voted: {player_value2} story points")
        label7.config(image=photo9)

    def on_button_click1_4():
        global player_value4
        player_value4 = 1
        # label2.config(text=f"You've voted: {player_value2} story points")
        label7.config(image=photo9)

    def reveal():
        results = [player_value1, player_value2, player_value3, player_value4]
        results.sort()
        #print(results)

        one = results[0]
        two = results[1]
        three = results[2]
        four = results[3]

        card_1(one)
        card_2(two)
        card_3(three)
        card_4(four)

        avg = sum(results)/4

        for i in range(len(numb1)):
            numb1[i] = numb1[i]-avg

            if numb1[i] < 0:
                numb1[i] = numb1[i]*-1
        numb1.sort()
        #print(numb1)
        fib3 = avg - numb1[0]


        label78.config(text=f"Vote average: {avg}")
        label79.config(text=f"Nearest fibonacci: {fib3}")
        label80.config(text=f"Let's hear from {one} & {four}")

        #print(results)

    def card_1(j):
        if j == 2:
            label3.config(image=photo2_high)
        elif j == 1:
            label3.config(image=photo1_high)
        elif j == 3:
            label3.config(image=photo3_high)
        elif j == 5:
            label3.config(image=photo5_high)
        elif j == 8:
            label3.config(image=photo8_high)

    def card_2(k):
        if k == 2:
            label6.config(image=photo2)
        elif k == 5:
            label6.config(image=photo5)
        elif k == 8:
            label6.config(image=photo8)
        elif k == 3:
            label6.config(image=photo3)
        elif k == 1:
            label6.config(image=photo1)

    def card_3(u):
        if u == 2:
            label7.config(image=photo2)
        elif u == 5:
            label7.config(image=photo5)
        elif u == 8:
            label7.config(image=photo8)
        elif u == 3:
            label7.config(image=photo3)
        elif u == 1:
            label7.config(image=photo1)

    def card_4(e):
        if e == 2:
            label4.config(image=photo2_high)
        elif e == 5:
            label4.config(image=photo5_high)
        elif e == 8:
            label4.config(image=photo8_high)
        elif e == 3:
            label4.config(image=photo3_high)
        elif e == 1:
            label4.config(image=photo1_high)




    label5=tk.Button(win2, text="Reveal", command=reveal)
    label5.pack()
    label5.place(relx = 0.95,
                   rely = 0.39)

    label78=tk.Label(win2, text="")
    label78.pack()
    label78.place(relx = 0.3,
                   rely = 0.35)

    label79=tk.Label(win2, text="")
    label79.pack()
    label79.place(relx = 0.6,
                   rely = 0.35)

    label80=tk.Label(win2, text="Vote for story points!")
    label80.pack()
    label80.place(relx = 0.47,
                   rely = 0.3)
    #def sorting():




#label2 = tk.Label(win, text="Vote for story points")
#label2.pack()
#label2.place(relx = 0.3,
#                   rely = 0.5)
# bind click event to image
#l.bind('<Button-1>', on_button_click())

# button with image binded to the same function


#b = tk.Button(win, text="Close", command=win.destroy)
#b.pack()
# Create a Button to display the message

    #Player 1
    button2 = tk.Button(win2, image=photo2, command=on_button_click2)
    button2.pack()

    button3 = tk.Button(win2, image=photo3, command=on_button_click3)
    button3.pack()

    button5 = tk.Button(win2, image=photo5, command=on_button_click5)
    button5.pack()

    button8 = tk.Button(win2, image=photo8, command=on_button_click8)
    button8.pack()

    button1 = tk.Button(win2, image=photo1, command=on_button_click1)
    button1.pack()

    button1.place(relx = 0.25,
                   rely = 0.72)
    button2.place(relx = 0.352,
                   rely = 0.72)
    button3.place(relx = 0.445,
                   rely = 0.72)
    button5.place(relx = 0.535,
                   rely = 0.72)
    button8.place(relx = 0.63,
                   rely = 0.72)

    #Player 2
    button2_2 = tk.Button(win2, image=photo2, command=on_button_click2_2)
    button2_2.pack()

    button3_2 = tk.Button(win2, image=photo3, command=on_button_click3_2)
    button3_2.pack()

    button5_2 = tk.Button(win2, image=photo5, command=on_button_click5_2)
    button5_2.pack()

    button8_2 = tk.Button(win2, image=photo8, command=on_button_click8_2)
    button8_2.pack()

    button1_2 = tk.Button(win2, image=photo1, command=on_button_click1_2)
    button1_2.pack()

    button1_2.place(relx = 0.25,
                   rely = 0.01)
    button2_2.place(relx = 0.352,
                   rely = 0.01)
    button3_2.place(relx = 0.445,
                   rely = 0.01)
    button5_2.place(relx = 0.535,
                   rely = 0.01)
    button8_2.place(relx = 0.63,
                   rely = 0.01)

    #Player 3

    button2_3 = tk.Button(win2, image=photo2_h, command=on_button_click2_3)
    button2_3.pack()

    button3_3 = tk.Button(win2, image=photo3_h, command=on_button_click3_3)
    button3_3.pack()

    button5_3 = tk.Button(win2, image=photo5_h, command=on_button_click5_3)
    button5_3.pack()

    button8_3 = tk.Button(win2, image=photo8_h, command=on_button_click8_3)
    button8_3.pack()

    button1_3 = tk.Button(win2, image=photo1_h, command=on_button_click1_3)
    button1_3.pack()

    button1_3.place(relx = 0.01,
                   rely = 0.01)
    button2_3.place(relx = 0.01,
                   rely = 0.2)
    button3_3.place(relx = 0.01,
                   rely = 0.37)
    button5_3.place(relx = 0.01,
                   rely = 0.53)
    button8_3.place(relx = 0.01,
                   rely = 0.7)

    #Player 4

    button2_4 = tk.Button(win2, image=photo2_h, command=on_button_click2_4)
    button2_4.pack()

    button3_4 = tk.Button(win2, image=photo3_h, command=on_button_click3_4)
    button3_4.pack()

    button5_4 = tk.Button(win2, image=photo5_h, command=on_button_click5_4)
    button5_4.pack()

    button8_4 = tk.Button(win2, image=photo8_h, command=on_button_click8_4)
    button8_4.pack()

    button1_4 = tk.Button(win2, image=photo1_h, command=on_button_click1_4)
    button1_4.pack()

    button1_4.place(relx = 0.8,
                   rely = 0.7)
    button2_4.place(relx = 0.8,
                   rely = 0.53)
    button3_4.place(relx = 0.8,
                   rely = 0.37)
    button5_4.place(relx = 0.8,
                   rely = 0.2)
    button8_4.place(relx = 0.8,
                   rely = 0.01)


# Add an optional Label widget


win.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

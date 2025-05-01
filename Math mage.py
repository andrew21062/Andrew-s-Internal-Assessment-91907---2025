# Andrew Wong
# 08/04/25  

import random
from tkinter import * 
from PIL import Image, ImageTk
        
enemy_list = [
    {"image": "enemy1.png"},{"image": "enemy2.png"},
    {"image": "enemy3.png"},{"image": "enemy4.png"},
    {"image": "enemy5.png"},{"image": "enemy6.png"},
    {"image": "enemy7.png"},{"image": "enemy8.png"},
    {"image": "enemy9.png"},{"image": "enemy10.png"}]

boss_list = [
    {"boss No": 1, "image": "boss1.png"},{"boss No": 2, "image": "boss2.png"},
    {"boss No": 3, "image": "boss3.png"},{"boss No": 4, "image": "boss4.png"},
    {"boss No": 5, "image": "boss5.png"}]

basic_questions = [
    {"question": "x+7=10", "answer": 3},{"question": "2x−4=6", "answer": 5},{"question": "x−3=7", "answer": 10},
    {"question": "3x+4=13", "answer": 3},{"question": "5x−15=0", "answer": 3},{"question": "4x+2=18", "answer": 4},
    {"question": "x+5=9", "answer": 4},{"question": "3x=21", "answer": 7},{"question": "x−8=-8", "answer": 0},
    {"question": "2x+5=13", "answer": 4},{"question": "3x−2=7", "answer": 3},{"question": "4x=20", "answer": 5},
    {"question": "x+6=11", "answer": 5},{"question": "x−2=6", "answer": 8},{"question": "2x=8", "answer": 4},
    {"question": "5x+5=20", "answer": 3},{"question": "3x+1=10", "answer": 3},{"question": "x+2=5", "answer": 3},
    {"question": "x−1=4", "answer": 5},{"question": "2x−1=9", "answer": 5},{"question": "3x+9=15", "answer": 2},
    {"question": "x+4=8", "answer": 4},{"question": "2x+1=7", "answer": 3},{"question": "5x−3=12", "answer": 3},
    {"question": "x+3=8", "answer": 5},{"question": "2x=6", "answer": 3},{"question": "x+1=3", "answer": 2},
    {"question": "3x+6=15", "answer": 3},{"question": "2x−5=1", "answer": 3},{"question": "4x−4=12", "answer": 4},
    {"question": "x+6=12", "answer": 6},{"question": "3x=15", "answer": 5},{"question": "x−4=3", "answer": 7},
    {"question": "4x−2=10", "answer": 3},{"question": "x+7=12", "answer": 5}]

advanced_questions= [
    {"question": "2x+3=5x−9", "answer": 4},{"question": "3x−2=2x+4", "answer": 6},{"question": "4x+7=3x+11", "answer": 4},
    {"question": "2x−5=-8+3", "answer": 0},{"question": "x+8=3x−4", "answer": 6},{"question": "5x−3=2x+9", "answer": 4},
    {"question": "3x+7=4x−2", "answer": 9},{"question": "6x−5=3x+7", "answer": 4},{"question": "x+5=2x+5", "answer": 0},
    {"question": "4x+5=2x+13", "answer": 4},{"question": "4=3x+4", "answer": 0},{"question": "7x−5=3x+19", "answer": 6},
    {"question": "x+12=5x−4", "answer": 4},{"question": "8x+7=2x+19", "answer": 2},{"question": "5x−2=3x+8", "answer": 5},
    {"question": "3x+2=2x+10", "answer": 8},{"question": "6x−4=2x+16", "answer": 5},{"question": "4x+9=5x−5", "answer": 14},
    {"question": "2x+4=4", "answer": 0},{"question": "3x+1=2x+4", "answer": 3},{"question": "5x−6=3x+10", "answer": 8},
    {"question": "2x+6=4x−10", "answer": 8},{"question": "2x+1=3x−5", "answer": 6},{"question": "2x-x=0+x", "answer": 0},
    {"question": "7x=0", "answer": 0},{"question": "0+5=5+x", "answer": 0},{"question": "3x−4=4x−5", "answer": 1},
    {"question": "4x−3=5x-7", "answer": 4},{"question": "3x−1=4x-9", "answer": 8},{"question": "x+7=3x+3", "answer": 2},
    {"question": "2x+36=5x+9", "answer": 9},{"question": "7x−5=6x+3", "answer": 8},{"question": "3x+5=6x−4", "answer": 3},
    {"question": "4x+5=3x+6", "answer": 1},{"question": "2x−4=3x-8", "answer": 4}]

expert_questions= [
    {"question": "5(x−1)=3(2x-1)-2", "answer": 0},{"question": "4(2x−5)=3(3x+7)−49", "answer": 8},{"question": "3x+8=2(x−5)+3x", "answer": 9},
    {"question": "2(x+4)=3(x−1)+10", "answer": 1},{"question": "x^10=0", "answer": 0},{"question": "3(x+2)−5=2x+", "answer": 6},
    {"question": "(x/4)+3=x-3", "answer": 8},{"question": "7(x+1)=4(2x-2)+9", "answer": 6},{"question": "x^2=0", "answer": 0},
    {"question": "2x+3=4(x−2)−1", "answer": 6},{"question": "5(x+1)=3(2x−7)+14", "answer": 12},{"question": "4(x−6)=2x+8", "answer": 16},
    {"question": "2(x+5)=3x−6", "answer": 16},{"question": "7x−4=3x+12", "answer": 4},{"question": "5x+9=2(3x+4)", "answer": 1},
    {"question": "6x−2=3(x+4)+7", "answer": 7},{"question": "3(x+2)=6(x−1)+6", "answer": 2},{"question": "8x−7=3x+18", "answer": 5},
    {"question": "((9+x)/7)+2=2(−2+4)", "answer": 5},{"question": "4x−5=3(2x−4)-19", "answer": 13},{"question": "-18=3(3x-9)", "answer": 1},
    {"question": "5x−2=3(2x-1)−5", "answer": 6},{"question": "5=3+(x/2)", "answer": 4},{"question": "7(x−4)=5(2x+3)−49", "answer": 2},
    {"question": "x+8=5(x+2)−6", "answer": 1},{"question": "6x+1=5(2x−3)", "answer": 4},{"question": "3(x+4)=2x+18", "answer": 6},
    {"question": "5(x+3)=9+6+x", "answer": 0},{"question": "2(x-4)+3x=−5", "answer": 3},{"question": "((x+2)/5)​=3", "answer": 13},
    {"question": "4(x−2)=3x+8", "answer": 16},{"question": "7x+1=3(2-x)", "answer": 2},{"question": "2x+7=3x+5", "answer": 2},
    {"question": "3(x+5)=2(x+8)+10", "answer": 11},{"question": "2+4(3x+2)=2(5x+1)+14", "answer": 3}]
    
health = 3
question_count = 0
max_questions = 10

# limit username characters
def character_limit(username_entry):
    if len(username_entry.get()) > 0:
        username_entry.set(username_entry.get()[:10])

def display_enemy(enemy_list):
    enemy_img = Image.open(enemy_list["image"])
    enemy_img = enemy_img.resize((190, 190))
    enemy_img = ImageTk.PhotoImage(enemy_img)
    enemy_img_label.config(image=enemy_img)
    enemy_img_label.image = enemy_img

# open basic difficulty window
def basic_difficulty():

# basic difficulty window's setting
    title_screen.destroy()
    basic_screen = Tk()
    basic_screen.geometry('550x600')
    basic_screen.resizable(width=False, height=False)
    basic_screen.title('Basic difficulty')


# Creating widgets
    heart_img = Image.open('heart image.png')
    heart_img = heart_img.resize((60, 60),)
    life_img = ImageTk.PhotoImage(heart_img)

    life_img_label_1 = Label(basic_screen, image=life_img)
    life_img_label_1.place(x=0, y=3)

    life_img_label_2 = Label(basic_screen, image=life_img)
    life_img_label_2.place(x=60, y=3)

    life_img_label_3 = Label(basic_screen, image=life_img)
    life_img_label_3.place(x=125, y=3)

    global current_enemy
    current_enemy = random.choice(enemy_list)
    display_enemy(current_enemy)
    enemy_img_label = Label(basic_screen)
    enemy_img_label.place(x=190, y=5)

    basic_screen.mainloop()
    
# Title screen's setting
title_screen = Tk()
title_screen.geometry('550x600')
title_screen.resizable(width=False, height=False)
title_screen.title('MATH MAGE')

# images' settings
image_1 = Image.open('image 1.png')
image_1 = image_1.resize((190, 190),)
title_img = ImageTk.PhotoImage(image_1)


# Creating widgets
title_img_label = Label(title_screen, image=title_img)
title_img_label.pack(pady=20)

title = Label(title_screen, text="Math Mage", font=("Times New Roman",50, "bold"))
title.pack(pady=10)

username_label = Label(title_screen, text="Username:", font=("Courier New", 20, "bold"))
username_label.place(x=130, y=345)

username = StringVar() 
username_entry = Entry(title_screen, textvariable = username, width=10, font=("Arial", 16)) 
username_entry.place(x=280, y=350)
username.trace("w", lambda *args: character_limit(username))

basic_button =  Button(title_screen, font=("Helvetica", 23, "bold"), text="Basic", command =basic_difficulty, width=9, bg="green2")
basic_button.pack(pady=80)

advanced_button =  Button(title_screen, font=("Helvetica", 23, "bold"), text="Advanced", width=9, bg="yellow")
advanced_button.place(x=80, y=500)

expert_button =  Button(title_screen, font=("Helvetica", 23, "bold"), text="Expert", width=9, bg="red")
expert_button.place(x=295, y=500)


title_screen.mainloop()

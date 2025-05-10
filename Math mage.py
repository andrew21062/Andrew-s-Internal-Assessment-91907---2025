# Andrew Wong
# 08/04/25

import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

enemy_list = [
    {"image": "enemy1.png"}, {"image": "enemy2.png"}, {"image": "enemy3.png"}, {"image": "enemy4.png"},
    {"image": "enemy5.png"}, {"image": "enemy6.png"}, {"image": "enemy7.png"}, {"image": "enemy8.png"},
    {"image": "enemy9.png"}, {"image": "enemy10.png"}]

boss_list = [
    {"image": "boss 1.png"}, {"image": "boss 2.png"}, {"image": "boss 3.png"}, {"image": "boss 4.png"},
    {"image": "boss 5.png"}]

basic_questions = [
    {"question": "x+7=10", "answer": 3}, {"question": "2x−4=6", "answer": 5}, {"question": "x−3=7", "answer": 10},
    {"question": "3x+4=13", "answer": 3}, {"question": "5x−15=0", "answer": 3}, {"question": "4x+2=18", "answer": 4},
    {"question": "x+5=9", "answer": 4}, {"question": "3x=21", "answer": 7}, {"question": "x−8=-8", "answer": 0},
    {"question": "2x+5=13", "answer": 4}, {"question": "3x−2=7", "answer": 3}, {"question": "4x=20", "answer": 5},
    {"question": "x+6=11", "answer": 5}, {"question": "x−2=6", "answer": 8}, {"question": "2x=8", "answer": 4},
    {"question": "5x+5=20", "answer": 3}, {"question": "3x+1=10", "answer": 3}, {"question": "x+2=5", "answer": 3},
    {"question": "x−1=4", "answer": 5}, {"question": "2x−1=9", "answer": 5}, {"question": "3x+9=15", "answer": 2},
    {"question": "x+4=8", "answer": 4}, {"question": "2x+1=7", "answer": 3}, {"question": "5x−3=12", "answer": 3},
    {"question": "x+3=8", "answer": 5}, {"question": "2x=6", "answer": 3}, {"question": "x+1=3", "answer": 2},
    {"question": "3x+6=15", "answer": 3}, {"question": "2x−5=1", "answer": 3}, {"question": "4x−4=12", "answer": 4},
    {"question": "x+6=12", "answer": 6}, {"question": "3x=15", "answer": 5}, {"question": "x−4=3", "answer": 7},
    {"question": "4x−2=10", "answer": 3}, {"question": "x+7=12", "answer": 5}]

advanced_questions = [
    {"question": "2x+3=5x−9", "answer": 4}, {"question": "3x−2=2x+4", "answer": 6},
    {"question": "4x+7=3x+11", "answer": 4},
    {"question": "2x−5=-8+3", "answer": 0}, {"question": "x+8=3x−4", "answer": 6},
    {"question": "5x−3=2x+9", "answer": 4},
    {"question": "3x+7=4x−2", "answer": 9}, {"question": "6x−5=3x+7", "answer": 4},
    {"question": "x+5=2x+5", "answer": 0},
    {"question": "4x+5=2x+13", "answer": 4}, {"question": "4=3x+4", "answer": 0},
    {"question": "7x−5=3x+19", "answer": 6},
    {"question": "x+12=5x−4", "answer": 4}, {"question": "8x+7=2x+19", "answer": 2},
    {"question": "5x−2=3x+8", "answer": 5},
    {"question": "3x+2=2x+10", "answer": 8}, {"question": "6x−4=2x+16", "answer": 5},
    {"question": "4x+9=5x−5", "answer": 14},
    {"question": "2x+4=4", "answer": 0}, {"question": "3x+1=2x+4", "answer": 3},
    {"question": "5x−6=3x+10", "answer": 8},
    {"question": "2x+6=4x−10", "answer": 8}, {"question": "2x+1=3x−5", "answer": 6},
    {"question": "2x-x=0+x", "answer": 0},
    {"question": "7x=0", "answer": 0}, {"question": "0+5=5+x", "answer": 0},
    {"question": "3x−4=4x−5", "answer": 1},
    {"question": "4x−3=5x-7", "answer": 4}, {"question": "3x−1=4x-9", "answer": 8},
    {"question": "x+7=3x+3", "answer": 2},
    {"question": "2x+36=5x+9", "answer": 9}, {"question": "7x−5=6x+3", "answer": 8},
    {"question": "3x+5=6x−4", "answer": 3},
    {"question": "4x+5=3x+6", "answer": 1}, {"question": "2x−4=3x-8", "answer": 4}]

expert_questions = [
    {"question": "5(x−1)=3(2x-1)-2", "answer": 0}, {"question": "4(2x−5)=3(3x+7)−49", "answer": 8},
    {"question": "3x+8=2(x−5)+3x", "answer": 9},
    {"question": "2(x+4)=3(x−1)+10", "answer": 1}, {"question": "x^10=0", "answer": 0},
    {"question": "3(x+2)−5=2x+", "answer": 6},
    {"question": "(x/4)+3=x-3", "answer": 8}, {"question": "7(x+1)=4(2x-2)+9", "answer": 6},
    {"question": "x^2=0", "answer": 0},
    {"question": "2x+3=4(x−2)−1", "answer": 6}, {"question": "5(x+1)=3(2x−7)+14", "answer": 12},
    {"question": "4(x−6)=2x+8", "answer": 16},
    {"question": "2(x+5)=3x−6", "answer": 16}, {"question": "7x−4=3x+12", "answer": 4},
    {"question": "5x+9=2(3x+4)", "answer": 1},
    {"question": "6x−2=3(x+4)+7", "answer": 7}, {"question": "3(x+2)=6(x−1)+6", "answer": 2},
    {"question": "8x−7=3x+18", "answer": 5},
    {"question": "((9+x)/7)+2=2(−2+4)", "answer": 5}, {"question": "4x−5=3(2x−4)-19", "answer": 13},
    {"question": "-18=3(3x-9)", "answer": 1},
    {"question": "5x−2=3(2x-1)−5", "answer": 6}, {"question": "5=3+(x/2)", "answer": 4},
    {"question": "7(x−4)=5(2x+3)−49", "answer": 2},
    {"question": "x+8=5(x+2)−6", "answer": 1}, {"question": "6x+1=5(2x−3)", "answer": 4},
    {"question": "3(x+4)=2x+18", "answer": 6},
    {"question": "5(x+3)=9+6+x", "answer": 0}, {"question": "2(x-4)+3x=−5", "answer": 3},
    {"question": "((x+2)/5)=3", "answer": 13},
    {"question": "4(x−2)=3x+8", "answer": 16}, {"question": "7x+1=3(2-x)", "answer": 2},
    {"question": "2x+7=3x+5", "answer": 2},
    {"question": "3(x+5)=2(x+8)+10", "answer": 11}, {"question": "2+4(3x+2)=2(5x+1)+14", "answer": 3}]

# limit username characters
def character_limit(username_entry):
    if len(username_entry.get()) > 0:
        username_entry.set(username_entry.get()[:10])

def check_username_basic():
    global username_entry

    username = username_entry.get().strip()  # Remove leading/trailing spaces
    if username:  # If the entry is not empty after stripping spaces
        basic_difficulty()
    else:
        messagebox.showerror("Error", "Please enter a username.")

def check_difficulty():
    if difficulty == 0:
        basic_difficulty()
#    elif difficulty == 1:
#        advanced_difficulty()
#    elif difficulty == 1:
#        expert _difficulty()

def display_enemy_img():
    global enemy_img

    current_enemy = random.choice(enemy_list)
    current_enemy = current_enemy["image"]
    enemy_img = Image.open(current_enemy)
    enemy_img = enemy_img.resize((300, 300))
    enemy_img = ImageTk.PhotoImage(enemy_img)

def display_boss_img():
    global boss_img

    current_boss = random.choice(boss_list)
    current_boss = current_boss["image"]
    boss_img = Image.open(current_boss)
    boss_img = boss_img.resize((300, 300))
    boss_img = ImageTk.PhotoImage(boss_img)

def get_basic_question():
    global question_1, answer_button1, question_2, answer_button2, question_3, answer_button3

    question_1 = random.choice(basic_questions)
    answer_button1 = Button(main_win, text=f"\U000026A1 {question_1['question']}", command=question_1_damage,
                            font=("Arial", 22),width=10, bg='deep sky blue')
    answer_button1.place(x=75, y=445)

    question_2 = random.choice(basic_questions)
    answer_button2 = Button(main_win, text=f"\U00002600 {question_2['question']}", command=question_2_damage,
                            font=("Arial", 22),width=10, bg='orange')
    answer_button2.place(x=290, y=445)

    question_3 = random.choice(basic_questions)
    answer_button3 = Button(main_win, text=f"\U0001F319 {question_3['question']}", command=question_3_damage,
                            font=("Arial", 22),width=10, bg='yellow')
    answer_button3.place(x=180, y=520)

def check_player_hp():
    global life_img_label_1, life_img_label_2, life_img_label_3, player_hp

    try:
        life_img_label_1.destroy()
        life_img_label_2.destroy()
        life_img_label_3.destroy()
    except:
        pass

    heart_img = Image.open('heart_image.png')
    heart_img = heart_img.resize((65, 65), )
    life_img = ImageTk.PhotoImage(heart_img)

    if player_hp == 3:
        life_img_label_1 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_1.place(x=0, y=3)
        life_img_label_2 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_2.place(x=70, y=3)
        life_img_label_3 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_3.place(x=140, y=3)

    elif player_hp == 2:
        life_img_label_1 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_1.place(x=0, y=3)
        life_img_label_2 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_2.place(x=70, y=3)

    elif player_hp == 1:
        life_img_label_1 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_1.place(x=0, y=3)

    elif player_hp == 0:
        result_screen()

    main_win.mainloop()

def question_1_damage():
    global basic_enemy_hp
    basic_enemy_hp = basic_enemy_hp - question_1['answer']
    enemy_hp_label.config(text= f" HP: {basic_enemy_hp} ")
    check_enemy_hp()

def question_2_damage():
    global basic_enemy_hp
    basic_enemy_hp = basic_enemy_hp - question_2['answer']
    enemy_hp_label.config(text= f" HP: {basic_enemy_hp} ")
    check_enemy_hp()

def question_3_damage():
    global basic_enemy_hp
    basic_enemy_hp = basic_enemy_hp - question_3['answer']
    enemy_hp_label.config(text= f" HP: {basic_enemy_hp} ")
    check_enemy_hp()

def attack_effect():
    global attack_effect_label

    # Function to update the GIF frames in the label
    def update_frame(frame_index):
        try:
            attack_effect_label.config(image=frames[frame_index])
            main_win.after(70, update_frame, (frame_index + 1) % len(frames))
        except:
            pass

    gif_path = "damage_effect.gif"  # Replace with your GIF file path
    image = Image.open(gif_path)
    
    # Convert the image to a format that can be used in Tkinter
    frames = []
    try:
        for frame in range(image.n_frames):
            image.seek(frame)
            frames.append(ImageTk.PhotoImage(image.copy()))
        # Create a label to display the GIF
        attack_effect_label = Label(main_win)
        attack_effect_label.pack()

        # Start updating the frames
        update_frame(0)
    except:
        pass

def check_enemy_hp():
    global player_hp, enemy_No

    if basic_enemy_hp <= 0:
        # reset the player's hp
        player_hp = 3
        # Increase the question count when the enemy is defeated
        enemy_No += 1
        if enemy_No > 6:
            result_screen()
        else:
            attack_effect()
            main_win.after(900, check_difficulty)
    else:
        player_hp -= 1
        get_basic_question()
        if player_hp <= 0:
            result_screen()
        else:
            check_player_hp()

# open info screen
def show_info_screen():
    global info_screen

    # Make sure only one info screen is opened at a time
    if info_screen is None or not Toplevel.winfo_exists(info_screen):
        # info screen's settings
        info_screen = Toplevel()
        info_screen.geometry('450x330')
        info_screen.resizable(width=False, height=False)
        info_screen.title('Info screen')

        # info screen's widgets
        tutorials_title = Label(info_screen, text="How To Play \U0001F52A :",  font=("Arial", 15, "bold"))
        tutorials_title.place(x=10,y=5)
        tutorials_text_1 = Label(info_screen, text=" - You chose one of the four formulas/attack at the bottom. "
                                                   "\n (\U000026A1, \U00002600, \U0001F319) The result of the chosen formula( x )"
                                                   "\n  will be damage dealt to the enemy.", font=("Arial", 12))
        tutorials_text_1.place(x=0,y=50)
        tutorials_text_2 = Label(info_screen, text=" - There are multiple solutions, however some formulas will "
                                      "\n insta kill the enemy." , font=("Arial", 12))
        tutorials_text_2.place(x=0,y=120)
        tutorials_text_3 = Label(info_screen, text=" - If the chosen formula does not immediately defeat the enemy"
                                      "\n then you will loss one heart. When all hearts are lost, it "
                                      "\n will be game over, however if you defeat your current enemy "
                                      "\n you will regain all your hearts. \U0001F496", font=("Arial", 12))
        tutorials_text_3.place(x=0,y=170)
        tutorials_text_4 = Label(info_screen, text=" - To win, you must defeat 6 enemies without losing all "
                                      "\n your hearts", font=("Arial", 12))
        tutorials_text_4.place(x=0, y=260)

        info_screen.protocol("WM_DELETE_WINDOW", on_closing)
    else:
        info_screen.focus()

def on_closing():
    global info_screen
    info_screen.destroy()
    info_screen = None

def restart():
    # clear the main screen
    for widget in main_win.winfo_children():
        widget.destroy()
    main_win.title('MATH MAGE')
    title_screen()


def result_screen():
    # clear the main screen
    for widget in main_win.winfo_children():
        widget.destroy()

    main_win.title('Result')
    text_1_label = Label(main_win, text=" You got: ", font=("Arial", 30, "bold"))
    text_1_label.pack(pady=10)

    if enemy_No == 6:
        result_label = Label(main_win, text=" A ", font=("Arial", 125, "bold"), fg="green2")
        result_label.pack()
    elif enemy_No <= 2:
        result_label = Label(main_win, text=" F ", font=("Arial", 125, "bold"), fg="red4")
        result_label.pack()
    elif enemy_No >= 4:
        result_label = Label(main_win, text=" B ", font=("Arial", 125, "bold"), fg="orange")
        result_label.pack()
    elif enemy_No < 4:
        result_label = Label(main_win, text=" C ", font=("Arial", 125, "bold"), fg="red")
        result_label.pack()

    score_label = Label(main_win, text=f"Score: {enemy_No}/6", font=("Arial", 30, "bold"))
    score_label.pack()

    if difficulty == 0:
        level_label = Label(main_win, text=f"Difficulty: \nBasic", font=("Arial", 30, "bold"), fg="green2")
        level_label.pack(pady=5)

    if difficulty == 1:
        level_label = Label(main_win, text=f"Difficulty: \nAdvanced", font=("Arial", 30, "bold"), fg="orange")
        level_label.pack(pady=5)

    if difficulty == 2:
        level_label = Label(main_win, text=f"Difficulty: \nExpert ", font=("Arial", 30, "bold"), fg="red")
        level_label.pack(pady=5)

    print_button = Button(main_win, text="Print result", font=("Helvetica", 23, "bold"), width=9, borderwidth=3,
                          relief="raised")
    print_button.pack()

    aagain_button = Button(main_win, text="Again", command=restart, font=("Helvetica", 23, "bold"), width=9, borderwidth=3,
                           relief="raised")
    aagain_button.place(x=80, y=510)

    end_button = Button(main_win, text="End", command= main_win.destroy , font=("Helvetica", 23, "bold"), width=9, borderwidth=3, relief="raised")
    end_button.place(x=295, y=510)

# open basic difficulty window
def basic_difficulty():
    global difficulty, basic_enemy_hp, basic_boss_hp, enemy_hp_label
    difficulty = 0
    basic_enemy_hp = 10
    basic_boss_hp = 15

    # clear the main screen
    for widget in main_win.winfo_children():
        widget.destroy()

    # create widgets
    if enemy_No <= 5:
        display_enemy_img()

        enemy_hp_label = Label(main_win, text=f" HP: {basic_enemy_hp} ", font=("Arial", 22, "bold"), bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        enemy_img_label = Label(main_win, image=enemy_img, borderwidth=3, relief="solid")
        enemy_img_label.place(x=125, y=80)
    else:
        display_boss_img()

        enemy_hp_label = Label(main_win, text=f" HP:  {basic_boss_hp} ", font=("Arial", 22, "bold"), bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        boss_img_label = Label(main_win, image=boss_img, borderwidth=3, relief="solid")
        boss_img_label.place(x=125, y=80)

    question_No_label = Label(main_win, text=f" {enemy_No}/6 ", font=("Arial", 20, "bold"), bg='white',
                              borderwidth=2, relief="solid")
    question_No_label.place(x=470, y=10)

    info_button = Button(main_win, text=" ? ", command= show_info_screen, font=("Arial", 16, "bold"),
                         width=3, fg="green")
    info_button.place(x=480, y=360)

    get_basic_question()
    check_player_hp()

def title_screen():
    # Setting up variables
    global player_hp, enemy_No, max_enemy, title_img_label, title_label, username_label
    global username_entry, basic_button, advanced_button, expert_button, info_screen
    player_hp = 3
    enemy_No = 1
    max_enemy = 6
    info_screen = None

    # images' settings
    image_1 = Image.open('image 1.png')
    image_1 = image_1.resize((190, 190), )
    title_img = ImageTk.PhotoImage(image_1)

    title_img_label = Label(main_win, image=title_img)
    title_img_label.pack(pady=20)

    title_label = Label(main_win, text="Math Mage", font=("Times New Roman", 50, "bold"))
    title_label.pack(pady=10)

    username_label = Label(main_win, text="Username: ", font=("Courier New", 22, "bold"))
    username_label.place(x=126, y=345)

    username = StringVar()
    username_entry = Entry(main_win, textvariable=username, width=10, font=("Arial", 16))
    username_entry.place(x=283, y=350)
    username.trace("w", lambda *args: character_limit(username))

    basic_button = Button(main_win, text="Basic", command=check_username_basic, font=("Helvetica", 23, "bold"),
                          width=9, bg="green2", borderwidth=3, relief="raised")
    basic_button.pack(pady=80)

    advanced_button = Button(main_win, text="Advanced", font=("Helvetica", 23, "bold"), width=9, bg="yellow",
                             borderwidth=3, relief="raised")
    advanced_button.place(x=80, y=500)

    expert_button = Button(main_win, text="Expert", font=("Helvetica", 23, "bold"), width=9, bg="red",
                           borderwidth=3, relief="raised")
    expert_button.place(x=295, y=500)

    main_win.mainloop()

# main window's setting
main_win = Tk()
main_win.geometry('550x600')
main_win.resizable(width=False, height=False)
main_win.title('MATH MAGE')
title_screen()

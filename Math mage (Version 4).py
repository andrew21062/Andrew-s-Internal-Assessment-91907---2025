# Andrew Wong
# Version 4.2.0

import pygame
import random
import pyglet
from tkinter import *
from tkinter import messagebox
from tkinter import Toplevel
from PIL import Image, ImageTk

# 'Enemy' is a class that contains all the image location of enemies used for this program
class Enemy:
    # the image location of all normal enemies made into a list
    enemy_list = [
        {"image": "assets/enemies/enemy1.png"}, {"image": "assets/enemies/enemy2.png"},
        {"image": "assets/enemies/enemy3.png"},
        {"image": "assets/enemies/enemy4.png"}, {"image": "assets/enemies/enemy5.png"},
        {"image": "assets/enemies/enemy6.png"},
        {"image": "assets/enemies/enemy7.png"}, {"image": "assets/enemies/enemy8.png"},
        {"image": "assets/enemies/enemy9.png"},
        {"image": "assets/enemies/enemy10.png"}]

    # the image location of all boss enemies made into a list
    boss_list = [
        {"image": "assets/bosses/boss 1.png"}, {"image": "assets/bosses/boss 2.png"},
        {"image": "assets/bosses/boss 3.png"}, {"image": "assets/bosses/boss 4.png"},
        {"image": "assets/bosses/boss 5.png"}]

    def __init__(self, img_location):
        self.img_location = img_location


global enemy_list, boss_list
list_1 = Enemy("enemy_list")
list_2 = Enemy("boss_list")

class InfoScreen:
    def __init__(self, on_closing_callback):
        self.info_screen = None
        self.on_closing = on_closing_callback

    def show_info_screen(self):
        # Make sure only one info screen is opened at a time
        if self.info_screen is None or not Toplevel.winfo_exists(self.info_screen):
            # info screen's geometry
            self.info_screen = Toplevel()
            self.info_screen.geometry('450x330')
            self.info_screen.configure(bg='white')
            self.info_screen.resizable(width=False, height=False)
            self.info_screen.title('Info screen')

            # info screen's widgets
            tutorials_title = Label(self.info_screen, text="How To Play \U0001F52A :", font=("Arial", 15, "bold"), bg='white')
            tutorials_title.place(x=10, y=5)
            tutorials_text_1 = Label(self.info_screen, text=" - You chose one of the four formulas/attack at the bottom. "
                                                       "\n (\U000026A1, \U00002600, \U0001F319) The result of the chosen formula( x )"
                                                       "\n  will be damage dealt to the enemy.", font=("Arial", 12), bg='white')
            tutorials_text_1.place(x=0, y=50)
            tutorials_text_2 = Label(self.info_screen, text=" - There are multiple solutions, however some formulas will "
                                                       "\n insta kill the enemy.", font=("Arial", 12), bg='white')
            tutorials_text_2.place(x=0, y=120)
            tutorials_text_3 = Label(self.info_screen, text=" - If the chosen formula does not immediately defeat the enemy"
                                                       "\n then you will loss one heart. When all hearts are lost, it "
                                                       "\n will be game over, however if you defeat your current enemy "
                                                       "\n you will regain all your hearts. \U0001F496", font=("Arial", 12), bg='white')
            tutorials_text_3.place(x=0, y=170)
            tutorials_text_4 = Label(self.info_screen, text=" - To win, you must defeat 6 enemies without losing all "
                                                       "\n your hearts.", font=("Arial", 12), bg='white')
            tutorials_text_4.place(x=0, y=260)

            self.info_screen.protocol("WM_DELETE_WINDOW", self.on_closing)
        else:
            self.info_screen.focus()

    def terminate_info(self):
        self.info_screen.destroy()


def on_closing():
    info.terminate_info()

info = InfoScreen(on_closing)


# questions list for basic difficultly (with answers)
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

# questions list for advanced difficultly (with answers)
advanced_questions = [
    {"question": "2x+3=5x−9", "answer": 4}, {"question": "3x−2=2x+4", "answer": 6},
    {"question": "4x+7=3x+11", "answer": 4}, {"question": "2x−5=-8+3", "answer": 0},
    {"question": "x+8=3x−4", "answer": 6}, {"question": "5x−3=2x+9", "answer": 4},
    {"question": "3x+7=4x−2", "answer": 9}, {"question": "6x−5=3x+7", "answer": 4},
    {"question": "x+5=2x+5", "answer": 0}, {"question": "4x+5=2x+13", "answer": 4},
    {"question": "4=3x+4", "answer": 0}, {"question": "7x−5=3x+19", "answer": 6},
    {"question": "x+12=5x−4", "answer": 4}, {"question": "8x+7=2x+19", "answer": 2},
    {"question": "5x−2=3x+8", "answer": 5}, {"question": "3x+2=2x+10", "answer": 8},
    {"question": "6x−4=2x+16", "answer": 5}, {"question": "4x+9=5x−5", "answer": 14},
    {"question": "2x+4=4", "answer": 0}, {"question": "3x+1=2x+4", "answer": 3},
    {"question": "5x−6=3x+10", "answer": 8}, {"question": "2x+6=4x−10", "answer": 8},
    {"question": "2x+1=3x−5", "answer": 6}, {"question": "2x-x=0+x", "answer": 0},
    {"question": "7x=0", "answer": 0}, {"question": "0+5=5+x", "answer": 0},
    {"question": "3x−4=4x−5", "answer": 1}, {"question": "4x−3=5x-7", "answer": 4},
    {"question": "3x−1=4x-9", "answer": 8}, {"question": "x+7=3x+3", "answer": 2},
    {"question": "2x+36=5x+9", "answer": 9}, {"question": "7x−5=6x+3", "answer": 8},
    {"question": "3x+5=6x−4", "answer": 3}, {"question": "4x+5=3x+6", "answer": 1},
    {"question": "2x−4=3x-8", "answer": 4}]

# questions list for expert difficultly (with answers)
expert_questions = [
    {"question": "5(x−1)=3(2x-1)-2", "answer": 0}, {"question": "4(2x−5)=3(3x+7)−49", "answer": 8},
    {"question": "3x+8=2(x−5)+3x", "answer": 9}, {"question": "2(x+4)=3(x−1)+10", "answer": 1},
    {"question": "x^10=0", "answer": 0}, {"question": "3(x+2)−5=2x", "answer": 6},
    {"question": "(x/4)+3=x-3", "answer": 8}, {"question": "7(x+1)=4(2x-2)+9", "answer": 6},
    {"question": "x^2=0", "answer": 0}, {"question": "2x+3=4(x−2)−1", "answer": 6},
    {"question": "5(x+1)=3(2x−7)+14", "answer": 12}, {"question": "4(x−6)=2x+8", "answer": 16},
    {"question": "2(x+5)=3x−6", "answer": 16}, {"question": "7x−4=3x+12", "answer": 4},
    {"question": "5x+9=2(3x+4)", "answer": 1}, {"question": "6x−2=3(x+4)+7", "answer": 7},
    {"question": "3(x+2)=6(x−1)+6", "answer": 2}, {"question": "8x−7=3x+18", "answer": 5},
    {"question": "((9+x)/7)+2=2(−2+4)", "answer": 5}, {"question": "4x−5=3(2x−4)-19", "answer": 13},
    {"question": "-18=3(3x-9)", "answer": 1}, {"question": "5x−2=3(2x-1)−5", "answer": 6},
    {"question": "5=3+(x/2)", "answer": 4}, {"question": "7(x−4)=5(2x+3)−49", "answer": 2},
    {"question": "x+8=5(x+2)−6", "answer": 1}, {"question": "6x+1=5(2x−3)", "answer": 4},
    {"question": "3(x+4)=2x+18", "answer": 6}, {"question": "5(x+3)=9+6+x", "answer": 0},
    {"question": "2(x-4)+3x=−5", "answer": 3}, {"question": "((x+2)/5)=3", "answer": 13},
    {"question": "4(x−2)=3x+8", "answer": 16}, {"question": "7x+1=3(2-x)", "answer": 2},
    {"question": "2x+7=3x+5", "answer": 2}, {"question": "3(x+5)=2(x+8)+10", "answer": 11},
    {"question": "2+4(3x+2)=2(5x+1)+14", "answer": 3}]


# completely shutdown the program
def terminate():
    main_win.destroy()
    pygame.mixer_music.stop()


# battle BGM's settings
def BGM():
    # import the music as mp3
    pygame.mixer.music.load("assets/audio/battle BGM.mp3")
    # set the volume to 50%
    pygame.mixer.music.set_volume(0.5)
    # loop the music 100 times
    pygame.mixer.music.play(loops=100)


# limit username's characters to 10
def character_limit(username_entry):
    if len(username_entry.get()) > 0:
        username_entry.set(username_entry.get()[:10])


# after clicking the basic difficulty, check the username's input
def check_username_basic():
    global user

    user = username_entry.get()
    # remove leading and trailing spaces
    username_check = username_entry.get().strip()

    # if the entry is not empty after stripping spaces, then play BGM and move on to question screen
    if username_check:
        BGM()
        basic_difficulty()
    else:
        # show error message if username is empty after stripping spaces
        messagebox.showerror("Error", "Please enter a username.")


# after clicking the advanced difficulty, check the username's input
def check_username_advanced():
    global user

    user = username_entry.get()
    # remove leading and trailing spaces
    username_check = username_entry.get().strip()

    # if the entry is not empty after stripping spaces, then play BGM and move on to question screen
    if username_check:
        BGM()
        advanced_difficulty()
    else:
        # show error message if username is empty after stripping spaces
        messagebox.showerror("Error", "Please enter a username.")


# after clicking the expert difficulty, check the username's input
def check_username_expert():
    global user

    user = username_entry.get()
    # remove leading and trailing spaces
    username_check = username_entry.get().strip()

    # if the entry is not empty after stripping spaces, then play BGM and move on to question screen
    if username_check:
        BGM()
        expert_difficulty()
    else:
        # show error message if username is empty after stripping spaces
        messagebox.showerror("Error", "Please enter a username.")


# check the difficulty the player chose, then jump to the corresponding question screen
def check_difficulty():
    # unpause the BGM
    pygame.mixer.music.unpause()

    # if difficulty is 0 then jump to basic difficulty screen
    if difficulty == 0:
        basic_difficulty()
    # if difficulty is 1 then jump to advanced difficulty screen
    elif difficulty == 1:
        advanced_difficulty()
    # if difficulty is 2 then jump to expert difficulty screen
    elif difficulty == 2:
        expert_difficulty()


# normal enemies' image settings
def display_enemy_img():
    global enemy_img

    # chose a random image from enemy_list, then import it
    current_enemy = random.choice(list_1.enemy_list)
    current_enemy = current_enemy["image"]
    enemy_img = Image.open(current_enemy)
    # resize the image to 300x300 pixels
    enemy_img = enemy_img.resize((300, 300))
    enemy_img = ImageTk.PhotoImage(enemy_img)


# boss enemies' image settings
def display_boss_img():
    global boss_img

    # chose a random image from boss_list, then import it
    current_boss = random.choice(list_2.boss_list)
    current_boss = current_boss["image"]
    boss_img = Image.open(current_boss)
    # resize the image to 300x300 pixels
    boss_img = boss_img.resize((300, 300))
    boss_img = ImageTk.PhotoImage(boss_img)


# get 3 questions from basic_questions
def get_basic_question():
    global question_1, answer_button1, question_2, answer_button2, question_3, answer_button3

    question_1 = random.choice(basic_questions)
    answer_button1 = Button(main_win, text=f"\U000026A1 {question_1['question']}", command=question_1_damage,
                            font=("Arial", 22), width=10, bg='deep sky blue')
    answer_button1.place(x=75, y=445)

    question_2 = random.choice(basic_questions)
    answer_button2 = Button(main_win, text=f"\U00002600 {question_2['question']}", command=question_2_damage,
                            font=("Arial", 22), width=10, bg='orange')
    answer_button2.place(x=290, y=445)

    question_3 = random.choice(basic_questions)
    answer_button3 = Button(main_win, text=f"\U0001F319 {question_3['question']}", command=question_3_damage,
                            font=("Arial", 22), width=10, bg='yellow')
    answer_button3.place(x=180, y=520)


# get 3 questions from advanced_questions
def get_advanced_question():
    global question_1, answer_button1, question_2, answer_button2, question_3, answer_button3

    question_1 = random.choice(advanced_questions)
    answer_button1 = Button(main_win, text=f"\U000026A1 {question_1['question']}", command=question_1_damage,
                            font=("Arial", 21), width=12, bg='deep sky blue')
    answer_button1.place(x=75, y=445)

    question_2 = random.choice(advanced_questions)
    answer_button2 = Button(main_win, text=f"\U00002600 {question_2['question']}", command=question_2_damage,
                            font=("Arial", 21), width=12, bg='orange')
    answer_button2.place(x=290, y=445)

    question_3 = random.choice(advanced_questions)
    answer_button3 = Button(main_win, text=f"\U0001F319 {question_3['question']}", command=question_3_damage,
                            font=("Arial", 21), width=12, bg='yellow')
    answer_button3.place(x=180, y=520)


# get 3 questions from expert_questions
def get_expert_question():
    global question_1, answer_button1, question_2, answer_button2, question_3, answer_button3

    try:
        question_1 = random.choice(expert_questions)
        answer_button1 = Button(main_win, text=f"\U000026A1 {question_1['question']}", command=question_1_damage,
                                font=("Arial", 17), width=20, bg='deep sky blue')
        answer_button1.place(x=5, y=450)

        question_2 = random.choice(expert_questions)
        answer_button2 = Button(main_win, text=f"\U00002600 {question_2['question']}", command=question_2_damage,
                                font=("Arial", 17), width=20, bg='orange')
        answer_button2.place(x=275, y=450)

        question_3 = random.choice(expert_questions)
        answer_button3 = Button(main_win, text=f"\U0001F319 {question_3['question']}", command=question_3_damage,
                                font=("Arial", 17), width=20, bg='yellow')
        answer_button3.place(x=140, y=520)
    except:
        pass


# check the player's remain HP, then show hearts according to that number
def check_player_hp():
    global life_img_label_1, life_img_label_2, life_img_label_3, player_hp

    # try to clean the heart images from pervious questions, if can't then move on
    try:
        life_img_label_1.destroy()
        life_img_label_2.destroy()
        life_img_label_3.destroy()
    except:
        pass

    # import heart image
    heart_img = Image.open("assets/player HP/heart 1.png")
    # resize the image to 65x65 pixels
    heart_img = heart_img.resize((65, 65), )
    life_img = ImageTk.PhotoImage(heart_img)

    # if the player's HP is 3, then put 3 hearts on the window
    if player_hp == 3:
        life_img_label_1 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_1.place(x=0, y=3)
        life_img_label_2 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_2.place(x=70, y=3)
        life_img_label_3 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_3.place(x=140, y=3)
    # if the player's HP is 2, then put 2 hearts on the window
    elif player_hp == 2:
        life_img_label_1 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_1.place(x=0, y=3)
        life_img_label_2 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_2.place(x=70, y=3)
    # if the player's HP is 1, then put 1 heart on the window
    elif player_hp == 1:
        life_img_label_1 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_1.place(x=0, y=3)
    # if the player's HP is 0, then put jump to result screen
    elif player_hp == 0:
        result_screen()

    main_win.mainloop()


# calculate question 1's damage on each difficulty
def question_1_damage():
    global basic_enemy_hp, advanced_enemy_hp, expert_enemy_hp

    if difficulty == 0:
        basic_enemy_hp = basic_enemy_hp - question_1['answer']
        enemy_hp_label.config(text=f" HP: {basic_enemy_hp} ")
        check_enemy_hp()
    elif difficulty == 1:
        advanced_enemy_hp = advanced_enemy_hp - question_1['answer']
        enemy_hp_label.config(text=f" HP: {advanced_enemy_hp} ")
        check_enemy_hp()
    elif difficulty == 2:
        expert_enemy_hp = expert_enemy_hp - question_1['answer']
        enemy_hp_label.config(text=f" HP: {expert_enemy_hp} ")
        check_enemy_hp()


# calculate question 2's damage on each difficulty
def question_2_damage():
    global basic_enemy_hp, advanced_enemy_hp, expert_enemy_hp

    if difficulty == 0:
        basic_enemy_hp = basic_enemy_hp - question_2['answer']
        enemy_hp_label.config(text=f" HP: {basic_enemy_hp} ")
        check_enemy_hp()
    elif difficulty == 1:
        advanced_enemy_hp = advanced_enemy_hp - question_2['answer']
        enemy_hp_label.config(text=f" HP: {advanced_enemy_hp} ")
        check_enemy_hp()
    elif difficulty == 2:
        expert_enemy_hp = expert_enemy_hp - question_2['answer']
        enemy_hp_label.config(text=f" HP: {expert_enemy_hp} ")
        check_enemy_hp()


# calculate question 3's damage on each difficulty
def question_3_damage():
    global basic_enemy_hp, advanced_enemy_hp, expert_enemy_hp

    if difficulty == 0:
        basic_enemy_hp = basic_enemy_hp - question_3['answer']
        enemy_hp_label.config(text=f" HP: {basic_enemy_hp} ")
        check_enemy_hp()
    elif difficulty == 1:
        advanced_enemy_hp = advanced_enemy_hp - question_3['answer']
        enemy_hp_label.config(text=f" HP: {advanced_enemy_hp} ")
        check_enemy_hp()
    elif difficulty == 2:
        expert_enemy_hp = expert_enemy_hp - question_3['answer']
        enemy_hp_label.config(text=f" HP: {expert_enemy_hp} ")
        check_enemy_hp()


# attack gif's settings
def attack_effect():
    global attack_effect_label

    # Function to update the GIF frames in the label
    # for attack effect 1 and 2, it is 70 millisecond per frame
    # for attack effect 3, it is 125 millisecond per frame
    def update_frame(frame_index):
        try:
            attack_effect_label.config(image=frames[frame_index])
            main_win.after(70, update_frame, (frame_index + 1) % len(frames))
        except:
            pass

    gif_path = "assets/attack gif/attack effect 1.gif"
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


# check the enemy's HP on each difficulty
def check_enemy_hp():
    global player_hp, enemy_No

    # for basic difficulty:
    if difficulty == 0:
        # check if the enemy had been defeated
        if basic_enemy_hp <= 0:
            # if so reset the player's hp
            player_hp = 3
            # if so increase the question count
            enemy_No += 1
            # if the total enemies defeated is over 6, then jump to result screen
            if enemy_No > 6:
                result_screen()
            # if not over 6 then:
            else:
                # play attack gif
                attack_effect()
                # pause BGM, then play attack sound effect
                pygame.mixer_music.pause()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/attack sound.mp3"))
                # after 900 millisecond check the player's difficulty to refresh the question screen
                main_win.after(900, check_difficulty)
        # if the enemy is not dead then:
        else:
            # the player loses one HP
            player_hp -= 1
            # get new questions
            get_basic_question()
            # if the player's HP is 0, then jump to result screen
            if player_hp <= 0:
                result_screen()
            else:
                # check the player HP to refresh heart images
                check_player_hp()

    # for advanced difficulty:
    if difficulty == 1:
        # check if the enemy had been defeated
        if advanced_enemy_hp <= 0:
            # if so reset the player's hp
            player_hp = 3
            # if so increase the question count
            enemy_No += 1
            # if the total enemies defeated is over 6, then jump to result screen
            if enemy_No > 6:
                result_screen()
            # if not over 6 then:
            else:
                # play attack gif
                attack_effect()
                # pause BGM, then play attack sound effect
                pygame.mixer_music.pause()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/attack sound.mp3"))
                # after 900 millisecond check the player's difficulty to refresh the question screen
                main_win.after(900, check_difficulty)
        # if the enemy is not dead then:
        else:
            # the player loses one HP
            player_hp -= 1
            # get new questions
            get_advanced_question()
            # if the player's HP is 0, then jump to result screen
            if player_hp <= 0:
                result_screen()
            else:
                # check the player HP to refresh heart images
                check_player_hp()

    # for expert difficulty:
    if difficulty == 2:
        # check if the enemy had been defeated
        if expert_enemy_hp <= 0:
            # if so reset the player's hp
            player_hp = 3
            # if so increase the question count
            enemy_No += 1
            # if the total enemies defeated is over 6, then jump to result screen
            if enemy_No > 6:
                result_screen()
            # if not over 6 then:
            else:
                # play attack gif
                attack_effect()
                # pause BGM, then play attack sound effect
                pygame.mixer_music.pause()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/attack sound.mp3"))
                # after 900 millisecond check the player's difficulty to refresh the question screen
                main_win.after(900, check_difficulty)
        # if the enemy is not dead then:
        else:
            # the player loses one HP
            player_hp -= 1
            # get new questions
            get_expert_question()
            # if the player's HP is 0, then jump to result screen
            if player_hp <= 0:
                result_screen()
            else:
                # check the player HP to refresh heart images
                check_player_hp()


# close the info screen
def on_closing():
    global info_screen

    info_screen.destroy()
    info_screen = None


# restart the whole program
def restart():
    # clear the main screen
    for widget in main_win.winfo_children():
        widget.destroy()
    # reset the program
    main_win.title('MATH MAGE')
    title_screen()


# the result screen's settings
def result_screen():
    # clear the main screen
    try:
        for widget in main_win.winfo_children():
            widget.destroy()
    except:
        pass

    # stop the BGM
    pygame.mixer_music.stop()

    # change the window's title
    main_win.title('Result')

    # result screen's widgets
    background_5 = Image.open("assets/backgrounds/result background.png")
    background_5 = background_5.resize((560, 610), )
    result_background = ImageTk.PhotoImage(background_5)

    result_background_label = Label(main_win, image=result_background)
    result_background_label.place(x=-10, y=0)

    text_1_label = Label(main_win, text=f"  {user} got: ", font=("ARCADECLASSIC", 30, "bold"))
    text_1_label.pack(pady=10)

    # if the more than 6 enemies had been defeated then:
    if enemy_No > 6:
        # play victory music
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/win sound.mp3"))
        # show grade A and score
        result_label = Label(main_win, text="   A   ", font=("ARCADECLASSIC", 125, "bold"), fg="green2")
        result_label.pack()
        score_label = Label(main_win, text=" Score: 6/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()
    elif enemy_No == 6:
        # play victory music
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/win sound.mp3"))
        # show grade A and score
        result_label = Label(main_win, text="   A   ", font=("ARCADECLASSIC", 125, "bold"), fg="green2")
        result_label.pack()
        score_label = Label(main_win, text=" Score: 6/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()
    # if less than or equal to 2 enemies defeated then:
    elif enemy_No <= 2:
        # play game over music
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/game over sound.mp3"))
        # show grade F and score
        result_label = Label(main_win, text="   F   ", font=("ARCADECLASSIC", 125, "bold"), fg="red4")
        result_label.pack()
        score_label = Label(main_win, text=f" Score: {enemy_No}/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()
    # if more than or equal to 4 enemies defeated then:
    elif enemy_No >= 4:
        # play victory music
        pygame.mixer_music.stop()
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/win sound.mp3"))
        # show grade B and score
        result_label = Label(main_win, text="   B   ", font=("ARCADECLASSIC", 125, "bold"), fg="orange")
        result_label.pack()
        score_label = Label(main_win, text=f" Score: {enemy_No}/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()
    # if less than 4 enemies defeated then:
    elif enemy_No < 4:
        # play game over music
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/game over sound.mp3"))
        # show grade C and score
        result_label = Label(main_win, text="   C   ", font=("ARCADECLASSIC", 125, "bold"), fg="red")
        result_label.pack()
        score_label = Label(main_win, text=f" Score: {enemy_No}/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()

    # show basic difficulty
    difficulty_label = Label(main_win, text=f"Difficulty:", font=("ARCADECLASSIC", 27, "bold"))
    difficulty_label.pack(pady=10)
    if difficulty == 0:
        level_label = Label(main_win, text=f"    Basic    ", font=("ARCADECLASSIC", 30, "bold"), fg="green2")
        level_label.pack()
    # show advanced difficulty
    if difficulty == 1:
        level_label = Label(main_win, text=f"   Advanced  ", font=("ARCADECLASSIC", 30, "bold"), fg="orange")
        level_label.pack()
    # show expert difficulty
    if difficulty == 2:
        level_label = Label(main_win, text=f"    Expert   ", font=("ARCADECLASSIC", 30, "bold"), fg="red")
        level_label.pack()

    # again button's settings
    again_button = Button(main_win, text="\u2764 Again", command=restart, font=("Helvetica", 23, "bold"), bg="white",
                          width=9, borderwidth=3, relief="raised")
    again_button.place(x=80, y=490)
    # end button's settings
    end_button = Button(main_win, text="\U0001F480 End", command=main_win.destroy, font=("Helvetica", 23, "bold"),
                        bg="white",
                        width=9, borderwidth=3, relief="raised")
    end_button.place(x=295, y=490)

    main_win.mainloop()


# basic questions screen's settings
def basic_difficulty():
    # setting up variables
    global difficulty, basic_enemy_hp, basic_boss_hp, enemy_hp_label
    difficulty = 0
    basic_enemy_hp = 10
    basic_boss_hp = 15

    # clear the main screen
    for widget in main_win.winfo_children():
        widget.destroy()

    # resume the BGM if stopped otherwise move on to the next line
    try:
        pygame.mixer_music.unpause()
    except:
        pass

    # create widgets
    background_2 = Image.open("assets/backgrounds/basic background.png")
    background_2 = background_2.resize((560, 610), )
    basic_background = ImageTk.PhotoImage(background_2)

    basic_background_label = Label(main_win, image=basic_background)
    basic_background_label.place(x=-10, y=0)

    if enemy_No <= 5:

        display_enemy_img()

        enemy_hp_label = Label(main_win, text=f" HP: {basic_enemy_hp} ", font=("ARCADECLASSIC", 22, "bold"), bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        enemy_img_label = Label(main_win, image=enemy_img, borderwidth=3, relief="solid")
        enemy_img_label.place(x=125, y=80)
    else:
        display_boss_img()

        enemy_hp_label = Label(main_win, text=f" HP:  {basic_boss_hp} ", font=("ARCADECLASSIC", 22, "bold"), bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        boss_img_label = Label(main_win, image=boss_img, borderwidth=3, relief="solid")
        boss_img_label.place(x=125, y=80)

    question_No_label = Label(main_win, text=f" {enemy_No}/6 ", font=("ARCADECLASSIC", 23, "bold"), bg='white',
                              borderwidth=2, relief="solid")
    question_No_label.place(x=480, y=10)

    info_button = Button(main_win, text=" ? ", command=info.show_info_screen, font=("ARCADECLASSIC", 16, "bold"),
                         width=3, fg="green")
    info_button.place(x=480, y=360)

    # get basic questions
    get_basic_question()
    # check the player's HP for heart images
    check_player_hp()


# advanced questions screen's settings
def advanced_difficulty():
    # setting up variables
    global difficulty, advanced_enemy_hp, advanced_boss_hp, enemy_hp_label
    difficulty = 1
    advanced_enemy_hp = 10
    advanced_boss_hp = 15

    # clear the main screen
    for widget in main_win.winfo_children():
        widget.destroy()

    # resume the BGM if stopped otherwise move on to the next line
    try:
        pygame.mixer_music.unpause()
    except:
        pass

    # create widgets
    background_3 = Image.open("assets/backgrounds/advanced background.png")
    background_3 = background_3.resize((560, 610), )
    advanced_background = ImageTk.PhotoImage(background_3)

    advanced_background_label = Label(main_win, image=advanced_background)
    advanced_background_label.place(x=-10, y=0)

    if enemy_No <= 5:

        display_enemy_img()

        enemy_hp_label = Label(main_win, text=f" HP: {advanced_enemy_hp} ", font=("ARCADECLASSIC", 22, "bold"),
                               bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        enemy_img_label = Label(main_win, image=enemy_img, borderwidth=3, relief="solid")
        enemy_img_label.place(x=125, y=80)
    else:
        display_boss_img()

        enemy_hp_label = Label(main_win, text=f" HP:  {advanced_boss_hp} ", font=("ARCADECLASSIC", 22, "bold"),
                               bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        boss_img_label = Label(main_win, image=boss_img, borderwidth=3, relief="solid")
        boss_img_label.place(x=125, y=80)

    question_No_label = Label(main_win, text=f" {enemy_No}/6 ", font=("ARCADECLASSIC", 23, "bold"), bg='white',
                              borderwidth=2, relief="solid")
    question_No_label.place(x=480, y=10)

    info_button = Button(main_win, text=" ? ", command=info.show_info_screen, font=("ARCADECLASSIC", 16, "bold"),
                         width=3, fg="green")
    info_button.place(x=480, y=360)

    # get advanced questions
    get_advanced_question()
    # check the player's HP for heart images
    check_player_hp()


# expert questions screen's settings
def expert_difficulty():
    # setting up variables
    global difficulty, expert_enemy_hp, expert_boss_hp, enemy_hp_label
    difficulty = 2
    expert_enemy_hp = 12
    expert_boss_hp = 18

    # clear the main screen
    for widget in main_win.winfo_children():
        widget.destroy()

    # resume the BGM if stopped otherwise move on to the next line
    try:
        pygame.mixer_music.unpause()
    except:
        pass

    # create widgets
    background_4 = Image.open("assets/backgrounds/expert background.png")
    background_4 = background_4.resize((560, 610), )
    expert_background = ImageTk.PhotoImage(background_4)

    expert_background_label = Label(main_win, image=expert_background)
    expert_background_label.place(x=-10, y=0)

    if enemy_No <= 5:
        display_enemy_img()

        enemy_hp_label = Label(main_win, text=f" HP: {expert_enemy_hp} ", font=("ARCADECLASSIC", 22, "bold"),
                               bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        enemy_img_label = Label(main_win, image=enemy_img, borderwidth=3, relief="solid")
        enemy_img_label.place(x=125, y=80)
    else:
        display_boss_img()

        enemy_hp_label = Label(main_win, text=f" HP:  {expert_boss_hp} ", font=("ARCADECLASSIC", 22, "bold"),
                               bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        boss_img_label = Label(main_win, image=boss_img, borderwidth=3, relief="solid")
        boss_img_label.place(x=125, y=80)

    question_No_label = Label(main_win, text=f" {enemy_No}/6 ", font=("ARCADECLASSIC", 23, "bold"), bg='white',
                              borderwidth=2, relief="solid")
    question_No_label.place(x=480, y=10)

    info_button = Button(main_win, text=" ? ", command=info.show_info_screen, font=("ARCADECLASSIC", 16, "bold"),
                         width=3, fg="green")
    info_button.place(x=480, y=360)

    # get expert questions
    get_expert_question()
    # check the player's HP for heart images
    check_player_hp()


# the title screen's settings
def title_screen():
    # Setting up variables
    global player_hp, enemy_No, max_enemy, title_img_label, title_label, username, username_label
    global username_entry, basic_button, advanced_button, expert_button, info_screen
    player_hp = 3
    enemy_No = 0
    max_enemy = 6
    info_screen = None

    # images' settings
    background_1 = Image.open("assets/backgrounds/title background 1.png")
    background_1 = background_1.resize((550, 600), )
    title_background = ImageTk.PhotoImage(background_1)

    # create widgets
    title_background_label = Label(main_win, image=title_background)
    title_background_label.pack()

    username_label = Label(main_win, text=" Username:                               ",
                           font=("ARCADECLASSIC", 22, "bold"),
                           borderwidth=3, relief="sunken")
    username_label.place(x=121, y=375)

    # let username be a string variable
    username = StringVar()
    username_entry = Entry(main_win, textvariable=username, width=10, font=("Arial", 16))
    username_entry.place(x=292, y=380)
    username.trace("w", lambda *args: character_limit(username))

    basic_button = Button(main_win, text="Basic", command=check_username_basic, font=("ARCADECLASSIC", 23, "bold"),
                          width=9, bg="green2", borderwidth=3, relief="raised")
    basic_button.place(x=195, y=430)

    advanced_button = Button(main_win, text="Advanced", command=check_username_advanced,
                             font=("ARCADECLASSIC", 23, "bold"),
                             width=9, bg="yellow", borderwidth=3, relief="raised")
    advanced_button.place(x=100, y=500)

    expert_button = Button(main_win, text="Expert", command=check_username_expert, font=("ARCADECLASSIC", 23, "bold"),
                           width=9, bg="red", borderwidth=3, relief="raised")
    expert_button.place(x=300, y=500)

    main_win.mainloop()


def main():  # the main loop of the program start here
    global main_win

    # main window's setting
    main_win = Tk()
    main_win.geometry('550x600')
    main_win.resizable(width=False, height=False)
    main_win.title('MATH MAGE')
    main_win.protocol('WM_DELETE_WINDOW', terminate)

    # add new font
    pyglet.font.add_file('assets/font/ARCADECLASSIC.TTF')

    # start pygame
    pygame.mixer.init()
    # open title screen
    title_screen()

main()  # start the program

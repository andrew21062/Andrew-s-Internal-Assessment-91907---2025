# Andrew Wong
# Version 5 (Button set 3)
# The purpose of my program is to improve year 11 students’ algebra by making solving questions more fun and engaging.

# Import the libraries needed to run this program.
import pygame
import random
import pyglet
from tkinter import *
from tkinter import messagebox
from tkinter import Toplevel
from PIL import Image, ImageTk

# 'Enemy' is a class that contains all the image location of enemies used for this program.
class Enemy:
    # The list that contains all the image location of all normal enemies.
    enemy_list = [
        {"image": "assets/enemies/enemy1.png"}, {"image": "assets/enemies/enemy2.png"},
        {"image": "assets/enemies/enemy3.png"},
        {"image": "assets/enemies/enemy4.png"}, {"image": "assets/enemies/enemy5.png"},
        {"image": "assets/enemies/enemy6.png"},
        {"image": "assets/enemies/enemy7.png"}, {"image": "assets/enemies/enemy8.png"},
        {"image": "assets/enemies/enemy9.png"},
        {"image": "assets/enemies/enemy10.png"}]

    # The list that contains all the image location of all boss enemies.
    boss_list = [
        {"image": "assets/bosses/boss 1.png"}, {"image": "assets/bosses/boss 2.png"},
        {"image": "assets/bosses/boss 3.png"}, {"image": "assets/bosses/boss 4.png"},
        {"image": "assets/bosses/boss 5.png"}]

    # Turn 'Enemy' into a class.
    def __init__(self, img_location):
        self.img_location = img_location


# Set 'enemy_list' and 'boss_list' as objects of the 'Enemy' class.
list_1 = Enemy("enemy_list")
list_2 = Enemy("boss_list")

# 'InfoScreen' is a class that contains all the attributes of the Info screen.
class InfoScreen:
    # Turn 'InfoScreen' into a class.
    def __init__(self, on_closing_callback):
        self.info_screen = None
        self.on_closing = on_closing_callback
    # A function that has all the attributes of the Info screen.
    def show_info_screen(self):
        # Make sure only one info screen is opened at a time.
        if self.info_screen is None or not Toplevel.winfo_exists(self.info_screen):
            # Info screen's window settings.
            self.info_screen = Toplevel()
            self.info_screen.geometry('450x330')
            self.info_screen.configure(bg='white')
            self.info_screen.resizable(width=False, height=False)
            self.info_screen.title('Info screen')

            # Info screen's widgets
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
        else:
            # Focus on the Info screen
            self.info_screen.focus()


# A function that closes the Info screen
def on_closing():
    info.terminate_info()

# Set 'ifo' as an object of the 'InfoScreen' class.
info = InfoScreen(on_closing)


# Questions list for basic difficultly (with answers).
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

# Questions list for advanced difficultly (with answers).
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

# Questions list for expert difficultly (with answers).
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


# This function shuts down the program and stops the BGM.
def terminate():
    main_win.destroy()
    pygame.mixer_music.stop()


# Battle BGM's settings.
def BGM():
    # Import 'battle BGM' as mp3.
    pygame.mixer.music.load("assets/audio/battle BGM.mp3")
    # Set the volume to 50%.
    pygame.mixer.music.set_volume(0.5)
    # Loop the music 1000 times.
    pygame.mixer.music.play(loops=1000)


# Limit username's characters to 10.
def character_limit(username_entry):
    if len(username_entry.get()) > 0:
        username_entry.set(username_entry.get()[:10])


# A function that jumps to the basic difficulty screen if the username is valid.
def check_username_basic():
    global user

    # Get the username input.
    user = username_entry.get()
    # Remove leading and trailing spaces.
    username_check = username_entry.get().strip()

    # If the entry is not empty after stripping spaces, then play BGM and jump on to the basic question screen.
    if username_check:
        BGM()
        basic_difficulty()
    else:
        # Show error message if username is empty after stripping spaces.
        messagebox.showerror("Error", "Please enter a username.")


# A function that jumps to the advanced difficulty screen if the username is valid.
def check_username_advanced():
    global user

    # Get the username input.
    user = username_entry.get()
    # Remove leading and trailing spaces.
    username_check = username_entry.get().strip()

    # If the entry is not empty after stripping spaces, then play BGM and jump on to the advanced question screen.
    if username_check:
        BGM()
        advanced_difficulty()
    else:
        # Show error message if username is empty after stripping spaces.
        messagebox.showerror("Error", "Please enter a username.")


# A function that jumps to the expert difficulty screen if the username is valid.
def check_username_expert():
    global user

    # Get the username input.
    user = username_entry.get()
    # Remove leading and trailing spaces.
    username_check = username_entry.get().strip()

    # If the entry is not empty after stripping spaces, then play BGM and jump on to the expert question screen.
    if username_check:
        BGM()
        expert_difficulty()
    else:
        # Show error message if username is empty after stripping spaces.
        messagebox.showerror("Error", "Please enter a username.")


# A function that check the difficulty the player chose, then jump to the corresponding question screen.
def check_difficulty():
    # Unpause the BGM.
    pygame.mixer.music.unpause()

    # If difficulty is 0 then jump to basic difficulty screen.
    if difficulty == 0:
        basic_difficulty()
    # If difficulty is 1 then jump to advanced difficulty screen.
    elif difficulty == 1:
        advanced_difficulty()
    # If difficulty is 2 then jump to expert difficulty screen.
    elif difficulty == 2:
        expert_difficulty()


# A function that contains all normal enemies' image settings.
def display_enemy_img():
    global enemy_img

    # Chose a random image from 'enemy_list', then import it.
    current_enemy = random.choice(list_1.enemy_list)
    current_enemy = current_enemy["image"]
    enemy_img = Image.open(current_enemy)
    # Resize the image to 300x300 pixels.
    enemy_img = enemy_img.resize((300, 300))
    # Set the image as the 'enemy_img' variable.
    enemy_img = ImageTk.PhotoImage(enemy_img)


# A function that contains all bosses' image settings.
def display_boss_img():
    global boss_img

    # Chose a random image from 'boss_list', then import it.
    current_boss = random.choice(list_2.boss_list)
    current_boss = current_boss["image"]
    boss_img = Image.open(current_boss)
    # Resize the image to 300x300 pixels.
    boss_img = boss_img.resize((300, 300))
    # Set the image as the 'boss_img' variable.
    boss_img = ImageTk.PhotoImage(boss_img)


# A function that get 3 questions from 'basic_questions'.
def get_basic_question():
    global question_1, answer_button1, question_2, answer_button2, question_3, answer_button3

    # Get a question from 'basic_questions', then set it as the text of question 1.
    question_1 = random.choice(basic_questions)
    answer_button1 = Button(main_win, text=f"\U000026A1 {question_1['question']}", command=question_1_damage,
                            font=("Arial", 22), width=10, bg='deep sky blue')
    answer_button1.place(x=75, y=445)

    # Get a question from 'basic_questions', then set it as the text of question 2.
    question_2 = random.choice(basic_questions)
    answer_button2 = Button(main_win, text=f"\U00002600 {question_2['question']}", command=question_2_damage,
                            font=("Arial", 22), width=10, bg='orange')
    answer_button2.place(x=290, y=445)

    # Get a question from 'basic_questions', then set it as the text of question 3.
    question_3 = random.choice(basic_questions)
    answer_button3 = Button(main_win, text=f"\U0001F319 {question_3['question']}", command=question_3_damage,
                            font=("Arial", 22), width=10, bg='yellow')
    answer_button3.place(x=180, y=520)


# A function that get 3 questions from 'advanced_questions'.
def get_advanced_question():
    global question_1, answer_button1, question_2, answer_button2, question_3, answer_button3

    # Get a question from 'advanced_questions', then set it as the text of question 1.
    question_1 = random.choice(advanced_questions)
    answer_button1 = Button(main_win, text=f"\U000026A1 {question_1['question']}", command=question_1_damage,
                            font=("Arial", 21), width=12, bg='deep sky blue')
    answer_button1.place(x=75, y=445)

    # Get a question from 'advanced_questions', then set it as the text of question 2.
    question_2 = random.choice(advanced_questions)
    answer_button2 = Button(main_win, text=f"\U00002600 {question_2['question']}", command=question_2_damage,
                            font=("Arial", 21), width=12, bg='orange')
    answer_button2.place(x=290, y=445)

    # Get a question from 'advanced_questions', then set it as the text of question 3.
    question_3 = random.choice(advanced_questions)
    answer_button3 = Button(main_win, text=f"\U0001F319 {question_3['question']}", command=question_3_damage,
                            font=("Arial", 21), width=12, bg='yellow')
    answer_button3.place(x=180, y=520)


# A function that get 3 questions from 'expert_questions'.
def get_expert_question():
    global question_1, answer_button1, question_2, answer_button2, question_3, answer_button3
    # Try to get questions from 'expert_questions', if it does not work move on.
    try:
        # Get a question from 'expert_questions', then set it as the text of question 1.
        question_1 = random.choice(expert_questions)
        answer_button1 = Button(main_win, text=f"\U000026A1 {question_1['question']}", command=question_1_damage,
                                font=("Arial", 17), width=20, bg='deep sky blue')
        answer_button1.place(x=5, y=450)

        # Get a question from 'expert_questions', then set it as the text of question 2.
        question_2 = random.choice(expert_questions)
        answer_button2 = Button(main_win, text=f"\U00002600 {question_2['question']}", command=question_2_damage,
                                font=("Arial", 17), width=20, bg='orange')
        answer_button2.place(x=275, y=450)

        # Get a question from 'expert_questions', then set it as the text of question 3.
        question_3 = random.choice(expert_questions)
        answer_button3 = Button(main_win, text=f"\U0001F319 {question_3['question']}", command=question_3_damage,
                                font=("Arial", 17), width=20, bg='yellow')
        answer_button3.place(x=140, y=520)
    except:
        pass


# A function that checks the player's remain HP, then show heart images according to that number.
def check_player_hp():
    global life_img_label_1, life_img_label_2, life_img_label_3, player_hp

    # Try to remove the heart images from pervious questions, if can't then move on.
    try:
        life_img_label_1.destroy()
        life_img_label_2.destroy()
        life_img_label_3.destroy()
    except:
        pass

    # Import the heart image.
    heart_img = Image.open("assets/player HP/heart 1.png")
    # Resize the image to 65x65 pixels.
    heart_img = heart_img.resize((65, 65), )
    life_img = ImageTk.PhotoImage(heart_img)

    # If the player's HP is 3, then put 3 hearts on the window.
    if player_hp == 3:
        life_img_label_1 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_1.place(x=0, y=3)
        life_img_label_2 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_2.place(x=70, y=3)
        life_img_label_3 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_3.place(x=140, y=3)
    # If the player's HP is 2, then put 2 hearts on the window.
    elif player_hp == 2:
        life_img_label_1 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_1.place(x=0, y=3)
        life_img_label_2 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_2.place(x=70, y=3)
    # If the player's HP is 1, then put 1 heart on the window.
    elif player_hp == 1:
        life_img_label_1 = Label(main_win, image=life_img, borderwidth=3, relief="sunken")
        life_img_label_1.place(x=0, y=3)
    # If the player's HP is 0, then put jump to result screen.
    elif player_hp == 0:
        result_screen()

    # Set this as the main loop of the program.
    main_win.mainloop()


# A function that calculates question 1's damage on each difficulty.
def question_1_damage():
    global basic_enemy_hp, advanced_enemy_hp, expert_enemy_hp

    # Calculate the damage if it was a basic difficulty enemy.
    if difficulty == 0:
        basic_enemy_hp = basic_enemy_hp - question_1['answer']
        enemy_hp_label.config(text=f" HP: {basic_enemy_hp} ")
        check_enemy_hp()
    # Calculate the damage if it was an advanced difficulty enemy.
    elif difficulty == 1:
        advanced_enemy_hp = advanced_enemy_hp - question_1['answer']
        enemy_hp_label.config(text=f" HP: {advanced_enemy_hp} ")
        check_enemy_hp()
    # Calculate the damage if it was an expert difficulty enemy.
    elif difficulty == 2:
        expert_enemy_hp = expert_enemy_hp - question_1['answer']
        enemy_hp_label.config(text=f" HP: {expert_enemy_hp} ")
        check_enemy_hp()


# A function that calculates question 2's damage on each difficulty.
def question_2_damage():
    global basic_enemy_hp, advanced_enemy_hp, expert_enemy_hp

    # Calculate the damage if it was a basic difficulty enemy.
    if difficulty == 0:
        basic_enemy_hp = basic_enemy_hp - question_2['answer']
        enemy_hp_label.config(text=f" HP: {basic_enemy_hp} ")
        check_enemy_hp()
    # Calculate the damage if it was an advanced difficulty enemy.
    elif difficulty == 1:
        advanced_enemy_hp = advanced_enemy_hp - question_2['answer']
        enemy_hp_label.config(text=f" HP: {advanced_enemy_hp} ")
        check_enemy_hp()
    # Calculate the damage if it was an expert difficulty enemy.
    elif difficulty == 2:
        expert_enemy_hp = expert_enemy_hp - question_2['answer']
        enemy_hp_label.config(text=f" HP: {expert_enemy_hp} ")
        check_enemy_hp()


# A function that calculates question 3's damage on each difficulty.
def question_3_damage():
    global basic_enemy_hp, advanced_enemy_hp, expert_enemy_hp

    # Calculate the damage if it was a basic difficulty enemy.
    if difficulty == 0:
        basic_enemy_hp = basic_enemy_hp - question_3['answer']
        enemy_hp_label.config(text=f" HP: {basic_enemy_hp} ")
        check_enemy_hp()
    # Calculate the damage if it was an advanced difficulty enemy.
    elif difficulty == 1:
        advanced_enemy_hp = advanced_enemy_hp - question_3['answer']
        enemy_hp_label.config(text=f" HP: {advanced_enemy_hp} ")
        check_enemy_hp()
    # Calculate the damage if it was an expert difficulty enemy.
    elif difficulty == 2:
        expert_enemy_hp = expert_enemy_hp - question_3['answer']
        enemy_hp_label.config(text=f" HP: {expert_enemy_hp} ")
        check_enemy_hp()


# A function that contains the attack gif's settings.
def attack_effect():
    global attack_effect_label

    # A function that sets the attack gif to 70 millisecond per frame.
    def update_frame(frame_index):
        # Try to set the attack gif to 70 millisecond per frame, if it does not work move on.
        try:
            attack_effect_label.config(image=frames[frame_index])
            main_win.after(70, update_frame, (frame_index + 1) % len(frames))
        except:
            pass

    # Import 'attack effect 2.gif' as the variable 'image'.
    image = Image.open("assets/attack gif/attack effect 2.gif")

    # Set 'frames' as a list.
    frames = []
    # Try to convert the gif into a format that can be used in Tkinter, if it does not work move on.
    try:
        # Convert the gif to a format that can be used in Tkinter.
        for frame in range(image.n_frames):
            image.seek(frame)
            frames.append(ImageTk.PhotoImage(image.copy()))

        # Create a label to display the GIF.
        attack_effect_label = Label(main_win)
        attack_effect_label.pack()

        # Start updating the frames.
        update_frame(0)
    except:
        pass


# A function that checks the enemy's HP on each difficulty.
def check_enemy_hp():
    global player_hp, enemy_No

    # For basic difficulty:
    if difficulty == 0:
        # Check if the enemy had been defeated.
        if basic_enemy_hp <= 0:
            # If so reset the player's hp.
            player_hp = 3
            # If so increase the question count.
            enemy_No += 1
            # If the total enemies defeated is over 6, then jump to result screen.
            if enemy_No > 6:
                result_screen()
            # If not over 6 then:
            else:
                # Play attack gif.
                attack_effect()
                # Pause BGM, then play attack sound effect.
                pygame.mixer_music.pause()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/attack sound.mp3"))
                # After 900 millisecond check the player's difficulty to refresh the question screen.
                main_win.after(900, check_difficulty)
        # If the enemy is not dead then:
        else:
            # The player loses one HP.
            player_hp -= 1
            # Get new questions.
            get_basic_question()
            # If the player's HP is 0, then jump to result screen.
            if player_hp <= 0:
                result_screen()
            else:
                # Check the player HP to refresh heart images.
                check_player_hp()

    # For advanced difficulty:
    if difficulty == 1:
        # Check if the enemy had been defeated.
        if advanced_enemy_hp <= 0:
            # If so reset the player's hp.
            player_hp = 3
            # If so increase the question count.
            enemy_No += 1
            # If the total enemies defeated is over 6, then jump to result screen.
            if enemy_No > 6:
                result_screen()
            # If not over 6 then:
            else:
                # Play attack gif.
                attack_effect()
                # Pause BGM, then play attack sound effect.
                pygame.mixer_music.pause()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/attack sound.mp3"))
                # After 900 millisecond check the player's difficulty to refresh the question screen.
                main_win.after(900, check_difficulty)
        # If the enemy is not dead then:
        else:
            # The player loses one HP.
            player_hp -= 1
            # Get new questions.
            get_advanced_question()
            # If the player's HP is 0, then jump to result screen.
            if player_hp <= 0:
                result_screen()
            else:
                # Check the player HP to refresh heart images.
                check_player_hp()

    # For expert difficulty:
    if difficulty == 2:
        # Check if the enemy had been defeated.
        if expert_enemy_hp <= 0:
            # If so reset the player's hp.
            player_hp = 3
            # If so increase the question count.
            enemy_No += 1
            # If the total enemies defeated is over 6, then jump to result screen.
            if enemy_No > 6:
                result_screen()
            # If not over 6 then:
            else:
                # Play attack gif.
                attack_effect()
                # Pause BGM, then play attack sound effect.
                pygame.mixer_music.pause()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/attack sound.mp3"))
                # After 900 millisecond check the player's difficulty to refresh the question screen.
                main_win.after(900, check_difficulty)
        # If the enemy is not dead then:
        else:
            # The player loses one HP.
            player_hp -= 1
            # Get new questions.
            get_expert_question()
            # If the player's HP is 0, then jump to result screen.
            if player_hp <= 0:
                result_screen()
            else:
                # Check the player HP to refresh heart images.
                check_player_hp()

# A function that adds the player's score to a text file.
def add_record():
    # Set the username into another variable.
    username = f"\nUSERNAME: {user} "

    # If difficulty is 0 then set 'Basic' as the 'difficulty_level'.
    if difficulty == 0:
        difficulty_level = "DIFFICULTY: Basic"
    # If difficulty is 0 then set 'Advanced' as the 'difficulty_level'.
    elif difficulty == 1:
        difficulty_level = "DIFFICULTY: Advanced"
    # If difficulty is 0 then set 'Expert' as the 'difficulty_level'.
    elif difficulty == 2:
        difficulty_level = "DIFFICULTY: Expert"

    # If the player had defeated more than 6 enemies, then set 'rank' to 'A' and 'score' to '6/6'.
    if enemy_No > 6:
        rank = "RANK: A"
        score = "SCORE: 6/6"
    # If the player had defeated exactly 6 enemies, then set 'rank' to 'A' and 'score' to '6/6'.
    elif enemy_No == 6:
        rank = "RANK: A"
        score = "SCORE: 6/6"
    # If the player had defeated exactly 2 or less enemies, then set 'rank' to 'F' and 'score' to the amount of enemies they defeated.
    elif enemy_No <= 2:
        rank = "RANK: F"
        score = f"SCORE: {enemy_No}/6"
    # If the player had defeated exactly 4 or more enemies, then set 'rank' to 'B' and 'score' to the amount of enemies they defeated.
    elif enemy_No >= 4:
        rank = "RANK: B"
        score = f"SCORE: {enemy_No}/6"
    # If the player had defeated less than 4 enemies, then set 'rank' to 'C' and 'score' to the amount of enemies they defeated.
    elif enemy_No < 4:
        rank = "RANK: C"
        score = f"SCORE: {enemy_No}/6"

    # Append 'username', 'difficulty_level', 'rank' and 'score' to the 'Players_score.txt' text file.
    with open("Players_score.txt", "a") as file:
        file.write(f"{username}, {difficulty_level}, {rank}, {score}\n")


# A function that restart the whole program.
def restart():
    # Delete all widgets on the main screen.
    for widget in main_win.winfo_children():
        widget.destroy()
    # Restart the program.
    main_win.title('MATH MAGE')
    title_screen()


# A function that contains the result screen's settings.
def result_screen():
    # Try to clear the main screen, if it does not work move on,
    try:
        # Delete all widgets on the main screen.
        for widget in main_win.winfo_children():
            widget.destroy()
    except:
        pass

    # Stop the BGM.
    pygame.mixer_music.stop()

    # Add record to the score board.
    add_record()

    # Change the window's title.
    main_win.title('Result')

    # Result screen's widgets.
    background_5 = Image.open("assets/backgrounds/result background.png")
    background_5 = background_5.resize((560, 610), )
    result_background = ImageTk.PhotoImage(background_5)

    result_background_label = Label(main_win, image=result_background)
    result_background_label.place(x=-10, y=0)

    text_1_label = Label(main_win, text=f"  {user} got: ", font=("ARCADECLASSIC", 30, "bold"))
    text_1_label.pack(pady=10)

    # If the more than 6 enemies had been defeated then:
    if enemy_No > 6:
        # Play victory music.
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/win sound.mp3"))
        # Show grade A and score.
        result_label = Label(main_win, text="   A   ", font=("ARCADECLASSIC", 125, "bold"), fg="green2")
        result_label.pack()
        score_label = Label(main_win, text=" Score: 6/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()
    # If the exactly 6 enemies had been defeated then:
    elif enemy_No == 6:
        # Play victory music.
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/win sound.mp3"))
        # Show grade A and score.
        result_label = Label(main_win, text="   A   ", font=("ARCADECLASSIC", 125, "bold"), fg="green2")
        result_label.pack()
        score_label = Label(main_win, text=" Score: 6/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()
    # If less than or equal to 2 enemies had been defeated then:
    elif enemy_No <= 2:
        # Play game over music.
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/game over sound.mp3"))
        # Show grade F and score.
        result_label = Label(main_win, text="   F   ", font=("ARCADECLASSIC", 125, "bold"), fg="red4")
        result_label.pack()
        score_label = Label(main_win, text=f" Score: {enemy_No}/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()
    # If more than or equal to 4 enemies had been defeated then:
    elif enemy_No >= 4:
        # Play victory music.
        pygame.mixer_music.stop()
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/win sound.mp3"))
        # Show grade B and score.
        result_label = Label(main_win, text="   B   ", font=("ARCADECLASSIC", 125, "bold"), fg="orange")
        result_label.pack()
        score_label = Label(main_win, text=f" Score: {enemy_No}/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()
    # If less than 4 enemies defeated then:
    elif enemy_No < 4:
        # Play game over music.
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/game over sound.mp3"))
        # Show grade C and score.
        result_label = Label(main_win, text="   C   ", font=("ARCADECLASSIC", 125, "bold"), fg="red")
        result_label.pack()
        score_label = Label(main_win, text=f" Score: {enemy_No}/6 ", font=("ARCADECLASSIC", 30, "bold"))
        score_label.pack()

    difficulty_label = Label(main_win, text=f"Difficulty:", font=("ARCADECLASSIC", 27, "bold"))
    difficulty_label.pack(pady=10)
    # Check the difficulty the player was on, then show it as a label.
    # Show basic difficulty.
    if difficulty == 0:
        level_label = Label(main_win, text=f"    Basic    ", font=("ARCADECLASSIC", 30, "bold"), fg="green2")
        level_label.pack()
    # Show advanced difficulty.
    if difficulty == 1:
        level_label = Label(main_win, text=f"   Advanced  ", font=("ARCADECLASSIC", 30, "bold"), fg="orange")
        level_label.pack()
    # Show expert difficulty.
    if difficulty == 2:
        level_label = Label(main_win, text=f"    Expert   ", font=("ARCADECLASSIC", 30, "bold"), fg="red")
        level_label.pack()

    # Again button's settings.
    again_button = Button(main_win, text="\u2764 Again", command=restart, font=("Helvetica", 23, "bold"), bg="white",
                          width=9, borderwidth=3, relief="raised")
    again_button.place(x=80, y=490)
    # End button's settings.
    end_button = Button(main_win, text="\U0001F480 End", command=main_win.destroy, font=("Helvetica", 23, "bold"),
                        bg="white",
                        width=9, borderwidth=3, relief="raised")
    end_button.place(x=295, y=490)

    # Let this function be the main loop of the program.
    main_win.mainloop()


# A function that contains the basic questions screen's settings.
def basic_difficulty():
    # Set up variables.
    global difficulty, basic_enemy_hp, basic_boss_hp, enemy_hp_label
    difficulty = 0
    basic_enemy_hp = 10
    basic_boss_hp = 15

    # Delete all widgets on the main screen
    for widget in main_win.winfo_children():
        widget.destroy()

    # Try to resume the BGM, if it does not work move on.
    try:
        pygame.mixer_music.unpause()
    except:
        pass

    # Create widgets.
    background_2 = Image.open("assets/backgrounds/basic background.png")
    background_2 = background_2.resize((560, 610), )
    basic_background = ImageTk.PhotoImage(background_2)

    basic_background_label = Label(main_win, image=basic_background)
    basic_background_label.place(x=-10, y=0)

    # If the player had defeated 5 or fewer enemies, then display widgets with normal enemy settings.
    if enemy_No <= 5:
        # Get new enemy image.
        display_enemy_img()

        enemy_hp_label = Label(main_win, text=f" HP: {basic_enemy_hp} ", font=("ARCADECLASSIC", 22, "bold"), bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        enemy_img_label = Label(main_win, image=enemy_img, borderwidth=3, relief="solid")
        enemy_img_label.place(x=125, y=80)
    # If the players had defeated more than 5 enemies, then display widgets with boss enemy settings.
    else:
        # Get new boss image.
        display_boss_img()

        enemy_hp_label = Label(main_win, text=f" HP:  {basic_boss_hp} ", font=("ARCADECLASSIC", 22, "bold"), bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        boss_img_label = Label(main_win, image=boss_img, borderwidth=3, relief="solid")
        boss_img_label.place(x=125, y=80)

    # Show question number and info button.
    question_No_label = Label(main_win, text=f" {enemy_No}/6 ", font=("ARCADECLASSIC", 23, "bold"), bg='white',
                              borderwidth=2, relief="solid")
    question_No_label.place(x=480, y=10)

    info_button = Button(main_win, text=" ? ", command=info.show_info_screen, font=("ARCADECLASSIC", 20, "bold"),
                         width=3, fg="green")
    info_button.place(x=480, y=360)

    # Get basic questions.
    get_basic_question()
    # Check the player's HP for heart images.
    check_player_hp()


# A function that contains the advance questions screen's settings.
def advanced_difficulty():
    # Set up variables.
    global difficulty, advanced_enemy_hp, advanced_boss_hp, enemy_hp_label
    difficulty = 1
    advanced_enemy_hp = 10
    advanced_boss_hp = 15

    # Delete all widgets on the main screen
    for widget in main_win.winfo_children():
        widget.destroy()

    # Try to resume the BGM, if it does not work move on.
    try:
        pygame.mixer_music.unpause()
    except:
        pass

    # Create widgets.
    background_3 = Image.open("assets/backgrounds/advanced background.png")
    background_3 = background_3.resize((560, 610), )
    advanced_background = ImageTk.PhotoImage(background_3)

    advanced_background_label = Label(main_win, image=advanced_background)
    advanced_background_label.place(x=-10, y=0)

    # If the player had defeated 5 or fewer enemies, then display widgets with normal enemy settings.
    if enemy_No <= 5:
        # Get new enemy image.
        display_enemy_img()

        enemy_hp_label = Label(main_win, text=f" HP: {advanced_enemy_hp} ", font=("ARCADECLASSIC", 22, "bold"),
                               bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        enemy_img_label = Label(main_win, image=enemy_img, borderwidth=3, relief="solid")
        enemy_img_label.place(x=125, y=80)
    # If the players had defeated more than 5 enemies, then display widgets with boss enemy settings.
    else:
        # Get new boss image.
        display_boss_img()

        enemy_hp_label = Label(main_win, text=f" HP:  {advanced_boss_hp} ", font=("ARCADECLASSIC", 22, "bold"),
                               bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        boss_img_label = Label(main_win, image=boss_img, borderwidth=3, relief="solid")
        boss_img_label.place(x=125, y=80)

    # Show question number and info button.
    question_No_label = Label(main_win, text=f" {enemy_No}/6 ", font=("ARCADECLASSIC", 23, "bold"), bg='white',
                              borderwidth=2, relief="solid")
    question_No_label.place(x=480, y=10)

    info_button = Button(main_win, text=" ? ", command=info.show_info_screen, font=("ARCADECLASSIC", 16, "bold"),
                         width=3, fg="green")
    info_button.place(x=480, y=360)

    # Get advanced questions.
    get_advanced_question()
    # Check the player's HP for heart images.
    check_player_hp()


# A function that contains the expert questions screen's settings.
def expert_difficulty():
    # Set up variables.
    global difficulty, expert_enemy_hp, expert_boss_hp, enemy_hp_label
    difficulty = 2
    expert_enemy_hp = 12
    expert_boss_hp = 18

    # Delete all widgets on the main screen
    for widget in main_win.winfo_children():
        widget.destroy()

    # Try to resume the BGM, if it does not work move on.
    try:
        pygame.mixer_music.unpause()
    except:
        pass

    # Create widgets.
    background_4 = Image.open("assets/backgrounds/expert background.png")
    background_4 = background_4.resize((560, 610), )
    expert_background = ImageTk.PhotoImage(background_4)

    expert_background_label = Label(main_win, image=expert_background)
    expert_background_label.place(x=-10, y=0)

    # If the player had defeated 5 or fewer enemies, then display widgets with normal enemy settings.
    if enemy_No <= 5:
        # Get new enemy image.
        display_enemy_img()

        enemy_hp_label = Label(main_win, text=f" HP: {expert_enemy_hp} ", font=("ARCADECLASSIC", 22, "bold"),
                               bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        enemy_img_label = Label(main_win, image=enemy_img, borderwidth=3, relief="solid")
        enemy_img_label.place(x=125, y=80)
    # If the players had defeated more than 5 enemies, then display widgets with boss enemy settings.
    else:
        # Get new boss image.
        display_boss_img()

        enemy_hp_label = Label(main_win, text=f" HP:  {expert_boss_hp} ", font=("ARCADECLASSIC", 22, "bold"),
                               bg='white',
                               borderwidth=1, relief="solid")
        enemy_hp_label.place(x=220, y=395)

        boss_img_label = Label(main_win, image=boss_img, borderwidth=3, relief="solid")
        boss_img_label.place(x=125, y=80)

    # Show question number and info button.
    question_No_label = Label(main_win, text=f" {enemy_No}/6 ", font=("ARCADECLASSIC", 23, "bold"), bg='white',
                              borderwidth=2, relief="solid")
    question_No_label.place(x=480, y=10)

    info_button = Button(main_win, text=" ? ", command=info.show_info_screen, font=("ARCADECLASSIC", 16, "bold"),
                         width=3, fg="green")
    info_button.place(x=480, y=360)

    # Get expert questions.
    get_expert_question()
    # Check the player's HP for heart images.
    check_player_hp()


# A function that contains the title screen's settings.
def title_screen():
    # Set up variables.
    global player_hp, enemy_No, max_enemy, title_img_label, title_label, username, username_label
    global username_entry, basic_button, advanced_button, expert_button, info_screen, mute_value
    player_hp = 3
    enemy_No = 0
    max_enemy = 6
    info_screen = None

    # Images' settings.
    background_1 = Image.open("assets/backgrounds/title background 1.png")
    background_1 = background_1.resize((550, 600), )
    title_background = ImageTk.PhotoImage(background_1)

    basic_img = Image.open("assets/buttons/basic button 3.png")
    basic_img = basic_img.resize((150, 70))
    basic_button_img = ImageTk.PhotoImage(basic_img)

    advance_img = Image.open("assets/buttons/advance button 3.png")
    advance_img = advance_img.resize((150, 70))
    advance_button_img = ImageTk.PhotoImage(advance_img)

    expert_img = Image.open("assets/buttons/expert button 3.png")
    expert_img = expert_img.resize((150, 70))
    expert_button_img = ImageTk.PhotoImage(expert_img)

    # Create widgets.
    title_background_label = Label(main_win, image=title_background)
    title_background_label.pack()

    username_label = Label(main_win, text=" Username:                               ",
                           font=("ARCADECLASSIC", 22, "bold"),
                           borderwidth=3, relief="sunken")
    username_label.place(x=121, y=375)

    # Let 'username' be a string variable.
    username = StringVar()
    username_entry = Entry(main_win, textvariable=username, width=10, font=("Arial", 16))
    username_entry.place(x=292, y=380)
    username.trace("w", lambda *args: character_limit(username))

    basic_button = Button(main_win, image=basic_button_img, command=check_username_basic, bg="green2", borderwidth=3, relief="raised")
    basic_button.place(x=205, y=425)

    advanced_button = Button(main_win, image=advance_button_img, command=check_username_advanced, bg="yellow", borderwidth=3, relief="raised")
    advanced_button.place(x=100, y=508)

    expert_button = Button(main_win, image=expert_button_img, command=check_username_expert, bg="red", borderwidth=3, relief="raised")
    expert_button.place(x=300, y=508)

    main_win.mainloop()


 # The function that is the main loop of the program.
def main():
    global main_win

    # Main window's setting.
    main_win = Tk()
    main_win.geometry('550x600')
    main_win.resizable(width=False, height=False)
    main_win.title('MATH MAGE')
    main_win.protocol('WM_DELETE_WINDOW', terminate)

    # Set up the main window's icon.
    icon_img =PhotoImage(file="assets/program icon/icon image.png")
    main_win.iconphoto(True, icon_img)

    # Add new font.
    pyglet.font.add_file('assets/font/ARCADECLASSIC.TTF')

    # Start pygame.
    pygame.mixer.init()
    # Open title screen.
    title_screen()

 # Start the program.
main()

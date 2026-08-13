import pygame
import json
import os
import numpy as np

# Load save data
if os.path.exists("game_savedata.json"):
    with open("game_savedata.json", "r") as file:
        data = json.load(file)
else:
    data = {"first_time": True, "name": ""}
    with open("game_savedata.json", "w") as file:
        json.dump(data, file, indent=4)

# Check if this is the player's first time
if data.get("first_time", True):
    print("FIRST TIME!")
    screen_stage = "1"
else:
    screen_stage = "0"

pygame.init()
pygame.mixer.init()

def make_higher(sound, amount=1.5):
    sound_array = pygame.sndarray.array(sound)
    new_length = int(len(sound_array) / amount)
    new_indices = np.linspace(0, len(sound_array) - 1, new_length)
    new_sound_array = np.zeros((new_length, sound_array.shape[1]), dtype=sound_array.dtype)
    for channel in range(sound_array.shape[1]):
        new_sound_array[:, channel] = np.interp(new_indices, np.arange(len(sound_array)), sound_array[:, channel])
    return pygame.sndarray.make_sound(new_sound_array.astype(sound_array.dtype))

def make_lower(sound, amount=1.5):
    sound_array = pygame.sndarray.array(sound)
    new_length = int(len(sound_array) * amount)
    new_indices = np.linspace(0, len(sound_array) - 1, new_length)
    new_sound_array = np.zeros((new_length, sound_array.shape[1]), dtype=sound_array.dtype)
    for channel in range(sound_array.shape[1]):
        new_sound_array[:, channel] = np.interp(new_indices, np.arange(len(sound_array)), sound_array[:, channel])
    return pygame.sndarray.make_sound(new_sound_array.astype(sound_array.dtype))

menu_select_sound = pygame.mixer.Sound("Sounds/freesound_community-menu-selection-102220.mp3")
higher_menu_sound = make_higher(menu_select_sound)
lower_menu_sound = make_lower(menu_select_sound)

muted = False

def play_sound(sound):
    if not muted:
        sound.play()

def update_mute():
    if muted:
        menu_select_sound.set_volume(0)
        higher_menu_sound.set_volume(0)
        lower_menu_sound.set_volume(0)
    else:
        menu_select_sound.set_volume(1)
        higher_menu_sound.set_volume(1)
        lower_menu_sound.set_volume(1)

def K_ent_sound():
    play_sound(menu_select_sound)
    play_sound(higher_menu_sound)

def K_bks_sound():
    play_sound(menu_select_sound)
    play_sound(lower_menu_sound)

screen = pygame.display.set_mode((1600, 1200))
pygame.display.set_caption("KnightSim")

big_font = pygame.font.SysFont("consolas", 75)
normal_font = pygame.font.SysFont("consolas", 50)
small_font = pygame.font.SysFont("consolas", 35)
xsmall_font = pygame.font.SysFont("consolas", 15)

# Setup prompt keys
txtA_promptkey = small_font.render("A ", True, "purple")
txtB_promptkey = small_font.render("B ", True, "purple")
txtC_promptkey = small_font.render("C ", True, "purple")
txtD_promptkey = small_font.render("D ", True, "purple")
txtE_promptkey = small_font.render("E ", True, "purple")
txtF_promptkey = small_font.render("F ", True, "purple")
txtG_promptkey = small_font.render("G ", True, "purple")
txtH_promptkey = small_font.render("H ", True, "purple")
txtI_promptkey = small_font.render("I ", True, "purple")
txtJ_promptkey = small_font.render("J ", True, "purple")
txtK_promptkey = small_font.render("K ", True, "purple")
txtL_promptkey = small_font.render("L ", True, "purple")
txtM_promptkey = small_font.render("M ", True, "purple")
txtN_promptkey = small_font.render("N ", True, "purple")
txtO_promptkey = small_font.render("O ", True, "purple")
txtP_promptkey = small_font.render("P ", True, "purple")
txtQ_promptkey = small_font.render("Q ", True, "purple")
txtR_promptkey = small_font.render("R ", True, "purple")
txtS_promptkey = small_font.render("S ", True, "purple")
txtT_promptkey = small_font.render("T ", True, "purple")
txtU_promptkey = small_font.render("U ", True, "purple")
txtV_promptkey = small_font.render("V ", True, "purple")
txtW_promptkey = small_font.render("W ", True, "purple")
txtX_promptkey = small_font.render("X ", True, "purple")
txtY_promptkey = small_font.render("Y ", True, "purple")
txtZ_promptkey = small_font.render("Z ", True, "purple")
txt1_promptkey = small_font.render("1 ", True, "purple")
txt2_promptkey = small_font.render("2 ", True, "purple")
txt3_promptkey = small_font.render("3 ", True, "purple")
txt4_promptkey = small_font.render("4 ", True, "purple")
txt5_promptkey = small_font.render("5 ", True, "purple")
txt6_promptkey = small_font.render("6 ", True, "purple")
txt7_promptkey = small_font.render("7 ", True, "purple")
txt8_promptkey = small_font.render("8 ", True, "purple")
txt9_promptkey = small_font.render("9 ", True, "purple")
txt0_promptkey = small_font.render("0 ", True, "purple")
# variable setup
name = data.get("name", "")
cursor_visible = True
selected_option = 0
previous_screen_stage = "0"
running = True
# Progress bar meth 1+1 = 3
progress = 40
completed = progress // 20
remaining = 20 - completed

while running:
    can_pause = screen_stage not in ["0", "1", "1001"] and not screen_stage.startswith("9")
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            play_sound(menu_select_sound)
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_DELETE and can_pause:
                previous_screen_stage = screen_stage
                screen_stage = "00"
                selected_option = 0

            # S0 Main menu
            elif screen_stage == "0":
                if event.key == pygame.K_UP:
                    selected_option -= 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_DOWN:
                    selected_option += 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_RETURN:
                    K_ent_sound()
                    if selected_option == 0:
                        screen_stage = "2"
                    elif selected_option == 1:
                        screen_stage = "901"
                    elif selected_option == 2:
                        screen_stage = "902"
                        selected_option = 0
                    elif selected_option == 3:
                        running = False

                if selected_option < 0:
                    selected_option = 3
                elif selected_option > 3:
                    selected_option = 0

            # S00 Pause menu
            elif screen_stage == "00":
                if event.key == pygame.K_UP:
                    selected_option -= 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_DOWN:
                    selected_option += 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_RETURN:
                    K_ent_sound()
                    if selected_option == 0:
                        screen_stage == previous_screen_stage
                    elif selected_option == 1:
                        screen_stage = "0"
                    elif selected_option == 2:
                        running = False
                
                    if selected_option < 0:
                        selected_option = 2
                    elif selected_option > 2:
                        selected_option = 0

            # S901 Credits
            elif screen_stage == "901":
                if event.key == pygame.K_BACKSPACE:
                    K_bks_sound()
                    selected_option = 1
                    screen_stage = "0"

            # S902 Settings
            elif screen_stage == "902":
                if event.key == pygame.K_UP:
                    selected_option -= 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_DOWN:
                    selected_option += 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_BACKSPACE:
                    K_bks_sound()
                    selected_option = 2
                    screen_stage = "0"
                elif event.key == pygame.K_RETURN:
                    K_ent_sound()
                    if selected_option == 0:
                        play_sound(higher_menu_sound)
                        print("undefined")
                    elif selected_option == 1:
                        play_sound(higher_menu_sound)
                        selected_option = 0
                        screen_stage = "9022"
                    elif selected_option == 2:
                        play_sound(higher_menu_sound)
                        print("undefined")
                    elif selected_option == 3:
                        play_sound(higher_menu_sound)
                        screen_stage = "9021"
                    elif selected_option == 4:
                        play_sound(higher_menu_sound)
                        selected_option = 0
                        screen_stage = "9025"

                if selected_option < 0:
                    selected_option = 4
                elif selected_option > 4:
                    selected_option = 0

            # S9022 Audio Settings
            elif screen_stage == "9022":
                if event.key == pygame.K_UP:
                    selected_option -= 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_DOWN:
                    selected_option += 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_BACKSPACE:
                    K_bks_sound()
                    selected_option = 1
                    screen_stage = "902"
                elif event.key == pygame.K_RETURN:
                    K_ent_sound()
                    if selected_option == 0:
                        muted = not muted
                        update_mute()
                    elif selected_option == 1:
                        play_sound(lower_menu_sound)
                        selected_option = 1
                        screen_stage = "902"

                if selected_option < 0:
                    selected_option = 1
                elif selected_option > 1:
                    selected_option = 0

            # S9021 Advanced settings
            elif screen_stage == "9021":
                if event.key == pygame.K_BACKSPACE:
                    K_bks_sound()
                    selected_option = 3
                    screen_stage = "902"

            # S9025 Wipe Save Warning
            elif screen_stage == "9025":
                if event.key == pygame.K_UP:
                    selected_option -= 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_DOWN:
                    selected_option += 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_BACKSPACE:
                    K_bks_sound()
                    selected_option = 4
                    screen_stage = "902"
                elif event.key == pygame.K_RETURN:
                    K_ent_sound()
                    if selected_option == 0:
                        selected_option = 4
                        screen_stage = "902"
                    elif selected_option == 1:
                        selected_option = 0
                        screen_stage = "90252"

                if selected_option < 0:
                    selected_option = 1
                elif selected_option > 1:
                    selected_option = 0

            # S90252 Wipe Save Warning 2
            elif screen_stage == "90252":
                if event.key == pygame.K_UP:
                    selected_option -= 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_DOWN:
                    selected_option += 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_BACKSPACE:
                    K_bks_sound()
                    selected_option = 4
                    screen_stage = "902"
                elif event.key == pygame.K_RETURN:
                    K_ent_sound()
                    if selected_option == 0:
                        selected_option = 4
                        screen_stage = "902"
                    elif selected_option == 1:
                        data = {"first_time": True, "name": ""}
                        with open("game_savedata.json", "w") as file:
                            json.dump(data, file, indent=4)
                        name = ""
                        selected_option = 0
                        screen_stage = "1"

                if selected_option < 0:
                    selected_option = 1
                elif selected_option > 1:
                    selected_option = 0

            # S1 Name screen
            elif screen_stage == "1":
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    for _ in range(2):
                        play_sound(menu_select_sound)
                elif event.key == pygame.K_RETURN:
                    K_ent_sound()
                    data["first_time"] = False
                    data["name"] = name
                    with open("game_savedata.json", "w") as file:
                        json.dump(data, file, indent=4)
                    screen_stage = "1001"
                elif event.key == pygame.K_BACKSPACE:
                    K_bks_sound()
                    name = name[:-1]
                else:
                    if event.unicode.isprintable():
                        play_sound(menu_select_sound)
                        name += event.unicode

            # S1001 First time ctrls screen
            elif screen_stage == "1001":
                if event.key == pygame.K_RETURN:
                    screen_stage = "0"

            # S2 Choice screen
            elif screen_stage == "2":
                if event.key == pygame.K_UP:
                    selected_option -= 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_DOWN:
                    selected_option += 1
                    play_sound(menu_select_sound)
                elif event.key == pygame.K_RETURN:
                    K_ent_sound()
                    if selected_option == 0:
                        screen_stage = "3"
                    elif selected_option == 1:
                        screen_stage = "4"
                elif event.key == pygame.K_HOME:
                    screen_stage = "0"

                if selected_option < 0:
                    selected_option = 1
                elif selected_option > 1:
                    selected_option = 0

            # S3 Explore
            elif screen_stage == "3":
                if event.key == pygame.K_BACKSPACE:
                    K_bks_sound()
                    screen_stage = "2"

            # S4 Train
            elif screen_stage == "4":
                if event.key == pygame.K_BACKSPACE:
                    K_bks_sound()
                    screen_stage = "2"

    screen.fill("black")

    # S0 title screen
    if screen_stage == "0":
        title1 = xsmall_font.render("██╗  ██╗███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗    ", True, "white")
        title2 = xsmall_font.render("██║ ██╔╝████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝   ", True, "white")
        title3 = xsmall_font.render("█████╔╝ ██╔██╗ ██║██║██║  ███╗███████║   ██║      ", True, "white")
        title4 = xsmall_font.render("██╔═██╗ ██║╚██╗██║██║██║   ██║██╔══██║   ██║       ", True, "white")
        title5 = xsmall_font.render("██║  ██╗██║ ╚████║██║╚██████╔╝██║  ██║   ██║       ", True, "white")
        title6 = xsmall_font.render("╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ", True, "white")
        title7 = xsmall_font.render("██████╗ ██╗   ██╗████████╗███████╗ ", True, "white")
        title8 = xsmall_font.render("██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝ ", True, "white")
        title9 = xsmall_font.render("██████╔╝ ╚████╔╝    ██║   █████╗  ", True, "white")
        title10 = xsmall_font.render("██╔══██╗  ╚██╔╝     ██║   ██╔══╝  ", True, "white")
        title11 = xsmall_font.render("██████╔╝   ██║      ██║   ███████╗", True, "white")
        title12 = xsmall_font.render("╚═════╝    ╚═╝      ╚═╝   ╚══════╝", True, "white")
        title13 = small_font.render("//By IntelI9 and K_muistaa501", True, "white")
        title14 = small_font.render("//Made for Project Stardance 2026", True, "white")
        title15 = normal_font.render("Press Esc to quit at any time", True, "purple")
        title16 = small_font.render("Welcome, Knight " + name + "!", True, "white")
        progress_bar = "[" + "".join(["|█"] * completed + ["|#"] * remaining) + "]"
        progress_text = small_font.render(progress_bar, True, "dark green")
        progress_per100 = normal_font.render(f"{completed * 20}% completed [Chapter: " + screen_stage + "]", True, "white")

        screen.blit(title1, (100, 300))
        screen.blit(title2, (100, 310))
        screen.blit(title3, (100, 320))
        screen.blit(title4, (100, 330))
        screen.blit(title5, (100, 340))
        screen.blit(title6, (100, 350))
        screen.blit(title7, (100, 400))
        screen.blit(title8, (100, 410))
        screen.blit(title9, (100, 420))
        screen.blit(title10, (100, 430))
        screen.blit(title11, (100, 440))
        screen.blit(title12, (100, 450))
        screen.blit(title13, (100, 500))
        screen.blit(title14, (100, 540))
        screen.blit(title15, (100, 950))
        if data["first_time"] == False:
           screen.blit(title16, (100, 600)) 
        screen.blit(progress_text, (100, 650))
        screen.blit(progress_per100, (100, 700))

        options = ["[Start]", "[Credits]", "[Settings]", "[Quit]"]

        for i, option in enumerate(options):
            prefix = "> " if i == selected_option else "  "
            if option == "[Quit]":
                colour = "red"
            elif i == selected_option:
                colour = "green"
            else:
                colour = "white"

            text = small_font.render(prefix + option, True, colour)
            screen.blit(text, (900, 600 + i * 60))

    # S00 Pause menu
    elif screen_stage == "00":
        options = ["[Back]","[To Start Menu]" "[Quit]"]
        for i, option in enumerate(options):
                   prefix = "> " if i == selected_option else "  "
                   if option == "[Quit]":
                       colour = "red"
                   elif i == selected_option:
                       colour = "green"
                   else:
                       colour = "white"
       
                   text = small_font.render(prefix + option, True, colour)
                   screen.blit(text, (900, 600 + i * 60))

    # S1 Name screen
    elif screen_stage == "1":
        prompt = small_font.render("Type your knight's name:", True, "white")
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            cursor = "^"
        elif pygame.time.get_ticks() % 500 < 250:
            cursor = "|"
        else:
            cursor = ""

        name_text = normal_font.render(name + cursor, True, "Green")
        screen.blit(prompt, (220, 330))
        screen.blit(name_text, (220, 380))

        press_text1 = small_font.render("Press ", True, "white")
        enter_text1 = small_font.render("ENTER", True, "purple")
        continue_text1 = small_font.render(" to continue", True, "white")

        screen.blit(press_text1, (210, 440))
        screen.blit(enter_text1, (210 + press_text1.get_width(), 440))
        screen.blit(continue_text1, (210 + press_text1.get_width() + enter_text1.get_width(), 440))

    # S2 Choice screen
    elif screen_stage == "2":
        welcome = normal_font.render("Welcome, Knight " + name + "!", True, "white")
        screen.blit(welcome, (220, 300))

        options = ["[Explore]", "[Train]"]

        for i, option in enumerate(options):
            prefix = "> " if i == selected_option else "  "
            colour = "green" if i == selected_option else "white"
            text = small_font.render(prefix + option, True, colour)
            screen.blit(text, (900, 600 + i * 60))

    # S3 Explore
    elif screen_stage == "3":
        # Game scene
            explore_text = small_font.render(
            "Welcome to the """"peaceful """" village of Chimmand.",True,"white")
            screen.blit(explore_text, (200, 400))

        # Dialogue box
            pygame.draw.rect(screen, "black", (100, 850, 1400, 250))
            pygame.draw.rect(screen, "#3FA879", (100, 850, 1400, 250), 4)

        # Character name
            speaker = small_font.render("Knight", True, "#3FA879")
            screen.blit(speaker, (140, 875))

    # Dialogue
            dialogue = small_font.render("Hmm... something feels strange about this village.", True,"white")
            screen.blit(dialogue, (140, 930))

    # Continue prompt
            continue_text = xsmall_font.render("Press ENTER to continue",True,"purple")
            screen.blit(continue_text, (1150, 1050))

    # S4 Train
    elif screen_stage == "4":
        train_text = small_font.render("At " + name + "'s house", True, "white")
        back_text = small_font.render("Press BACKSPACE to go back", True, "purple")
        screen.blit(train_text, (200, 400))
        screen.blit(back_text, (200, 500))

    #S1001 First time ctrls screen
    elif screen_stage == "1001":
        ctrls_text1 = normal_font.render("Use [UP] and [DOWN] arrows to navigate menus", True, "purple")
        ctrls_text2 = normal_font.render("[Enter] (Return) to select", True, "white")
        ctrls_text3 = normal_font.render("[Backspace] to go back", True, "purple")
        ctrls_text4 = normal_font.render("Enjoy the game!",True, "blue")
        screen.blit(ctrls_text1, ctrls_text1.get_rect(midleft=(300, 350)))
        screen.blit(ctrls_text2, ctrls_text2.get_rect(midleft=(450, 450)))
        screen.blit(ctrls_text3, ctrls_text3.get_rect(midleft=(450, 550)))
        screen.blit(ctrls_text4, ctrls_text4.get_rect(midleft=(450, 650)))

    # S901 Credits
    elif screen_stage == "901":
        credits_text1 = normal_font.render("//KnightByte by K_muistaa501 & IntelI9 (C) 2026",True, "#00E5FF")
        credits_text2 = small_font.render("//Ascii by patryojk on",True, "purple")
        credits_text3 = xsmall_font.render("https://patorjk.com/software/taag/#p=display&f=Graffiti&t=&x=none&v=4&h=4&w=80&we=false", True, "Green")
        credits_text4 = small_font.render("//This code was partially generated by ChatGPT: code goblin & debug wiz",True, "purple")
        credits_text5 = small_font.render("Thanks Hack Club!!! We wouldn't code if it weren't for you",True, "blue")
        back_text = small_font.render("Press BACKSPACE to go back", True, "purple")
        screen.blit(credits_text1, (100, 200))
        screen.blit(credits_text2, (100, 250))
        screen.blit(credits_text3, (100, 300))
        screen.blit(credits_text4, (100, 350))
        screen.blit(credits_text5, (100, 400))
        screen.blit(back_text, (200, 1000))

    # S902 Settings
    elif screen_stage == "902":
        options_text1 = small_font.render("Settings", True, "white")
        back_text = small_font.render("Press BACKSPACE to go back", True, "purple")
        options = [
            "[General]",
            "[Audio]",
            "[Video]",
            "[Advanced FOR NERDS ONLY]",
            "{!WIPE SAVE!}"
        ]

        screen.blit(options_text1, (200, 400))
        screen.blit(back_text, (200, 450))

        for i, option in enumerate(options):
            prefix = "> " if i == selected_option else "  "

            if option == "{!WIPE SAVE!}":
                colour = "red"
            elif i == selected_option:
                colour = "green"
            else:
                colour = "white"

            text = small_font.render(prefix + option, True, colour)
            screen.blit(text, (900, 600 + i * 60))

    # S9022 Audio Settings
    elif screen_stage == "9022":
        audio_title = small_font.render("Audio Settings", True, "white")
        mute_status = "ON" if muted else "OFF"

        options = [
            "[Mute: " + mute_status + "]",
            "[Back]"
        ]

        for i, option in enumerate(options):
            prefix = "> " if i == selected_option else "  "
            colour = "green" if i == selected_option else "white"
            text = small_font.render(prefix + option, True, colour)
            screen.blit(text, (900, 600 + i * 60))

        back_text = small_font.render("Press BACKSPACE to go back", True, "purple")
        screen.blit(audio_title, (200, 400))
        screen.blit(back_text, (200, 500))

    # S9021 Advanced Settings
    elif screen_stage == "9021":
        advanced_text = small_font.render("This will be peak! Advanced settings coming soon!", True, "orange")
        back_text = small_font.render("Press BACKSPACE to go back", True, "purple")
        screen.blit(advanced_text, (200, 400))
        screen.blit(back_text, (200, 500))

    # S9025 Wipe Save Warning
    elif screen_stage == "9025":
        warning_text = small_font.render("WARNING!", True, "red")
        warning_text2 = small_font.render("This will delete your save data.", True, "yellow")
        warning_text3 = small_font.render("Your knight's name will be lost to the 404 grave of abyss.", True, "red")

        options = ["[Cancel]", "[!Continue!]"]

        screen.blit(warning_text, (200, 300))
        screen.blit(warning_text2, (200, 370))
        screen.blit(warning_text3, (200, 420))

        for i, option in enumerate(options):
            prefix = "> " if i == selected_option else "  "
            colour = "green" if i == 0 and selected_option == i else "red" if i == 1 and selected_option == i else "white"
            text = small_font.render(prefix + option, True, colour)
            screen.blit(text, (900, 600 + i * 60))

    # S90252 Wipe Save Warning 2
    elif screen_stage == "90252":
        warning_text = small_font.render("WARNING!", True, "red")
        warning_text2 = small_font.render("This will delete your save data.", True, "yellow")
        warning_text3 = small_font.render("Your knight's name will be lost to the 404 grave of abyss.", True, "red")
        warning_text4 = small_font.render("ARE YOU SURE YOU WANT TO DELETE YOUR DATA", True, "purple")

        options = ["[Cancel]", "[!WIPE SAVE!]"]

        screen.blit(warning_text, (200, 300))
        screen.blit(warning_text2, (200, 370))
        screen.blit(warning_text3, (200, 420))
        screen.blit(warning_text4, (200, 470))

        for i, option in enumerate(options):
            prefix = "> " if i == selected_option else "  "
            colour = "green" if i == 0 and selected_option == i else "red" if i == 1 and selected_option == i else "white"
            text = small_font.render(prefix + option, True, colour)
            screen.blit(text, (900, 600 + i * 60))

    pygame.display.flip()

pygame.quit()

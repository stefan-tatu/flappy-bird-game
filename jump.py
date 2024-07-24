#  resolution 1920x1080
#  b - boss key
#  d - cheat add 2 potins
#  e - cheat make the pipes spaces bigger
#  f - makes the game slower

from tkinter import *
import random
import json
import os
import webbrowser
import csv


null = ""
not_null = False
choice = 1

global user_score
global username


def get_username():  # validates the name introduced by the user
    global username
    global value
    global not_null
    global menupage1
    while not not_null:
        if username.get() != null:
            not_null = True
            value = username.get()
            menu_page2()
        else:
            not_null = False
            menupage1.destroy()
            menu_page1()


def play(validtator=False):
    menupage2.destroy()
    global pause
    global play, control, updated
    play = True
    pause = False
    updated = False

    def init():  # initialise the global and common variables
        global obj_y, block_x, play, score, no_of_ups
        global frame, block_1, block_2, block_3
        global x_space, control, p_Up_2, p_Up_1, p_Down_2
        global p_Down_1, x_coord_2, x_coord_1, space_1, data, space
        obj_y = 150
        block_x = 2000
        play = True
        score = 0
        no_of_ups = 0
        frame = 40
        block_1 = 1350
        block_2 = 1350
        block_3 = 1350
        x_space = 300
        space = 300
        p_Up_2 = 0
        p_Up_1 = 0
        p_Down = 0
        p_Up = 0
        p_Down_2 = 0
        p_Down_1 = 0
        x_coord_2 = 0
        x_coord_1 = 0
        x_coord = 0
        space_1 = 0
        data = {}  # in case of new game, the pre-saved data will be lost
        data['valid'] = {'ok': False}
        data['basics'] = {'score': score, 'frame': frame, 'bird': obj_y}
        data['pipes'] = {'block_1': block_1, 'block_2': block_2,
                         'block_x': block_x, 'p_Up_1': p_Up_1,
                         'p_Down_1': p_Down_1, 'p_Up_2': p_Up_2,
                         'p_Down_2': p_Down_2, 'x_coord_2': x_coord_2,
                         'space_1': space_1, 'p_Down': p_Down, 'p_Up': p_Up,
                         'x_space': x_space, 'space': space,
                         'x_coord': x_coord, 'x_coord_1': x_coord_1}
        with open('savedata.json', 'w') as f:
            json.dump(data, f)

        f.close()
        try:
            control
        except NameError:
            control = None
        if control is None:
            control = '<space>'

    def init_2():  # initialise the common varibles for load option
        global no_of_ups, play, control
        play = True
        no_of_ups = 0
        try:
            control
        except NameError:
            control = None
        if control is None:
            control = '<space>'

    def pause_game():  # pause game activation
        global pause
        pause = True

    def boss_key(event):  # boss key activation
        global pause
        pause_game()
        webbrowser.open("shorturl.at/hjnHT")

    def resume_game():  # resume after pause
        global pause
        if pause is True:
            pause = False
            if play is True:
                birdDown()
                birdUp()
                move_piece()

    def update_leaderboard():   # update leaderboard with the last score
    	global value, score, sortlist, updated
    	if updated is False:
	    	with open ("leaderboard.csv", "a", newline='') as file:  
	    		fields=['score', 'name']                      
	    		writer=csv.DictWriter(file, fieldnames=fields)
	    		writer.writerow({'score' : score, 'name' : value})
	    		updated = True


    def show_leaderboard():  # show in the end of game where the player's score is
    	global score, value, canvas  # in the leaderboard
    	update_leaderboard()
    	j = 0
    	with open ("leaderboard.csv", "r") as file:
    		sortlist = []
    		reader = csv.reader(file)
    		for i in reader:
    			sortlist.append(i)
    			j += 1

    	for i in range (0, j):
    		sortlist[i][0]=int(sortlist[i][0])

    	sortlist.sort(reverse=True)

    	for postion in range (0, j):
    		if sortlist[postion][0] == score and sortlist[postion][1] == value:
    			break
    	
    	txt = canvas.create_text(500, 100, font="Times 20",
    							 text="How High is Your Current Score:")
    	if postion == 0:
    		txt = canvas.create_text(500, 150, font="Times 20",
    								 text=str(postion+1) + ".   " +
    								 str(sortlist[postion][1]) + " - " +
    								 str(sortlist[postion][0]))
    		if j >= 2:
    			txt = canvas.create_text(500, 200, font="Times 20",
    									 text=str(postion+2) + ".   " +
    									 str(sortlist[postion+1][1]) + " - " +
    									 str(sortlist[postion+1][0]))
    		if j >= 3:
    			txt = canvas.create_text(500, 250, font="Times 20",
    									 text=str(postion+3) + ".   " +
    									 str(sortlist[postion+2][1]) + " - " +
    									 str(sortlist[postion+2][0]))

    	elif postion != j - 1:
    		txt = canvas.create_text(500, 150, font="Times 20", text=str(postion) +
    								 ".   " + str(sortlist[postion-1][1]) + " - " +
    								 str(sortlist[postion-1][0]))
    		txt = canvas.create_text(500, 200, font="Times 20", text=str(postion+1) +
    								 ".   " + str(sortlist[postion][1]) + " - " +
    								 str(sortlist[postion][0]))
    		txt = canvas.create_text(500, 250, font="Times 20", text=str(postion+2) +
    								 ".   " + str(sortlist[postion+1][1]) + " - " +
    								 str(sortlist[postion+1][0]))

    	elif j > 2:
    		txt = canvas.create_text(500, 150, font="Times 20", text=str(postion-1) +
    								 ".   " + str(sortlist[postion-2][1]) + " - " +
    								 str(sortlist[postion-2][0]))
    		txt = canvas.create_text(500, 200, font="Times 20", text=str(postion) +
    								 ".   " + str(sortlist[postion-1][1]) + " - " +
    								 str(sortlist[postion-1][0]))
    		txt = canvas.create_text(500, 250, font="Times 20", text=str(postion+1) +
    								 ".   " + str(sortlist[postion][1]) + " - " +
    								 str(sortlist[postion][0]))

    	else:
    		txt = canvas.create_text(500, 150, font="Times 20", text=str(postion) +
    								 ".   " + str(sortlist[postion-1][1]) + " - " +
    								 str(sortlist[postion-1][0]))
    		txt = canvas.create_text(500, 200, font="Times 20", text=str(postion+1) +
    								 ".   " + str(sortlist[postion][1]) + " - " +
    								 str(sortlist[postion][0]))


    	canvas.pack()

    def block_reload():  # if we load a saved game, we need to load the pipes
        global block_1, block_2, block_x, p_Up_1, p_Down_1, space, x_coord
        global x_coord_1, p_Down_2, p_Up_2, x_coord_2, space_1
        global p_Down, p_Up, x_space
        if p_Up != 0:
            p_Up = canvas.create_rectangle(block_x, 0, block_x+100, x_coord,
                                           fill="#748B75", outline="#503D42",
                                           width=4)
            p_Down = canvas.create_rectangle(block_x, x_space + x_coord,
                                             block_x + 100, 800,
                                             fill="#748B75",
                                             outline="#503D42",
                                             width=4)

        if p_Up_1 != 0:
            p_Up_1 = canvas.create_rectangle(block_1, 0, block_1+100,
                                             x_coord_1, fill="#748B75",
                                             outline="#503D42", width=4)
            p_Down_1 = canvas.create_rectangle(block_1, space_1 + x_coord_1,
                                               block_1 + 100, 800,
                                               fill="#748B75",
                                               outline="#503D42",
                                               width=4)

        if p_Up_2 != 0:
            p_Up_2 = canvas.create_rectangle(block_2, 0, block_1+100,
                                             x_coord_2, fill="#748B75",
                                             outline="#503D42", width=4)
            p_Down_2 = canvas.create_rectangle(block_2, space_1 + x_coord_2,
                                               block_2 + 100, 800,
                                               fill="#748B75",
                                               outline="#503D42",
                                               width=4)

        canvas.pack()

    def save_game():  # the function saving the game
        global pause, data, score, obj_y, frame, data, play
        global block_1, block_2, block_x, p_Up_1, p_Down_1, x_coord_1
        global p_Down_2, p_Up_2, x_coord_2, space_1, p_Down
        global p_Up, x_space, space, x_coord
        pause = True
        if play is True:
            data['valid'] = {'ok': True}
            data['basics'] = {'score': score, 'frame': frame, 'bird': obj_y}
            data['pipes'] = {'block_1': block_1, 'block_2': block_2,
                             'block_x': block_x, 'p_Up_1': p_Up_1,
                             'p_Down_1': p_Down_1, 'p_Up_2': p_Up_2,
                             'p_Down_2': p_Down_2, 'x_coord_2': x_coord_2,
                             'space_1': space_1, 'p_Down': p_Down,
                             'p_Up': p_Up, 'x_space': x_space,
                             'space': space, 'x_coord': x_coord,
                             'x_coord_1': x_coord_1}
            with open('savedata.json', 'w') as f:
                json.dump(data, f)
            f.close()

    def save_exit():  # if the game is over, it will only exit the game
    	global play, window_game  # otherwise, it is save and exit
    	if play is True:
    		save_game()
    	window_game.destroy()
    	

    def cheat_1(event):  # this cheat code adds two extra points
        global score, play
        if play is True:
	        score = score + 2
	        scr_frame = menu_g.create_rectangle(20, 25, 165, 75,
	                                            fill="#E0D796",
	                                            outline="#E0D796", width=4)
	        scr_txt = menu_g.create_text(85, 55, font=("Helvetica", 18),
	                                     text="Score: " + str(score))

    def cheat_2(event):  # this cheat code enlarges the spaces between pipes,
        global x_space, play   # up to a certain value max, every time used
        if space < 400 and play is True:
            x_space = x_space+5

    def cheat_3(event):  # this makes the game move slower, max to acertain
        global frame, play     # frame rate, every time used
        if frame < 60 and play is True:
            frame = frame+2

    def back_from_info():  # function for controls info to dissapear
    	global wd_info     # and unpause game
    	wd_info.destroy()
    	resume_game()

    def controls_info():  # page to show the player the controls
        global wd_info
        pause_game()
        wd_info = Tk()
        wd_info.geometry("550x600")
        wd_info.configure(background="#71C5CF") 
        wd_info.title("Controls info")
        Label(wd_info, text="Game Controls", bg="#71C5CF",
              font="Times 30").pack()
        info = Canvas(wd_info, bg="#E0D796", width=450, height=500)
        info.create_text(220, 50, fill="#475841",
                         font="Times 20", text="<b> - boss key")
        info.create_text(220, 120, fill="#475841", font="Times 20",
                         text="<d> - (cheat) +2 points each press", )
        info.create_text(220, 190, fill="#475841", font="Times 20",
                         text="<e> - (cheat) enlarge pipes space", )
        info.create_text(220, 260, fill="#475841", font="Times 20",
                         text="<f> - (cheat) make the game slower", )
        info.create_text(220, 330, fill="#475841", font="Times 20",
                         text=str(control) + " - controls the bird", )
        button_back = Button(info, text="Exit Game",
                              command=back_from_info, bg="#748B75",
                              height="3", width="14",).place(x=150, y=400)
        info.pack()

    def menu_config():  # function configuring the left menu
        global score, window_game
        try:
            score
        except NameError:
            score = None
        if score is None:
            score = 0
        scr_frame = menu_g.create_rectangle(10, 20, 170, 80,
                                            fill="#E0D796", outline="#503D42",
                                            width=4)
        scr_txt = menu_g.create_text(85, 55, font=("Helvetica", 18),
                                     text="Score: " + str(score))
        button_pause = Button(menu_g, text="Pause",
                              command=pause_game, bg="#748B75",
                              height="3", width="14",).place(x=20, y=300)
        button_resume = Button(menu_g, text="Resume",
                               command=resume_game, bg="#748B75",
                               height="3", width="14",).place(x=20, y=400)
        button_info = Button(menu_g, text="Info",
                             command=controls_info, bg="#748B75",
                             height="3", width="14",).place(x=20, y=500)
        button_save_exit = Button(menu_g, text="Save and Exit",
                             command=save_exit, bg="#71C5CF",
                             height="3", width="14",).place(x=20, y=600)
        button_save = Button(menu_g, text="Save",
                             command=save_game, bg="#71C5CF",
                             height="3", width="14",).place(x=20, y=700)
        menu_g.pack(side="left")

    def set_window_game():  # we configure the main game window
        window_game.geometry("1500x800")
        window_game.configure(background='#475841')
        window_game.title(u'\u2730' + " L E T's   J U M P  " +
                          u'\u2730' + "   G A M E")

    def block_random():  # generates pipes with random position of holes
        global x_space, x_coord, p_Down, p_Up, block_x, space
        block_x = 1350
        space = x_space
        x_coord = random.randint(150, 480)
        p_Up = canvas.create_rectangle(block_x, 0, block_x + 100,
                                       x_coord, fill="#748B75",
                                       outline="#503D42", width=4)
        p_Down = canvas.create_rectangle(block_x, x_space + x_coord,
                                         block_x + 100, 800, fill="#748B75",
                                         outline="#503D42", width=4)
        canvas.pack()


    def score_count(block):  # count the score for the current round
        global score
        if obj_y >= block:
            score += 1
            scr_frame = menu_g.create_rectangle(10, 20, 170, 80,
                                                fill="#E0D796",
                                                outline="#503D42", width=4)
            scr_txt = menu_g.create_text(85, 55, font=("Helvetica", 18),
                                         text="Score: " + str(score))

        levelUP()

    def levelUP():  # at every 9 points earned, the game becomes harder,
        global score, frame, x_space  # as the space between pipes will be
        if score % 9 == 0 and score != 0:  # less and the game will move faster
            if x_space > 199:
                x_space = x_space - 5
            if frame > 19:
                frame = frame - 2

    def lose():  # function detrmining game loose
        global play, restart_box
        if obj_y > 800:
            play = False
            bird = canvas.create_image(100, obj_y, image=bird_states[3])
            restart_box = canvas.create_rectangle(300, 50, 700, 500,
                                                  fill="#D4AC57",
                                                  outline="#503D42",
                                                  width=4)
            gameover_text = canvas.create_text(500, 375,
                                               font=("Helvetica", 32),
                                                   text="GAME OVER")
            restart_text = canvas.create_text(500, 450,
                                              font=("Helvetica", 32),
                                              text="Press R to restart")
            show_leaderboard()

    global window_game, bird, bird_states, canvas
    window_game = Tk()
    set_window_game()
    menu_g = Canvas(window_game, width=190, height=800,
                    background="#503D42", bd=0, highlightthickness=0)
    menu_config()
    canvas = Canvas(window_game, width=1000, heigh=800,
                    background="#CED0CE", bd=0, highlightthickness=0)
    canvas.pack()

    if validtator is False:
        init()
    else:
        init_2()
        block_reload()
    # to have the 4 stages of the bird
    bird_states = [PhotoImage(file='images/0.png'),
                   PhotoImage(file='images/1.png'),
                   PhotoImage(file='images/2.png'),
                   PhotoImage(file='images/dead.png')]
    bird = canvas.create_image(100, obj_y, image=bird_states[0])

    def collusion():  # collusion detect
        global block_2, p_Up_2, p_Down_2, x_coord_2, space_1, obj_y, play
        if obj_y - 20 < x_coord_2 or obj_y + 20 > space_1 + x_coord_2:
            play = False
            birdDown()

    def move_piece():  # generates pieces in a row and moves them
        global block_1, block_2, block_x, p_Up_1, p_Down_1, x_coord_1
        global p_Down_2, p_Up_2, x_coord_2, space_1, p_Up, p_Down
        lose()
        if play is True:
            if block_2 < 120 and block_2 > 0:
                collusion()
            if block_2 < 5 and block_2 > 0:
                score_count(block_2)

            if block_x == 2000:
                block_random()
            elif block_2 == 1350 and block_1 == 1350:
                if block_x > 960:
                    block_x -= 4
                    canvas.coords(p_Up, block_x, 0, block_x + 100, x_coord)
                    canvas.coords(p_Down, block_x, space + x_coord,
                                  block_x + 100, 800)
                elif block_x < 960 and block_x > 955:
                    block_1 = block_x
                    p_Up_1 = p_Up
                    p_Down_1 = p_Down
                    x_coord_1 = x_coord
                    space_1 = space
                    block_random()
                    canvas.coords(p_Up, block_x, 0, block_x + 100, x_coord)
                    canvas.coords(p_Down, block_x, space + x_coord,
                                  block_x + 100, 800)

            elif block_2 == 1350:
                if block_x > 960:
                    block_x -= 4
                    block_1 -= 4
                    space_1 = space
                    canvas.coords(p_Up, block_x, 0, block_x + 100, x_coord)
                    canvas.coords(p_Down, block_x, space + x_coord,
                                  block_x + 100, 800)
                    canvas.coords(p_Up_1, block_1, 0, block_1 + 100, x_coord_1)
                    canvas.coords(p_Down_1, block_1, space_1 + x_coord_1,
                                  block_1 + 100, 800)

                elif block_x < 960 and block_x > 955:
                    block_2 = block_1
                    p_Up_2 = p_Up_1
                    p_Down_2 = p_Down_1
                    x_coord_2 = x_coord_1
                    block_1 = block_x
                    p_Up_1 = p_Up
                    p_Down_1 = p_Down
                    x_coord_1 = x_coord
                    space_1 = space
                    block_random()
                    canvas.coords(p_Up, block_x, 0, block_x + 100, x_coord)
                    canvas.coords(p_Down, block_x, space + x_coord,
                                  block_x + 100, 800)

            elif block_2 > - 101 and block_2 < 1350:
                    block_x -= 4
                    block_1 -= 4
                    block_2 -= 4
                    space_1 = space
                    canvas.coords(p_Up, block_x, 0, block_x + 100, x_coord)
                    canvas.coords(p_Down, block_x,
                                  space + x_coord, block_x + 100, 800)
                    canvas.coords(p_Up_1, block_1, 0, block_1 + 100, x_coord_1)
                    canvas.coords(p_Down_1, block_1,
                                  space_1 + x_coord_1, block_1 + 100, 800)
                    canvas.coords(p_Up_2, block_2, 0, block_2 + 100, x_coord_2)
                    canvas.coords(p_Down_2, block_2,
                                  space_1 + x_coord_2, block_2 + 100, 800)

            elif block_2 < -102:
                block_x -= 4
                block_1 -= 4
                block_2 -= 4
                block_2 = block_1
                p_Up_2 = p_Up_1
                p_Down_2 = p_Down_1
                x_coord_2 = x_coord_1
                block_1 = block_x
                p_Up_1 = p_Up
                p_Down_1 = p_Down
                x_coord_1 = x_coord
                space_1 = space
                block_random()
                canvas.coords(p_Up, block_x, 0, block_x + 100, x_coord)
                canvas.coords(p_Down, block_x,
                              space + x_coord, block_x + 100, 800)

            else:
                block_x -= 4
                block_1 -= 4
                block_2 -= 4
                block_2 = block_1
                p_Up_2 = p_Up_1
                p_Down_2 = p_Down_1
                x_coord_2 = x_coord_1
                block_1 = block_x
                p_Up_1 = p_Up
                p_Down_1 = p_Down
                x_coord_1 = x_coord
                space_1 = space
                block_random()
                canvas.coords(p_Up, block_x, 0, block_x + 100, x_coord)
                canvas.coords(p_Down, block_x,
                              space + x_coord, block_x + 100, 800)

        if pause is False and play is True:
            window_game.after(frame, move_piece)

    def birdUp(event=None):  # function for bird to go up
        global obj_y
        global no_of_ups
        global play

        lose()
        if play is True and pause is False:
            canvas.itemconfig(bird, image=bird_states[2])
            canvas.tag_raise(bird)
            obj_y -= 10
            if obj_y <= 20:
                obj_y = 20
            canvas.coords(bird, 100, obj_y)
            if no_of_ups < 3:
                no_of_ups += 1
                canvas.itemconfig(bird, image=bird_states[1])
                canvas.tag_raise(bird)

                if pause is False:
                    window_game.after(frame, birdUp)
            else:
                no_of_ups = 0

    def birdDown():  # function for bird to go down
        global obj_y
        global play
        if play is not False:
            obj_y += 6
            lose()
            canvas.itemconfig(bird, image=bird_states[0])
            canvas.tag_raise(bird)
            canvas.coords(bird, 100, obj_y)
            if play is not False:
                if pause is False:
                    window_game.after(frame, birdDown)
        else:
            obj_y += 6
            canvas.itemconfig(bird, image=bird_states[3])
            canvas.tag_raise(bird)
            canvas.coords(bird, 100, obj_y)
            if obj_y < 1000:
                window_game.after(30, birdDown)
            else:
                restart_box = canvas.create_rectangle(300, 50, 700, 500,
                                                      fill="#D4AC57",
                                                      outline="#503D42",
                                                      width=4)
                gameover_text = canvas.create_text(500, 375,
                                                   font=("Helvetica", 32),
                                                   text="GAME OVER")
                restart_text = canvas.create_text(500, 450,
                                                  font=("Helvetica", 32),
                                                  text="Press R to restart")
                show_leaderboard()

    def restart(event):  # restart game 
        global canvas, play, pause, window_game, value, score, updated
        if play is False:
        	canvas.destroy()
        	canvas = Canvas(window_game, width=1000, heigh=800,
        					background="#CED0CE", bd=0, highlightthickness=0)
        	canvas.pack()

        	bird = canvas.create_image(100, obj_y, image=bird_states[0])
        	init()
        	score=0
        	menu_g = Canvas(window_game, width=190, height=800,
        					background="#503D42", bd=0, highlightthickness=0)
        	menu_config()
        	play = True
        	pause = False
        	updated=False
        	window_game.after(frame, birdDown)
        	window_game.bind(control, birdUp)
        	window_game.after(frame, move_piece)
        	window_game.bind("b", boss_key)
        	window_game.bind("d", cheat_1)
        	window_game.bind("e", cheat_2)
        	window_game.bind("f", cheat_3)
        	window_game.bind("r", restart)
    menu_config()

    window_game.after(frame, birdDown)
    window_game.bind(control, birdUp)
    window_game.after(frame, move_piece)
    window_game.bind("b", boss_key)
    window_game.bind("d", cheat_1)
    window_game.bind("e", cheat_2)
    window_game.bind("f", cheat_3)
    window_game.bind("r", restart)
    window_game.mainloop()


def load():  # function to load the data for a saved game
    global data, validator, space, p_Down, p_Up, x_coord
    global obj_y, block_x, play, score, no_of_ups, frame, block_1
    global block_2, block_3, x_space, x_coord_1, space_1, data
    global control, p_Up_2, p_Up_1, p_Down_2, p_Down_1, x_coord_2
    f = open('savedata.json')
    data = json.load(f)
    validator = data['valid']['ok']
    score = data['basics']['score']
    frame = data['basics']['frame']
    obj_y = data['basics']['bird']
    block_1 = data['pipes']['block_1']
    block_2 = data['pipes']['block_2']
    block_x = data['pipes']['block_x']
    p_Down_1 = data['pipes']['p_Down_1']
    p_Up_1 = data['pipes']['p_Up_1']
    p_Up_2 = data['pipes']['p_Up_2']
    p_Down_2 = data['pipes']['p_Down_2']
    x_coord_2 = data['pipes']['x_coord_2']
    x_coord_1 = data['pipes']['x_coord_1']
    x_coord = data['pipes']['x_coord']
    space_1 = data['pipes']['space_1']
    p_Down = data['pipes']['p_Down']
    p_Up = data['pipes']['p_Up']
    x_space = data['pipes']['x_space']
    space = data['pipes']['space']
    f.close()
    play(validator)

global control


def choose_space():
    global control
    control = '<space>'


def choose_up():
    global control
    control = '<Up>  '


def choose_click():
    global control
    control = '<Button-1> '


def choose_w():
    global control
    control = 'w'


def change_key():  # menu gor control key changing
    global window_chcontrol
    menupage2.destroy()
    window_chcontrol = Tk()
    window_chcontrol.geometry("300x450")
    window_chcontrol.configure(background="#748B75")
    window_chcontrol.title("Change jump key")
    button_Space = Button(window_chcontrol, text="Space", bg="#CED0CE",
                          command=choose_space, height="2",
                          width="20",).place(x=60, y=50)
    button_up = Button(window_chcontrol, text="Up Key", bg="#CED0CE",
                       command=choose_up, height="2",
                       width="20",).place(x=60, y=150)
    button_click = Button(window_chcontrol, text="Right Click", bg="#CED0CE",
                          command=choose_click, height="2",
                          width="20", ).place(x=60, y=250)
    button_w = Button(window_chcontrol, text="W", bg="#CED0CE",
                      command=choose_w, height="2",
                      width="20", ).place(x=60, y=350)
    button_menu = Button(window_chcontrol, text="Back", bg="#D4AC57",
                         command=back_1, height="2",
                         width="20", ).place(x=60, y=350)
    window_chcontrol.mainloop()


def menu_page1():  # this menu page collect the naame of the user
    global menupage1  # with the posibility to exit the game from this stage
    global value
    menupage1 = Tk()
    menupage1.title(u'\u2730' + " L E T's   J U M P  " +
                    u'\u2730' + "   G A M E")
    menupage1.geometry("500x150")
    menupage1.configure(background="#CED0CE")

    global username
    username = StringVar()
    username_label = Label(
        menupage1, text="Enter your name here: ",
        bg="#CED0CF", font="Helvetica 20"
    ).pack()
    entry = Entry(menupage1, textvariable=username).place(x=170, y=50)
    button_ok = Button(
        menupage1,
        text="ENTER",
        bg="#D4AC57",
        command=get_username,
        height="1",
        width="10",
    ).place(x=100, y=100)
    button_exit = Button(
        menupage1,
        text="EXIT",
        bg="#748B75",
        command=menupage1.destroy,
        height="1",
        width="10",
    ).place(x=300, y=100)

    menupage1.mainloop()


def back_1():  # to return from change key to menu
    global window_chcontrol
    window_chcontrol.destroy()
    menu_page2_2()


def back_2():
    global window_game
    window_game.destroy()
    menu_page2_2()


def leaderboard_destroy():  # exit from leaderboard, back to menu
	global ldbpage
	ldbpage.destroy()
	menu_page2_2()


def leaderboard_page():   # this configure leaderboard page
	global ldbpage, menupage2
	menupage2.destroy()
	ldbpage = Tk()
	ldbpage.title("Leaderboard")
	ldbpage.geometry("300x370")
	j = 0
	with open ("leaderboard.csv", "r") as file:
		sortlist = []
		reader = csv.reader(file)
		for i in reader:
			sortlist.append(i)
			j += 1

	for i in range (0, j):
		sortlist[i][0]=int(sortlist[i][0])

	sortlist.sort(reverse=True)

	crd = 50
	info = Canvas(ldbpage, bg="#E0D796", width=250, height=300)
	if j < 6:
		for i in range (0, j):
			info.create_text(120, crd, fill="#475841", font="Times 20",
	                         text=str(i+1) + ".   " +
	                         str(sortlist[i][1]) + " - " +
	                         str(sortlist[i][0]))
			crd = crd+50
	else:
		for i in range (0, 5):
			info.create_text(120, crd, fill="#475841", font="Times 20",
	                         text=str(i+1) + ".   " +
	                         str(sortlist[i][1]) + " - " +
	                         str(sortlist[i][0]))
			crd = crd+50

	button_exit = Button(ldbpage, text="EXIT", bg="#748B75",
						 command=leaderboard_destroy, height="1",
						 width="10",).place(x=100, y=320)

	info.pack()



def menu_page2_2():  # second verios of it when you return to menu
    global menupage2, window_play
    menupage2 = Tk()
    menupage2.title(u'\u2730' + " L E T's   J U M P  " +
                    u'\u2730' + "   G A M E")
    menupage2.geometry("300x600")
    menupage2.configure(background="#CED0CE")
    title_page = Label(menupage2, text=" Game menu", bg="#CED0CE",
                       font="Helvetica 20").pack()
    button_play = Button(menupage2, text="Play", command=play,
                         bg="#D4AC57", height="2", width="20",).place(x=60,
                                                                      y=100)
    button_load = Button(menupage2, text="Load", command=load,
                         bg="#9bcf9b", height="2", width="20",).place(x=60,
                                                                      y=200)
    button_leaderboard = Button(menupage2, text="Leaderboard",
                                command=leaderboard_page, bg="#748B75",
                                height="2",
                                width="20",).place(x=60, y=300)
    button_change_user = Button(menupage2, text="Change Key Controls",
                                command=change_key, bg="#748B75", height="2",
                                width="20",).place(x=60, y=400)
    button_exit = Button(menupage2, text="Exit", command=menupage2.destroy,
                         bg="#71C5CF", height="2",
                         width="20", ).place(x=60, y=500)
    menupage2.mainloop()


def menu_page2():  # this sets the menu with bottons for various funcionalities
    global menupage1, menupage2, window_play, scoreboard
    menupage2 = Tk()
    menupage2.title(u'\u2730' + " L E T's   J U M P  " +
                    u'\u2730' + "   G A M E")
    menupage2.geometry("300x600")
    menupage2.configure(background="#CED0CE")
    title_page = Label(menupage2, text=" Game menu", bg="#CED0CE",
                       font="Helvetica 20").pack()
    button_play = Button(menupage2, text="Play", command=play,
                         bg="#D4AC57", height="2", width="20",).place(x=60,
                                                                      y=100)
    button_load = Button(menupage2, text="Load", command=load,
                         bg="#9bcf9b", height="2", width="20",).place(x=60,
                                                                      y=200)
    button_leaderboard = Button(menupage2, text="Leaderboard",
                                command=leaderboard_page,
                                bg="#748B75", height="2",
                                width="20",).place(x=60, y=300)
    button_change_user = Button(menupage2, text="Change Key Controls",
                                command=change_key, bg="#748B75", height="2",
                                width="20",).place(x=60, y=400)
    button_exit = Button(menupage2, text="Exit", command=menupage2.destroy,
                         bg="#71C5CF", height="2",
                         width="20", ).place(x=60, y=500)
    get_username()
    menupage1.destroy()
    menupage2.mainloop()

menu_page1()



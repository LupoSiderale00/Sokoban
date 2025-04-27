import sys
import os
from readchar import readkey, key

#Global variables for level state, targets, and UI elements
level_global = []
level_t = None
target_pos = []
target_done = 0
n_target = 0
moves = [
    "Moves:",
    0
    ]
legend = [
        "Legend:",
        "# : Wall",
        "$ : Box",
        ". : Target",
        "@ : Player",
        "* : Box on Target"
    ]
controls = [
        "Controls:",
        "W - Up",
        "A - Left",
        "S - Down",
        "D - Right",
        "Q - Quit",
        "R = Reset"
    ]

#Main function, clear terminal, print explanation and then asks user for difficulty. The result will be used to open the correct level and searched how many objectives, then the board will be displayed and the input will be read
def main():
    clear_terminal()
    explanation()
    difficulty = level_selector()
    level = open_level(difficulty)
    find_target()
    display_board(level)
    read_movement()

#Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Function that explains the project to the player and asks for difficulty
def explanation():
    print("This project is a CLI-based Sokoban game where the objective is to push the box into the correct position to win.\nPlease select your desired difficulty level below.\n")

#Function that prompt the user difficulty selection
def level_selector():
    while True:
        s = input("Choose a difficulty: (H)ard or (E)asy? ").lower().strip()
        if s == "easy" or s == "e":
            s = "e"
            return s
        elif s == "hard" or s == "h":
            s = "h"
            return s
        else:
            continue

#Function that open and create cache version of level based on difficulty selected by user
def open_level(difficulty):
    #Select correct level based on difficulty
    if difficulty == "e":
        level = "level1.txt"
    else:
        level = "level2.txt"
    #Try to open level with name of difficulty selected
    try:
        with open(level) as file:
            global level_global
            lines = file.readlines()
            for line in lines:
                if "\n" in line:
                    line = line.replace("\n","")
                level_global.append(list(line))


        #Create a copy of the level that will be used for this game
        with open(level[:-4]+"current"+".txt", "w") as file:
             file.writelines(lines)
             global level_t
             level_t = level
             return lines
    #If the file doesn't exits, use sys.exit to quit the program and tell the user that the file doesn't exist
    except (FileNotFoundError):
        sys.exit("File does not exist")

#Function that display the board
def display_board(level):
    #Clear the terminal and get the max len that will be displayed in the terminal
    clear_terminal()
    max_lines = max(len(level_global), len(legend), len(controls), len(moves))

    #loop that prints each line for every tab with justification and correct spacing using max_lines as range for loop
    for i in range(max_lines):
        board_row = "".join(level_global[i]) if i < len(level_global) else ""
        legend_row = legend[i] if i < len(legend) else ""
        control_row = controls[i] if i < len(controls) else ""
        moves_row = moves[i] if i <len(moves) else ""
        print(f"{board_row.ljust(15)} {legend_row.ljust(25)} {control_row.ljust(25)} {moves_row}")

#Function that reads the player's movement
def read_movement():
    while True:
        k = readkey()
        k = k.lower()
        if k == "w" :
            move_up()
        if k == "s" :
            move_down()
        if k == "a" :
            move_left()
        if k == "d" :
            move_right()
        #if key pressed is q, the game will quit via sys.exit
        if k == "q":
            sys.exit("User has quit the game")
        #if key pressed is r, reload the python program to restart the game
        if k == "r":
            os.execv(sys.executable, ['python'] + sys.argv)

#Function that moves the player up
def move_up():
    global target_done
    #Get player position
    pos_row,pos_col = get_player_pos()

    #if there is empy space,move player and update the board and counter and save board
    if level_global[pos_row-1][pos_col] == " ":
        level_global[pos_row-1][pos_col] = "@"
        level_global[pos_row][pos_col] = " "
        save_level_copy()
        clear_terminal()
        moves[1]+=1
        update_board()

    #Check if player is moving aganst a box
    elif level_global[pos_row-1][pos_col] == "$":

        #if there is empy space behind box, move the box, player and update the board and counter and save board
        if level_global[pos_row-2][pos_col] == " ":
            level_global[pos_row-1][pos_col] = "@"
            level_global[pos_row-2][pos_col] = "$"
            level_global[pos_row][pos_col] = " "
            save_level_copy()
            clear_terminal()
            moves[1]+=1
            update_board()

        #if there is an objective behind the box, move the box, player and update the board counter save the board and check winning condition
        elif level_global[pos_row-2][pos_col] == ".":
            level_global[pos_row-2][pos_col] = "*"
            level_global[pos_row-1][pos_col] = "@"
            level_global[pos_row][pos_col]   = " "
            save_level_copy()
            clear_terminal()
            moves[1]+=1
            update_board()
            target_done+=1
            check_winning_cond()

        else:
            print("Player cannot move there")


    else:
        print("Player cannot move there")

#Function that moves the player down
def move_down():
    global target_done
    #Get player position
    pos_row,pos_col = get_player_pos()

    #if there is empy space,move player and update the board and counter and save board
    if level_global[pos_row+1][pos_col] == " ":
        level_global[pos_row+1][pos_col] = "@"
        level_global[pos_row][pos_col] = " "
        save_level_copy()
        clear_terminal()
        moves[1]+=1
        update_board()

    #Check if player is moving against a box
    elif level_global[pos_row+1][pos_col] == "$":

        #if there is empy space behind box, move the box, player and update the board and counter and save board
        if level_global[pos_row+2][pos_col] == " ":
            level_global[pos_row+1][pos_col] = "@"
            level_global[pos_row+2][pos_col] = "$"
            level_global[pos_row][pos_col] = " "
            save_level_copy()
            clear_terminal()
            moves[1]+=1
            update_board()

        #if there is an objective behind the box, move the box, player and update the board counter save the board and check winning condition
        elif level_global[pos_row+2][pos_col] == ".":
            level_global[pos_row+1][pos_col] = "@"
            level_global[pos_row+2][pos_col] = "*"
            level_global[pos_row][pos_col] = " "
            save_level_copy()
            clear_terminal()
            moves[1]+=1
            update_board()
            target_done+=1
            check_winning_cond()

        else:
            print("Cannot move box")

    else:
        print("Player cannot move there")

#Function that moves the player left
def move_left():
    global target_done
    pos_row,pos_col = get_player_pos()

    #if there is empy space,move player and update the board and counter and save board
    if level_global[pos_row][pos_col-1] == " ":
        level_global[pos_row][pos_col-1] = "@"
        level_global[pos_row][pos_col] = " "
        save_level_copy()
        clear_terminal()
        moves[1]+=1
        update_board()

    #Check if player is moving aganst a box
    elif level_global[pos_row][pos_col-1] == "$":

        #if there is empy space behind box, move the box, player and update the board and counter and save board
        if level_global[pos_row][pos_col-2] == " ":
            level_global[pos_row][pos_col-1] = "@"
            level_global[pos_row][pos_col-2] = "$"
            level_global[pos_row][pos_col] = " "
            save_level_copy()
            clear_terminal()
            moves[1]+=1
            update_board()

        #if there is an objective behind the box, move the box, player and update the board counter save the board and check winning condition
        elif level_global[pos_row][pos_col-2] == ".":
            level_global[pos_row][pos_col-1] = "@"
            level_global[pos_row][pos_col-2] = "*"
            level_global[pos_row][pos_col] = " "
            save_level_copy()
            clear_terminal()
            moves[1]+=1
            update_board()
            target_done+=1
            check_winning_cond()

        else:
            print("Cannot move box")

    else:
        print("Player cannot move there")

#Function that moves the player right
def move_right():
    global target_done
    pos_row,pos_col = get_player_pos()

    #if there is empy space,move player and update the board and counter and save board
    if level_global[pos_row][pos_col+1] == " ":
        level_global[pos_row][pos_col+1] = "@"
        level_global[pos_row][pos_col] = " "
        save_level_copy()
        clear_terminal()
        moves[1]+=1
        update_board()

    #Check if player is moving aganst a box
    elif level_global[pos_row][pos_col+1] == "$":

        #if there is empy space behind box, move the box, player and update the board and counter and save board
        if level_global[pos_row][pos_col+2] == " ":
            level_global[pos_row][pos_col+1] = "@"
            level_global[pos_row][pos_col+2] = "$"
            level_global[pos_row][pos_col] = " "
            save_level_copy()
            clear_terminal()
            moves[1]+=1
            update_board()

        #if there is an objective behind the box, move the box, player and update the board counter save the board and check winning condition
        elif level_global[pos_row][pos_col+2] == ".":
            level_global[pos_row][pos_col+1] = "@"
            level_global[pos_row][pos_col+2] = "*"
            level_global[pos_row][pos_col] = " "
            save_level_copy()
            clear_terminal()
            moves[1]+=1
            update_board()
            target_done+=1
            check_winning_cond()

        else:
            print("Player cannot move there")

    else:
        print("Player cannot move there")

#Function that gets the position of the player before movement and return both the column and row
def get_player_pos():
    for index, line in enumerate(level_global):
        if "@" in line:
            current_row = index
            current_column = line.index("@")
            return current_row,current_column
        else:
            continue

#Function to update the board if player's movement was "legal"
def update_board():
    #Clear the terminal and get the max len that will be displayed in the terminal
    clear_terminal()
    max_lines = max(len(level_global), len(legend), len(controls), len(moves))

    #loop that prints each line for every tab with justification and correct spacing using max_lines as range for loop
    for i in range(max_lines):
        board_row = "".join(level_global[i]) if i < len(level_global) else ""
        legend_row = legend[i] if i < len(legend) else ""
        control_row = controls[i] if i < len(controls) else ""
        moves_row = moves[i] if i <len(moves) else ""
        print(f"{board_row.ljust(15)} {legend_row.ljust(25)} {control_row.ljust(25)} {moves_row}")

#Function that finds the target(s) in the board and save their position in list taget_pos and then get len of it and save it as n_target global var
def find_target():
    global target_pos
    for index, line in enumerate(level_global):
        if "." in line:
            current_row = index
            current_column = line.index(".")
            pos = str(current_row)+ "," +str(current_column)
            target_pos.append(pos)

        else:
            continue
    global n_target
    n_target = len(target_pos)

#Function that checks if the player has enough winning condition as there are in the level, if so function final_screen is called
def check_winning_cond():
    if target_done == n_target:
        final_screen()

#Function that is called when the player has solved the level. It shows the player how many moves they did and asks to either restart or quit the game
def final_screen():
    clear_terminal()
    print(f"Congrats! You won the game! It took you {moves[1]} moves to complete the game!")
    print("If you want to play again, press 'r' or 'q' to quit")

#Functions that save a copy of the level selected, so we can modify real time with player's movement without having to restore the file after the game is quit
def save_level_copy():
    with open(level_t[:-4]+"current"+".txt", "w") as file:
        for row in level_global:
            file.write("".join(row)+"\n")

if __name__ == "__main__":
    main()




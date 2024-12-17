import random
# --------- GAME VALUE ---------
game_status = 1
machine_turn = 0
human_turn = 1
winning = 0
board = [
    ' ',' ',' ',
    ' ',' ',' ',
    ' ',' ',' ',
]
# --------- GAME VALUE ---------

def random_role():
    return [x for x in set(["X","O"])]

def display_board():
    return f"{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} | {board[5]}\n{board[6]} | {board[7]} | {board[8]}"

def machine_play_logic(value):
    global human_turn,machine_turn
    choose = random.randint(0,len(board) - 1)
    if board[choose] == " ":
        human_turn = 1
        machine_turn = 0
        board[choose] = value
    return "machine choosed at position " + str(choose +1)+"\n" + display_board() +"\n" + "Switching to human turn......"

def human_play_logic(position,value):
    global human_turn,machine_turn
    position = int(position) - 1
    if not board[position] == " ":
        return f"cannot add {value} because this already has one"
    else:
        human_turn = 0
        machine_turn = 1
        board[position] = value
        return f"Sucessfully added {value}\n" + display_board() +"\n" + "Switching to machine turn......"
def winning_logic():
    global game_status, winning
    winning_positions = [
    (0, 1, 2),  # Row 1
    (3, 4, 5),  # Row 2
    (6, 7, 8),  # Row 3
    (0, 3, 6),  # Column 1
    (1, 4, 7),  # Column 2
    (2, 5, 8),  # Column 3
    (0, 4, 8),  # Diagonal 1
    (2, 4, 6)   # Diagonal 2
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            game_status = 0  
            print((f"Player {board[a]} wins!"))
            winning = 1
def draw_logic():
    global game_status
    if not ' ' in board and not winning == True:
        game_status = 0
        print("Draw")

def main():
    print("You now play as",random_role()[0])
    while game_status:
        if human_turn:
            print(display_board())
            print("This is your turn now")
            player_input = input("Enter which number do you want to choose 1,9, e to exit\n>> ")
            if player_input == "e":
                break
            if not player_input.isdigit():
                print("invalid input")
                continue
            if int(player_input) < 1 or int(player_input) > 9:
                print("invalid input")
                continue
            print(human_play_logic(player_input,random_role()[0]))
        else:
            print(machine_play_logic(random_role()[1]))
        winning_logic()
        draw_logic()
if __name__ == "__main__":
    main()


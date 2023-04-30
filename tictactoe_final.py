import random
print( " This is a Tic Tac Toe Game where you will go against a ai. The board is going from 1-9 from top left to bottom right so chose your number wisely or I will win")

game_numbers = [1,2,3,4,5,6,7,8,9]

game_board = [[1,2,3], [4,5,6], [7,8,9]]

board_rows = 3

board_collum = 3

def off_gameboard():
    for i in range(board_rows):
        print("\n+---+---+---+")
        print("|", end="")
        for x in range(board_collum):
            print("", game_board[i][x], end=" |")
    print("\n+---+---+---+")

def modify_gameboard(num, turn):
    num -= 1
    if(num == 0):
        game_board[0][0] = turn
    elif(num == 1):
        game_board[0][1] = turn
    elif(num == 2):
        game_board[0][2] = turn
    elif(num == 3):
        game_board[1][0] = turn
    elif(num == 4):
        game_board[1][1] = turn
    elif(num == 5):
        game_board[1][2] = turn
    elif(num == 6):
        game_board[2][0] = turn
    elif(num == 7):
        game_board[2][1] = turn
    elif(num == 8):
        game_board[2][2] = turn


def winner_check(game_board):
#code for all horizontal wins since there are 3 ways to win it counts 6 because the possibility for 'X' and 'O'
    if game_board[0][0] == 'X' and game_board[0][1] == 'X' and game_board[0][2] == 'X':
        print("Congrats X won")
        return "X"
    elif game_board[0][0] == 'O' and game_board[0][1] == 'O' and game_board[0][2] == 'O':
        print("Congrats O won")
        return "O"
    elif game_board[1][0] == 'X' and game_board[1][1] == 'X' and game_board[1][2] == 'X':
        print("Congrats X won")
        return "X"
    elif game_board[1][0] == 'O' and game_board[1][1] == 'O' and game_board[1][2] == 'O':
        print("Congrats O won")
        return "O"
    elif game_board[2][0] == 'X' and game_board[2][1] == 'X' and game_board[2][2] == 'X':
        print("Congrats X won")
        return "X"
    elif game_board[2][0] == 'O' and game_board[2][1] == 'O' and game_board[2][2] == 'O':
        print("Congrats O won")
        return "O"
#code for all vertical wins since there are 3 ways to win it count 6 because of the possibility for 'X' and 'O'
    if game_board[0][0] == 'X' and game_board[1][0] == 'X' and game_board[2][0] == 'X':
        print("Congrats X won")
        return "X"
    elif game_board[0][0] == 'O' and game_board[1][0] == 'O' and game_board[2][0] == 'O':
        print("Congrats O won")
        return "O"
    elif game_board[0][1] == 'X' and game_board[1][1] == 'X' and game_board[2][1] == 'X':
        print("Congrats X won")
        return "X"
    elif game_board[0][1] == 'O' and game_board[1][1] == 'O' and game_board[2][1] == 'O':
        print("Congrats O won")
        return "O"
    elif game_board[0][2] == 'X' and game_board[1][2] == 'X' and game_board[2][2] == 'X':
        print("Congrats X won")
        return "X"
    elif game_board[0][2] == 'O' and game_board[1][2] == 'O' and game_board[2][2] == 'O':
        print("Congrats O won")
        return "O"
#code for all diagnal wins since there are 2 ways to win it counts 4 because the possibility for 'X' and 'O'
    if game_board[0][0] == 'X' and game_board[1][1] == 'X' and game_board[2][2] == 'X':
        print("Congrats X won")
        return "X"
    elif game_board[0][0] == 'O' and game_board[1][1] == 'O' and game_board[2][2] == 'O':
        print("Congrats O won")
        return "O"
    elif game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][0] == 'X':
        print("Congrats X won")
        return "X"
    elif game_board[0][2] == 'O' and game_board[1][1] == 'O' and game_board[2][0] == 'O':
        print("Congrats X won")
        return "O"
    else:
        return "Go again"

    


end_game = False
turn_counter = 0

while(end_game == False):
    if(turn_counter % 2 == 1):
        off_gameboard()
        number_choose = int(input("\nChoose a number [1-9]: "))
        if number_choose >= 1 or number_choose <= 9:
            modify_gameboard(number_choose, 'X')
            game_numbers.remove(number_choose)
        else:
            print("Wrong number. So try again")
        turn_counter += 1
    else:
        while True:
            fake_player = random.choice(game_numbers)
            print("\nFake player choice: ", fake_player)
            if fake_player in game_numbers:
                modify_gameboard(fake_player, 'O')
                game_numbers.remove(fake_player)
                turn_counter += 1
                break
    tictactoe_winner = winner_check(game_board)
    if tictactoe_winner != "Go again":
        print("\nThe game has ended! Thanks for Playing!")
        break

                
            
        
        

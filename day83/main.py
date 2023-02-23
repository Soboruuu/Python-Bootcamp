# make dictionary for each cells
game = {1: "   ",
        2: "   ",
        3: "   ",
        4: "   ",
        5: "   ",
        6: "   ",
        7: "   ",
        8: "   ",
        9: "   ",}


# make 3x3 game board
def print_board(game):
    board= f"{game[1]}|{game[2]}|{game[3]}\n" \
           f" _________\n" \
           f"{game[4]}|{game[5]}|{game[6]}\n" \
           f" _________\n" \
           f"{game[7]}|{game[8]}|{game[9]}"
    print(board)


# Player O's Turn
def o_move(game):
    omove = int(input("Choose O's move!\n"
                      "Type 1 to 9\n"))
    if check_duplicated(omove, game) == False:
        o_move(game)
    else:
        game[omove] = " O "
        check_win()


# Player X's Turn
def x_move(game):
    xmove = int(input("Choose X's move!\n"
                      "Type 1 to 9\n"))
    if check_duplicated(xmove, game) == False:
        x_move(game)
    else:
        game[xmove] = " X "
        check_win()


# Check winning values, whoever made |, /, \, - straight line first on 3x3 game board wins
def check_win():
      if game[1] == game[2] == game[3] != "   ":
            return False
      elif game[4] == game[5] == game[6] != "   ":
            return False
      elif game[7] == game[8] == game[9] != "   ":
            return False
      elif game[1] == game[4] == game[7] != "   ":
            return False
      elif game[2] == game[5] == game[8] != "   ":
            return False
      elif game[3] == game[6] == game[9] != "   ":
            return False
      elif game[1] == game[5] == game[9] != "   ":
            return False
      elif game[3] == game[5] == game[7] != "   ":
            return False


# Check if players try to put their marks on the cells which are already taken
def check_duplicated(move, game):
    if game[move] != "   ":
        print('You can not use that cell!\n'
              'Try again!')
        print_board(game)
        return False


# Check both player's turn counter. if reaches 9 without winner, game is over.
def check_count(count):
    if count < 9:
        return True
    else:
        return False


# Main game loop
def main():
    count = 0
    while check_count(count):
        print_board(game)
        o_move(game)
        count +=1
        if check_count(count) == False:
            print_board(game)
            print('Draw!')
        else:
            if check_win() == False:
                print_board(game)
                print('Game Over!')
                return
            print_board(game)
            x_move(game)
            count += 1
            if check_count(count) == False:
                print_board(game)
                print('Draw!')
                return
            else:
                if check_win() == False:
                    print('Game Over!')
                    return

print('Welcome to Tic Tac Toe Game!')
main()

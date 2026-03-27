game = [[" " for _ in range(3)] for _ in range(3)]
intro = [["T", "I", "C"],
    ["T", "A", "C"],
    ["T", "O", "E"]]


def print_grid(matrix):
    print()
    separator = ("+" + "---") * 3 + "+"
    print(separator.center(50))
    for row in matrix:
        elements = ' | '.join(map(str,row))
        print(f"| {elements} | ".center(50))
        print(separator.center(50))
    print()




def is_valid_move(matrix, row, col):
    return matrix[row][col] == " "


def is_no_move(matrix):
    return " " not in [cell for row in matrix for cell in row]
    

def mark_move(matrix, player, row, col):    
    if player == "Player 1":
        matrix[row][col] = "X"
    else:
        matrix[row][col] = "O"
        
        
#-------------checker for winner----------------
def row_checker(row):
    values = set(row)

    if len(values) != 1:
        return None

    winner = values.pop()

    if winner == " ":
        return None

    return winner


def diagonal_checker(matrix):
    size = len(matrix)

    diag1 = [matrix[i][i] for i in range(size)]
    diag2 = [matrix[i][size - 1 - i] for i in range(size)]

    for diag in (diag1, diag2):
        values = set(diag)
        if len(values) == 1:
            winner = values.pop()
            if winner != " ":
                return winner

    return None




def check_for_winner(matrix):
    for row in matrix:
        result = row_checker(row)
        if result is not None:
            return result

    for column in zip(*matrix):
        result = row_checker(column)
        if result is not None:
            return result

    result = diagonal_checker(matrix)
    if result is not None:
        return result

    return None
    


        
def prompt_move(prompt):
    while True:
        try:
            row, col = map(int, input(prompt).split(','))
        except ValueError:
            continue
        
        if 1 <= row <=3 and 1 <= col <= 3:
            return row - 1, col - 1
            


def main():  #tic-tac-toe finallyyyyyy
    print("Tic-Tac-Toe Game".center(50,"-"))
    print_grid(intro)
    print("Rules:\nPlayers must input row and column in the format (row,col)\nwhere they want to put their move\nwherein col and row should be in between 1 and 3\nExample input: 1, 2\nFirst to line up 3 components wins the game.\n")
    
    players = ["Player 1", "Player 2"]
    turn = 0
    
    while True:
        row, col = prompt_move(f"{players[turn]}'s move: ")
        current_player = players[turn]
        
        if not is_valid_move(game, row, col):
            print("Invalid move. Square already taken.")
            continue
        
        mark_move(game, players[turn], row, col)
        turn = (turn + 1) % 2
        print_grid(game)
        winner = check_for_winner(game)
        

        
        if winner is not None:
            print(f"Congratulations! Winner is {current_player}.")
            return
    
        if is_no_move(game):
            print("No winner.")
            return


if __name__ == "__main__":
    main()
import random
class Board:
    def __init__(self, name):
        self.name = name
        self.position = {}
        self.playBoard = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        # Track X's
        self.bingo = {
            "row" : [0,0,0,0,0],
            "col" : [0,0,0,0,0]
        }
        
    def createBoard(self, row, col, value):
        self.playBoard[row][col] = value
        self.position[value] = (row, col)
    
    def updateBoard(self, pos):
        if pos in self.position:
            x,y = self.position[pos]
            self.playBoard[x][y] = 'X'
            self.updateBingo(x,y)
    
    def updateBingo(self, x, y):
        # Track X's per row and col.
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1
        
    def checkBingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"]

class Game:
    def displayBoard(self, board_obj: Board):
        board = board_obj.playBoard
        
        print(board_obj.name)
        for i in range(5):
            for j in board[i]:
                if j=='X':
                    print(f" {j}",end=" ")
                elif int(j)>9:
                    print(j,end=" ")
                else:
                    print(f"0{j}",end=" ")
            print()
        print()

if __name__ == "__main__":
    game = Game()
    board_objs = []

    # Create the game boards.
    with open('2021\Day04_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        called_numbers = data[0].split(',')
        board_num = 0
        for line in data[1:]:
            # When readline returns an empty string, create a new board and resets counters.
            if line == "":
                board_row = 0
                board_num += 1
                board_obj = Board(name=(f'board{board_num}'))
                board_objs.append(board_obj)
                continue
            # When readline returns values update the board with the values.
            else:
                # Update the values on the board
                for board_col, item in enumerate(line.split()):
                    board_obj.createBoard(board_row, board_col, int(item))
                board_row += 1
            # Print the board once full
            if board_row > 4:
                game.displayBoard(board_obj)

    # Process called numbers.
    for cn in called_numbers:
        print(f'{cn} was called')
        for board_obj in board_objs:
            board_obj.updateBoard(int(cn))
            #game.displayBoard(board_obj)
            if board_obj.checkBingo():
                print(f"{board_obj.name} WON")
                break
        else:
            continue
        break

    winning_board = board_obj.playBoard
    winning_num = int(cn)
    sum_unmarked_num = 0
    for row in winning_board:
        sum_unmarked_num += sum(filter(lambda i: isinstance(i, int), row))
    print(f'Sum of all unmarked numbers: {sum_unmarked_num}')
    print(f'Last number called: {winning_num}')
    print(f'Final score: {sum_unmarked_num * winning_num}')
    
        # if player1.checkBingo() and player2.checkBingo():
        #     print("DRAW")
        #     break
        
            
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.curent_winner = None 

    def print_board(self):
        for row in [self.board[i*3:(1+1)*3] for i in range(3)]:
            print("| " + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        pass
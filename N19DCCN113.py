# N19DCCN113-Đinh Nho Nam
# N19DCCN090-Phạm Văn Khánh
# N19DCCN031-Trần Nhật Duy
#cách chạy và sử dụng chương trình 
# Bước 1 cài đặt thư viện graphics nhập câu lệnh vào terminal : pip install graphics
# Bước 2 run chương trình
import sys
import graphics as g

class TicTacToe:
    def __init__(self, win_size=300):
        self.win = g.GraphWin("Tic-Tac-Toe", win_size, win_size)
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.turn = 'X'
        self.moves_left = 9
        self.buttons = []
        self.winning_combs = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)],
        ]
    # vẽ bản 3 x 3 và thể hiện X O của người và máy
    def draw_board(self):
        for i in range(3):
            for j in range(3):
                button = g.Rectangle(g.Point(i*100, j*100), g.Point(i*100+100, j*100+100))
                button.draw(self.win)
                self.buttons.append(button)
    #vẽ dấu X và O
    def display_move(self, row, col):
        center = g.Point(col*100 + 50, row*100 + 50)
        label = g.Text(center, self.turn)
        label.draw(self.win)
    #thuật toán MINIMAX và phương phát cắt tỉa alpha- beta
    def minimax(self, depth, alpha, beta, isMaximizing):
        result = self.check_winner()
        if result == 'X':
            return 10 - depth
        elif result == 'O':
            return depth - 10
        elif result == 'tie':
            return 0
        if isMaximizing:
            bestVal = -sys.maxsize
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        value = self.minimax(depth + 1, alpha, beta, False)
                        self.board[i][j] = ' '
                        bestVal = max(bestVal, value)
                        alpha = max(alpha, bestVal)
                        if beta <= alpha:
                            break
            return bestVal
        else:
            bestVal = sys.maxsize
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        value = self.minimax(depth + 1, alpha, beta, True)
                        self.board[i][j] = ' '
                        bestVal = min(bestVal, value)
                        beta = min(beta, bestVal)
                        if beta <= alpha:
                            break
            return bestVal
    #sử dụng thuật toán minimax để xác định nước đi tốt nhất cho máy
    def best_move(self):
        bestVal = -sys.maxsize
        row = -1
        col = -1
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'X'
                    moveVal = self.minimax(0, -sys.maxsize, sys.maxsize, False)
                    self.board[i][j] = ' '
                    if moveVal > bestVal:
                        row = i
                        col = j
                        bestVal = moveVal
        return row, col
    #kiểm tra thắng thua
    def check_winner(self):
        
        for comb in self.winning_combs:
            if (self.board[comb[0][0]][comb[0][1]] == self.board[comb[1][0]][comb[1][1]] == self.board[comb[2][0]][comb[2][1]]) and (self.board[comb[0][0]][comb[0][1]] != ' '):
                return self.board[comb[0][0]][comb[0][1]]
        if self.moves_left == 0:
            return 'tie'
        return None
    #vòng lặp game
    def play_game(self):
        self.draw_board()
        while True:
            if self.turn == 'X':
                move = self.win.getMouse()
                print(self.board)
                col =int( move.getX() // 100)
                row = int(move.getY() // 100)
                if self.board[row][col] == ' ':
                    self.display_move(row, col)
                    self.board[row][col] = self.turn
                    self.turn = 'O'
                    self.moves_left -= 1
                winner = self.check_winner()
                if winner or self.moves_left == 0:
                    if winner == 'tie':
                        # g.setTextColor("black")
                        # setTextColor(color)  # sets the text color
                        g.Text(g.Point(150, 135), 'Hòa').draw(self.win)
                    else:
                       
                        g.Text(g.Point(150, 135), winner + ' Chiến Thắng').draw(self.win)
                    break
            else:
                row, col = self.best_move()
                self.display_move(row, col)
                self.board[row][col] = self.turn
                self.turn = 'X'
                self.moves_left -= 1
                winner = self.check_winner()
                if winner or self.moves_left == 0:
                    if winner == 'tie':
                        g.Text(g.Point(150, 135), 'Hòa').draw(self.win)
                    else:
                        g.Text(g.Point(150, 135), winner + '  Chiến Thắng').draw(self.win)
                    break
        self.win.getMouse()
        self.win.close()

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
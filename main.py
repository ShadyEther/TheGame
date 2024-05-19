
class TicTactoe():

    

    def create_board(self):
        self.board=[]
        for i in range(3):
            row=[]
            for j in range(3):
                row.append(-1)
            self.board.append(row)

    def __init__(self,**kwargs):
        self.create_board()
        self.player1="X"
        self.player2="O"
        pass

    

    def display_screen(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]==0:
                    print(self.player1,end=" ")
                elif self.board[i][j]==1:
                    print(self.player2,end=" ")
                else:
                    print("@",end=" ")
            print()

    def take_input(self):
        x,y=map(int,input().split())
        if x < 3 and y < 3 and self.board[x][y]==-1:
            return x,y
        else:
            return [3,3]
            
    def update_board(self,x,y,player):
        if self.board[x][y] ==-1:
            self.board[x][y]=player
            return True
        else:
            return False

    
    def check_win(self):
        # check rows and cols and diagonals for same values
        for row in self.board:
            if row[0]==row[1]==row[2]!=-1: #ch3ck rows
                return row[0]
        for col in range(3):
            if self.board[0][col]==self.board[1][col]==self.board[2][col]!=-1: #check cols
                return self.board[0][col]
        if self.board[0][0]==self.board[1][1]==self.board[2][2]!=-1:#chec left diagonal
            return self.board[0][0]
        if  self.board[0][2]==self.board[1][1]==self.board[2][0]!=-1:#check right diagonal
            return self.board[0][2]
        return -1


    def game_loop(self):
        # TODO: takeinput
        turn=0
        totalturns=0
        while(totalturns<8):
            self.display_screen()
            print("Player",turn+1,"'s Turn")
            input=self.take_input()
            if input[0]!=3 and input[1]!=3:
                if self.update_board(input[0],input[1],turn):
                    winner=self.check_win()
                    if winner != -1:
                        print("winner is Player: ",winner)
                        break
                    else:
                        if totalturns>=7:
                            print("Match is tied")
                        else:
                            turn=not(turn)
                            totalturns+=1
                            # proceed  with next turn
                else:
                    print("That position is already filled")
            else:
                print("Invalid input! Enter between {0, 1, 2}")
                 
            # takeinpput again





if __name__=="__main__":
    game_obj=TicTactoe()
    print(game_obj.board)
    game_obj.game_loop()






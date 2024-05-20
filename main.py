
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

    def update_board(self,x,y,player):
        self.board[x][y]=player

    def take_input(self):
        while True:
            x,y=map(int,input("Enter Your position like x,y within range [0,1,2]: ").split())
            if 0<=x<3 and 0<=y<3 and self.board[x][y]==-1:
                return x,y
            print("Invalid Input! Choose an avaliable coordinate!")     
    

    
    def check_win(self):
        # check rows and cols and diagonals for same values
        for _ in range(3):
            if self.board[_][0]==self.board[_][1]==self.board[_][2]!=-1:
                return self.board[_][0]
            if self.board[0][_]==self.board[1][_]==self.board[2][_]!=-1: #check cols
                return self.board[0][_]

        if self.board[0][0]==self.board[1][1]==self.board[2][2]!=-1:#chec left diagonal
            return self.board[0][0]
        if  self.board[0][2]==self.board[1][1]==self.board[2][0]!=-1:#check right diagonal
            return self.board[0][2]
        return -1


    def game_loop(self):
        # TODO: takeinput
        turn=0
        totalturns=0
        self.display_screen()
        while(totalturns<9):
            print("Player",turn+1,"'s Turn")
            input=self.take_input()
            self.update_board(input[0],input[1],turn)
            self.display_screen()
            winner=self.check_win()
            if winner != -1:
                print("winner is Player: ",winner)
                break
            else:
                if totalturns>=8:
                    print("Match is tied")
                else:
                    turn=not(turn)
                    totalturns+=1             
            # takeinpput again





if __name__=="__main__":
    game_obj=TicTactoe()
    print(game_obj.board)
    game_obj.game_loop()






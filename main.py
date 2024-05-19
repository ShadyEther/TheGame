
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
        pass

    def take_input(self):
        x,y=map(int,input().split())
        return x,y

    
    def check_win(self):
        pass

    def check_tie(self):
        pass

    def restart(self):
        pass


    def game_loop(self):
        # TODO: takeinput
        # TODO: Validate it
        # TODO: Check win
        # TODO: Check Tie
        # restart
        input=self.take_input()
        print(input)





if __name__=="__main__":
    game_obj=TicTactoe()
    print(game_obj.board)
    game_obj.game_loop()





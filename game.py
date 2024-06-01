from chessboard import chessboard
from minimax import minimax
from optimize_MMT import optimize_MMT

class MMT_to_MMT():
    def displacement(self, para):

        return [para]

    def train_MMT_MMT(self, Parameter0, Parameter1):
        # create nearby points
        Para0 = self.displacement(Parameter0)
        
        win_rate = []
        para1 = Parameter1
        for para0 in Para0:          
            '''
            battle para0 with para1,
            and get win rate of para0
            '''
            mmx = minimax()
            # play 200 rounds
            WIN = 0
            ROUND = 100
            for round in range(ROUND):
                board = chessboard()
                for i in range(10000):
                    if board.isWin() or board.isLose():
                        break
                    elif (i+round)%2 == 0:
                        board = mmx.Next_state(board, para0)
                    else:
                        board = mmx.Next_state(board, para1)
                    board.display()
                if (board.isWin() and (i+round)%2 == 0) or (board.isLose() and (i+round)%2 == 1):
                    WIN += 1
            win_rate.append(WIN/ROUND)
        return optimize_MMT.optimize(Para0, win_rate)

class RL_to_MMT():
    def train_RL_MMT(PARA):
        
        return 

if __name__ == "__main__":
    
    # train origin minimax machine
    para0 = [1,2,3,3,2,1]
    para1 = [3,2,1,1,2,3]
    mmt_mmt = MMT_to_MMT()
    for _ in range(1):
        new_para = mmt_mmt.train_MMT_MMT(para0, para1)
        para1 = para0
        para0 = new_para
        
        # new->0, 0->1, 1->2
    
    # train RL machine
    # MMT_PARA = para0
    # for _ in range(10):
    #     new_para = RL_to_MMT.train_RL_MMT(MMT_PARA)
    
        
    
                
        
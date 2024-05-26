from chessboard import chessboard
from minimax import minimax
from optimize_MMT import optimize_MMT

class MMT_to_MMT():
    def displacement(self, para):

        return []

    def train_MMT_MMT(self, Parament0, Parament1):
        
        Para0 = self.displacement(Parament0)
        
        result = []
        for para0 in Para0:
            para1 = Parament1
            
            # battle para0 with para1
            # and get win rate of para0
            # begin LIN
            
            # end
            
            result.append(1)
        
        return optimize_MMT.optimize(Para0, result)

class RL_to_MMT():
    def train_RL_MMT(PARA):
        
        return 

if __name__ == "__main__":
    
    # train origin minimax machine
    para0 = para1 = []
    for _ in range(10):
        new_para = MMT_to_MMT.train_MMT_MMT(para0, para1)
        para1 = para0
        para0 = new_para
    
    # train RL machine
    MMT_PARA = para0
    for _ in range(10):
        new_para = RL_to_MMT.train_RL_MMT(MMT_PARA)
        
    
                
        
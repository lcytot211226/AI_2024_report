from chessboard import chessboard
from minimax import minimax
from optimize_MMT import optimize_MMT
import argparse
from RL import *
from tqdm import tqdm
import random

class MMT_to_MMT():
    def displacement(self, para):
        # h = 2
        S = []
        for _ in range(16):
            rand_para = []
            for p in para:
                rand_para.append(p+random.uniform(-2, 2)) 
            S.append(rand_para)
        
        return S

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
            ROUND = 1
            for round in range(ROUND):
                board = chessboard()
                for i in range(10000):
                    if board.isWin() or board.isLose():
                        break
                    elif (i+round)%2 == 0:
                        board = mmx.Next_state(board, para0)
                    else:
                        board = mmx.Next_state(board, para1)
                    #board.display(action, board.state)
                if (board.isWin() and (i+round)%2 == 0) or (board.isLose() and (i+round)%2 == 1):
                    WIN += 1
            win_rate.append(WIN/ROUND)
        return optimize_MMT.optimize(Para0, win_rate)

def train1():
    print("Training 1 is running")
    para0 = [1,2,3,3,2,1]
    para1 = [3,2,1,1,2,3]
    mmt_mmt = MMT_to_MMT()
    for _ in tqdm(range(1)):
        new_para = mmt_mmt.train_MMT_MMT(para0, para1)
        para1 = para0
        para0 = new_para
    return new_para
    
        
def train2(para):
    print("Training 2 is running")
    train_RL(color=0, episode=100, para=para)
    
    
def play():
    print("loading...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run functions.")
    parser.add_argument('--train', action='store_true', help='Run training')
    parser.add_argument('--play', action='store_true', help='playplayplay')
    
    args = parser.parse_args()

    if args.train:
        para = train1()
        print(para)
        train2(para)
    if args.play:
        play()
        
    
        
    
                
        
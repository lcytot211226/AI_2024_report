import matplotlib.pyplot as plt
import copy

class chessboard():
    all_posi = {
        (0, 0), (0, 3), (0, 6), (1, 1), (1, 3), (1, 5), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6),
        (6, 0), (6, 3), (6, 6), (5, 1), (5, 3), (5, 5), (4, 2), (4, 3), (4, 4)
    }
    def __init__(self):
        self.state = [set(),set()] # [ black, white ]
        self.round = 0
        self.lose = False
        self.win  = False
        self.used_posi = []
    
    def get_Action(self):
        '''
        input : color(0/1), round
        output: actions
        '''
        
        color = self.round % 2
        
        # unused position
        unused_posi = self.all_posi - self.used_posi
                
        # put/move chess and maybe remove other chess
        actions = [] # action = [ add, remove ], add={(x,y,color),...}
        if len(self.state[color]) == 3: # there's only 3 chesses
            for movefrom in self.state[color]:
                for moveto in unused_posi:
                    if(self.is_line(movefrom, moveto)):
                        for remove in self.state[1-color]:
                            actions.append([{(moveto[0],moveto[1],color)},
                                            {(movefrom[0],movefrom[1],color), (remove[0],remove[1],1-color)}])
                    else:
                        actions.append([{(moveto[0],moveto[1],color)},
                                        {(movefrom[0],movefrom[1],color)}])
        elif round < 18: # place stage
            action = [[],[]]
        else:             # normal stage
            action = [[],[]]
            
        return actions
    
    def get_NextState(self, action): 
        # input : color, action, round
        # output: next_chessboard
        
        color = self.round % 2
        
        next_chessboard = copy.deepcopy(self)
        for x,y,color in action[0]:
            next_chessboard.state[color].add((x,y))
            next_chessboard.used_posi.add((x,y))
        
        for x,y,color in action[1]:
            next_chessboard.state[color].remove((x,y))
            next_chessboard.used_posi.remove((x,y))
        
        
        
        
        return []

    def isLose(self):
        return self.lose
    
    def isWin(self):
        return self.win
    
    def is_line(self, movefrom, moveto):
        return False
    
    def append(self, x, y, color):
        # ONLY FOR TEST, DON'T USE
        return
    
    
    def display(self):
        return 

'''

following is game rule:

size       = 7*7
left-up    = (0,0)
right-down = (6,6)

black has high priority

'''

if __name__ == "__main__":
    board = chessboard()
    board.display()
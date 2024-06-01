import matplotlib.pyplot as plt
import copy
import math

class chessboard():
    all_posi = [
        (0, 0), (0, 3), (0, 6), (1, 1), (1, 3), (1, 5), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6),
        (6, 0), (6, 3), (6, 6), (5, 1), (5, 3), (5, 5), (4, 2), (4, 3), (4, 4)
    ]
    
    def __init__(self):
        self.state = [set(),set()] # [ black, white ]
        self.round = 0
        self.chase_time = 0
        self.lose = False
        self.win  = False
        self.used_posi = set()
        self.unused_posi = set(self.all_posi)
    
    def get_Action(self):
        '''
        input : 
        output: actions
        '''
        
        color = self.round % 2
        
        # unused position
                
        # put/move chess and maybe remove other chess
        actions = set() # action = ( add, remove ), add={(x,y,color),...}
        
        if self.round < 18:
            # place stage
            for add in self.unused_posi:
                ADD = (add[0], add[1], color)
                
                # enter eat stage or not
                if self.get_NextState(({ADD}, set())).in_line(ADD):
                    REMOVE_list = []
                    for remove in self.state[1-color]:
                        REMOVE = (remove[0], remove[1], 1-color)
                        if not self.get_NextState(({ADD}, set())).in_line(REMOVE):
                            REMOVE_list.append(REMOVE)
                            
                    if len(REMOVE_list) == 0:
                        actions.add( (frozenset({ADD}), frozenset()) )
                    else:
                        for REMOVE in REMOVE_list:
                            actions.add( (frozenset({ADD}), frozenset({REMOVE})) )
                else:
                    actions.add( (frozenset({ADD}), frozenset()) )
                    
        else:
            # normal stage
            for movefrom in self.state[color]:
                moveto_set = self.__where_to_move(movefrom)
                # print(moveto_set)
                for moveto in moveto_set:
                    MOVETO = (moveto[0], moveto[1], color)
                    MOVEFROM = (movefrom[0], movefrom[1], color)
                    
                    # enter eat stage or not
                    if self.get_NextState( ({MOVETO}, {MOVEFROM}) ).in_line(MOVETO):
                        REMOVE_list = []
                        for remove in self.state[1-color]:
                            REMOVE = (remove[0], remove[1], 1-color)
                            if not self.get_NextState( ({MOVETO}, {MOVEFROM}) ).in_line(REMOVE):
                                REMOVE_list.append(REMOVE)
                                
                        if len(REMOVE_list) == 0:
                            actions.add( (frozenset({MOVETO}), frozenset({MOVEFROM})) )
                        else:
                            actions.add( (frozenset({MOVETO}), frozenset({MOVEFROM, REMOVE})) )
                    else:
                        actions.add( (frozenset({MOVETO}), frozenset({MOVEFROM})) )
        if len(actions) == 0:
            self.lose = True
        return actions
    
    def get_NextState(self, action): 
        # input : action
        # output: next_chessboard
        
        next = copy.deepcopy(self)
        for x,y,color in action[0]:
            next.state[color].add((x,y))
            next.used_posi.add((x,y))
            next.unused_posi.remove((x,y))
        
        for x,y,color in action[1]:
            next.state[color].remove((x,y))
            next.used_posi.remove((x,y))
            next.unused_posi.add((x,y))
        
        next.round += 1
        color = next.round % 2
        
        if next.round >= 18:
            if len(action[1]) >= 2:
                next.chase_time = 0
            else:
                next.chase_time += 1
            
            if next.chase_time >= 20:
                next.win =  len(next.state[color]) > len(next.state[1-color])
                next.lose = not next.win
            elif len(action[0])+len(action[1]) == 0:
                next.lose = True
            elif len(next.state[color]) <= 3:
                next.lose = True
            elif len(next.state[1-color]) <= 3:
                next.win  = True
                
        return next

    def isLose(self):
        return self.lose
    
    def isWin(self):
        return self.win
    
    def in_line(self, posi):
        x, y, color = posi
        
        i = 3-abs(3-x)
        if x != 3:
            if (x,i) in self.state[color] and (x,3) in self.state[color] and (x,6-i) in self.state[color]:
                return True
        elif y < 3:
            if (x,0) in self.state[color] and (x,1) in self.state[color] and (x,2) in self.state[color]:
                return True
        else:
            if (x,4) in self.state[color] and (x,5) in self.state[color] and (x,6) in self.state[color]:
                return True
            
        j = 3-abs(3-y)
        if y != 3:
            if (j,y) in self.state[color] and (3,y) in self.state[color] and (6-j,y) in self.state[color]:
                return True
        elif x < 3:
            if (0,y) in self.state[color] and (1,y) in self.state[color] and (2,y) in self.state[color]:
                return True
        else:
            if (4,y) in self.state[color] and (5,y) in self.state[color] and (6,y) in self.state[color]:
                return True
        return False
    
    def __where_to_move(self, point):
        x, y = point
        points = []
        
        i = 3-abs(3-x)
        if x != 3:
            if y == 3:
                if (x,i) not in self.used_posi: 
                    points.append((x,i))
                if (x,6-i) not in self.used_posi:
                    points.append((x,6-i))
            else:
                 if (x,3) not in self.used_posi: 
                    points.append((x,3))
        else:
            if abs(3-y) == 2:
                if (x,y-1) not in self.used_posi: 
                    points.append((x,y-1))
                if (x,y+1) not in self.used_posi:
                    points.append((x,y+1))
            elif y < 3:
                if (x,1) not in self.used_posi:
                    points.append((x,1))
            else:
                if (x,5) not in self.used_posi:
                    points.append((x,5))
                
        j = 3-abs(3-y)
        if y != 3:
            if x == 3:
                if (j,y) not in self.used_posi:
                    points.append((j,y))
                if (6-j,y) not in self.used_posi:
                    points.append((6-j,y))
            else:
                 if (3,y) not in self.used_posi:
                    points.append((3,y))
        else:
            if abs(3-x) == 2:
                if (x-1,y) not in self.used_posi: 
                    points.append((x-1,y))
                if (x+1,y) not in self.used_posi:
                    points.append((x+1,y))
            elif x < 3:
                if (1,y) not in self.used_posi:
                    points.append((1,y))
            else:
                if (5,y) not in self.used_posi:
                    points.append((5,y))    
                    
        return points
    
    def append(self, x, y, color):
        # ONLY FOR TEST, DON'T USE
        return
    
    
    def display(self, action, state):
        
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('saddlebrown')
        ax.set_facecolor('saddlebrown')
        
        # draw board
        for i in range(3):
            ax.plot([i,i], [i,6-i], color='white', zorder=1)
            ax.plot([i,6-i], [6-i,6-i], color='white', zorder=1)
            ax.plot([6-i,6-i], [6-i,i], color='white', zorder=1)
            ax.plot([6-i,i], [i,i], color='white', zorder=1)
        ax.plot([3, 3], [0, 2], color='white', zorder=1)
        ax.plot([3, 3], [4, 6], color='white', zorder=1)
        ax.plot([0, 2], [3, 3], color='white', zorder=1)
        ax.plot([4, 6], [3, 3], color='white', zorder=1)
        ax.set_xlim(-1, 7)
        ax.set_ylim(-1, 7)
        ax.set_xticks(range(7))
        ax.set_yticks(range(7))
        ax.axis('off')
        
        plt.title(action)


        # mark chess
        for i in range(2):
            color = 'black' if i==0 else 'white'
            for y,x in self.state[i]:  
                marker = 'o'
                size = 600
                ax.scatter(x, 6-y, color=color, marker=marker, s=size, zorder=2)
                    

        # display
        plt.gca().set_aspect('equal', adjustable='box')
        import os
        save_dir = 'picture'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        file_path = os.path.join(save_dir, f'frame_{self.round:03d}.png')
        plt.savefig(file_path)
        # plt.show()
        plt.close(fig)

'''

following is game rule:

size       = 7*7
left-up    = (0,0)
right-down = (6,6)

black has high priority

'''

if __name__ == "__main__":
    board = chessboard()
    while True:
        if board.isLose() or board.isWin() or board.round>=100:
            break
        else:
            actions = list(board.get_Action())
            board = board.get_NextState(actions[0])
            board.display()
    
    if (board.round %2 == 0 and board.win) or (board.round %2 == 1 and board.lose):
        print("black win")
    else:
        print("white win")
class chessboard():

    def __ini__(self):
        self.state = [[],[]] # [ black, white ]
        return 0
    
    def get_Action(self, color):
        # input : color
        # output: actions
        return []
    
    def get_NextState(self, color, action): 
        # input : color, action
        # output: state
        return []
    
    def display(self):
        return 

'''

following is game rule:

size       = 7*7
left-up    = (0,0)
right-down = (6,6)

black has high priority

'''
class minimax():
    '''
    state:
    state.state = [set(),set()] # [ black, white ]
    state.round 
    state.get_Action()
    state.get_NextState(action)
    state.isLose()
    state.isWin()
    '''
    
    def Next_state(self, state, parameter): 
        '''
        input : state, parameter
        output: next_state
        (state: chessboard)
        '''
        # 
        import random
        actions = list(state.get_Action())
        next_state = state.get_NextState(actions[random.randint(0,len(actions)-1)])
        return next_state
    
    def get_value(self, state, parameter):
        '''
        input : state, parameter
        output: value
        (state: chessboard)
        para = [num_black, num_white, eat, ate, black_line, white_line]
        '''
        
        return 1
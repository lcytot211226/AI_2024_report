class minimax():
    def Next_state(self, state): 
        '''
        input : state
        output: next_state
        (state: chessboard)
        '''
        # 
        
        next_state = state
        return next_state
    
    def get_value(self, state, parameter):
        '''
        input : state, parameter
        output: value
        (state: chessboard)
        para = [num_black, num_white, eat, ate, black_line, white_line]
        '''
        
        return 1
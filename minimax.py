# -*- coding: utf-8 -*-
from chessboard import chessboard
import random

class minimax():
    '''
    state:
    state.state = [set(), set()] # [ black, white ]
    state.round
    state.get_Action()
    state.get_NextState(action)
    state.isLose()
    state.isWin()
    '''

    def Next_state(self, state, parameter, alpha=-float('inf'), beta=float('inf'), depth=3):
        '''
        input : state, parameter
        output: next_state
        '''
        if state.isWin() or state.isLose() or depth == 0:
            return state

        actions = state.get_Action()
        best_value = -float('inf')
        best_actions = []

        for action in actions:
            next_state = state.get_NextState(action)
            value = self.__minimax(next_state, parameter, alpha, beta, depth - 1, state.round % 2)
            if value > best_value:
                best_value = value
                best_actions = [action]
            elif value == best_value:
                best_actions.append(action)

        if not best_actions:
            return state

        best_action = random.choice(best_actions)
        return state.get_NextState(best_action), best_action

    def __minimax(self, state, parameter, alpha, beta, depth, current_player_color):
        if state.isWin() or state.isLose() or depth == 0:
            return self.__get_value(state, parameter)

        actions = state.get_Action()
        if state.round % 2 == current_player_color:  
            value = -float('inf')
            for action in actions:
                next_state = state.get_NextState(action)
                value = max(value, self.__minimax(next_state, parameter, alpha, beta, depth - 1, current_player_color))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float('inf')
            for action in actions:
                next_state = state.get_NextState(action)
                value = min(value, self.__minimax(next_state, parameter, alpha, beta, depth - 1, current_player_color))
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value

    def __get_value(self, state, parameter):
        '''
        input : state, parameter
        output: value
        (state: chessboard)
        para = [num_black, num_white, eat, ate, black_line, white_line]
        '''
        if len(parameter) != 6:
            raise ValueError("Parameter length must be 6")

        num_black = len(state.state[0])
        num_white = len(state.state[1])
        eat = self.__count_eat(state, 0)
        ate = self.__count_eat(state, 1)
        black_line = self.__count_lines(state, 0)
        white_line = self.__count_lines(state, 1)

        features = [num_black, num_white, eat, ate, black_line, white_line]
        value = sum(p * f for p, f in zip(parameter, features))

        return value

    def __count_eat(self, state, color):

        eat_count = 0
        for posi in state.state[color]:
            posic = (posi[0], posi[1], 1 - color)
            if state.in_line(posic):
                eat_count += 1
        return eat_count

    def __count_lines(self, state, color):

        line_count = 0
        for posi in state.state[color]:
            posic = (posi[0], posi[1], color)
            if state.in_line(posic):
                line_count += 1
        return line_count

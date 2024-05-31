from chessboard import chessboard
from minimax import minimax
from RL import RL

if __name__ == "__main__":
    agents = [RL(), minimax()]
    board = chessboard()
    board.display()
    while not(board.isWin() or board.isLose()):
        board = agents[board.round % 2].Next_state(state = board, parameter=None)
        board.display()
    
    import convert_pic
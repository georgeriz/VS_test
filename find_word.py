import copy

def get_next(ip, size_i, size_j):
    options = [(ip[0]+i,ip[1]+j) for i in [-1,0,1] for j in [-1,0,1]]
    return filter(lambda p: p[0]!=-1 and p[1]!=-1 and p[0]!=size_i and p[1]!=size_j, options)

def find_word(board, word):
    tmp_board = copy.deepcopy(board)
    def foo(board, word, x, y):
        if board[x][y] != word[0]: return False
        if len(word) == 1: return True
        tmp = board[x][y]
        board[x][y] = "-"
        for p in get_next((x,y), len(board), len(board[0])):
            if foo(board, word[1:], p[0], p[1]): return True
            
        else: 
            board[x][y] = tmp
            return False
    return any(foo(tmp_board, word, i, j) for i in range(len(board)) for j in range(len(board[0])))



testBoard = [
  ["E","A","R","A"],
  ["N","L","E","C"],
  ["I","A","I","S"],
  ["B","Y","O","R"]
]



assert( find_word(testBoard, "C"               ))
assert( find_word(testBoard, "EAR"             ))
assert( not find_word(testBoard, "EARS"            ))
assert( find_word(testBoard, "BAILER"          ))
assert( find_word(testBoard, "RSCAREIOYBAILNEA"))
assert( not find_word(testBoard, "CEREAL"          ))
assert( not find_word(testBoard, "ROBES"           ))
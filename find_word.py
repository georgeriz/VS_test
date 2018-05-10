import copy

def get_next(ip, size_i, size_j):
    alist = []
    if ip[0] - 1 >= 0:
        alist.append((ip[0] - 1, ip[1]))
        if ip[1] - 1 >= 0:
            alist.append((ip[0] - 1, ip[1] - 1))
        if ip[1] + 1 <= size_j - 1:
            alist.append((ip[0] - 1, ip[1] + 1))
    if ip[0] + 1 <= size_i - 1:
        alist.append((ip[0] + 1, ip[1]))
        if ip[1] - 1 >= 0:
            alist.append((ip[0] + 1, ip[1] - 1))
        if ip[1] + 1 <= size_j - 1:
            alist.append((ip[0] + 1, ip[1] + 1))
    if ip[1] - 1 >= 0:
        alist.append((ip[0], ip[1] - 1))
    if ip[1] + 1 <= size_i - 1:
        alist.append((ip[0], ip[1] + 1))
    return alist

def foo(ip, board, word):
    for letter in word:
        #print "looking for:" , letter
        #print board
        for pp in get_next(ip, len(board), len(board[0])):
            #print pp
            if board[pp[0]][pp[1]] == letter:
                if len(word) == 1:
                    return True
                tmp = board[pp[0]][pp[1]]
                board[pp[0]][pp[1]] = '-'
                if foo(pp, board, word[1:]):
                    return True
                board[pp[0]][pp[1]] = tmp
        else:
            #print "did not find:", letter
            return False


def find_word(board, word):
    #print "Now starting for:", word
    tmp_board = copy.deepcopy(board)
    for i, line in enumerate(tmp_board):
        for j, char in enumerate(line):
            if char == word[0]:
                if len(word) == 1:
                    return True
                tmp = char
                tmp_board[i][j] = '-'
                if foo((i,j), tmp_board, word[1:]):
                    return True
                tmp_board[i][j] = tmp
    return False





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
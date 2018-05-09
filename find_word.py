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
        print "looking for:" , letter
        for pp in get_next(ip, len(board), len(board[0])):
            print pp
            if board[pp[0]][pp[1]] == letter:
                if len(word) == 1:
                    return True
                if foo(pp, board, word[1:]):
                    return True
        else:
            print "did not find:", letter
            return False


def find_word(board, word):
    for i, line in enumerate(board):
        for j, char in enumerate(line):
            if char == word[0]:
                if len(word) == 1:
                    return True
                if foo((i,j), board, word[1:]):
                    return True
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
##assert( not find_word(testBoard, "CEREAL"          ))
assert( not find_word(testBoard, "ROBES"           ))
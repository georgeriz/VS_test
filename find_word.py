def find_word(board, word):
    return False





testBoard = [
  ["E","A","R","A"],
  ["N","L","E","C"],
  ["I","A","I","S"],
  ["B","Y","O","R"]
]



assert( find_word(testBoard, "C"               ))
assert( find_word(testBoard, "EAR"             ))
assert( find_word(testBoard, "EARS"            ))
assert( find_word(testBoard, "BAILER"          ))
assert( find_word(testBoard, "RSCAREIOYBAILNEA"))
assert( find_word(testBoard, "CEREAL"          ))
assert( find_word(testBoard, "ROBES"           ))
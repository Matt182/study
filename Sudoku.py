def done_or_not(board): #board[i][j]
  # your solution here
  # ..
  # return 'Finished!'
  # ..
  # or return 'Try again!'
  # ..
  # search for mistake in rows and columns:
  numb = []
  for i in board:
      if len(set(i)) < len(i):
          return 'Try again!'
  for i in range(0,len(board[0])):
      for j in range(0,len(board[0])):
          numb.append(j)
      if len(set(numb)) < len(board[0]):
          return 'Try again!'
      numb = []
  #search for mistake in quads 3x3:
  
  return 'Finished!'

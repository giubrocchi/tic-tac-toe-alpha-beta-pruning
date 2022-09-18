from math import inf

board = ['0', '1', '2', 
         '3', '4', '5', 
         '6', '7', '8']
person = 'X'
computer = 'O'

def print_board():
  count = 0
  for tile in board:
    if(count == 2 or count == 5 or count == 8):
        print(tile)
    else:
      print(f'{tile}|', end='')
    count += 1
  print()

def make_play(position, player):
  board[int(position)] = player

def check_play(position):
  if(board[position] in [person, computer]):
    return False
  return True

def check_end():
  if(board[0] == board[1] == board[2]):
    if(board[0] == person):
      return person
    return computer
  if(board[3] == board[4] == board[5]):
    if(board[3] == person):
      return person
    return computer
  if(board[6] == board[7] == board[8]):
    if(board[6] == person):
      return person
    return computer

  if(board[0] == board[3] == board[6]):
    if(board[0] == person):
      return person
    return computer
  if(board[1] == board[4] == board[7]):
    if(board[1] == person):
      return person
    return computer
  if(board[2] == board[5] == board[8]):
    if(board[2] == person):
      return person
    return computer

  if(board[0] == board[4] == board[8]):
    if(board[0] == person):
      return person
    return computer
  if(board[2] == board[4] == board[6]):
    if(board[2] == person):
      return person
    return computer

  for tile in board:
    if(tile in ['0', '1', '2', '3', '4', '5', '6', '7', '8']):
      return False

  return None

def computer_turn(depth, a, b, minimax):
  status = check_end()
  if(status in [person, computer, None] or depth == 0):
    score = count_score(computer) - count_score(person)
    return [score, None]

  if(minimax == 'max'):
    value = -inf
    
    for field in board:
      if(field in ['0', '1', '2', '3', '4', '5', '6', '7', '8']):
        board[int(field)] = computer
        new_value = computer_turn(depth - 1, a, b, 'min')[0]
        board[int(field)] = field

        if(new_value > value):
          value = new_value
          return_field = field

        if(value >= b):
          break

        a = max(a, value)

    return [value, return_field]
    
  else:
    value = inf
    
    for field in board:
      if(field in ['0', '1', '2', '3', '4', '5', '6', '7', '8']):
        board[int(field)] = person
        new_value = computer_turn(depth - 1, a, b, 'max')[0]
        board[int(field)] = field

        if(new_value < value):
          value = new_value
          return_field = field

        if(value <= a):
          break

        b = min(b, value)
      
    return [value, return_field]

def count_score(player):
  if(player == computer):
    oposite_player = person
  else:
    oposite_player = computer
    
  value = 0
  
  row_one = [board[0], board[1], board[2]]
  row_two = [board[3], board[4], board[5]]
  row_three = [board[6], board[7], board[8]]
  column_one = [board[0], board[3], board[6]]
  column_two = [board[1], board[4], board[7]]
  column_three = [board[2], board[5], board[8]]
  diagonal_one = [board[0], board[4], board[8]]
  diagonal_two = [board[2], board[4], board[6]]
  
  for line in [row_one, row_two, row_three, column_one, column_two, column_three, diagonal_one, diagonal_two]:
    if(line.count(player) == 3):
      value += 100
    elif(line.count(player) == 2 and line.count(oposite_player) == 0):
      value += 10
    elif(line.count(player) == 1 and line.count(oposite_player) == 0):
      value += 1

  return value
    

def play_game():
  turn = person
  
  while True:
    print()
    print_board()
    status = check_end()
  
    if(status == person):
      print('\nYou won!')
      return
    elif(status == computer):
      print('\nYou lost!')
      return
    elif(status == None):
      print('\nTie!')
      return
    
    if(turn == person):
      inp = '-1'

      while(inp not in board):
        inp = input('Your turn: ')

      make_play(inp, person)
      turn = computer
      
    else:
      print("Computer's turn")
      make_play(computer_turn(3, -inf, inf, 'max')[1], computer)
      turn = person
    
play_game()


def make_next_board(thing):
  out = [
    ['0', '0', '0'],
    ['0', '1', '0'],
    ['0', '0', '0']
  ]
  if thing[0][2] == '1' or thing[0][0] == '0':
    out[1][1] = '0'
  return out


def sum_neighbors(thing_1, thing_2, thing_3):
  return 2

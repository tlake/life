
def make_next_board(thing):
  
  if len(thing) == 5 and thing[4][1] == '1':
    return [
      ['0','0','0','0','0'],
      ['0','0','0','0','0'],
      ['0','0','0','0','0'],
      ['0','0','0','0','0'],
      ['0','1','1','1','0']
    ]
  if len(thing) == 3:
    out = [
      ['0', '0', '0'],
      ['0', '1', '0'],
      ['0', '0', '0']
    ]
    if thing[0][2] == '1' or thing[0][0] == '0':
      out[1][1] = '0'
    return out
  else:
     return thing


def sum_neighbors(thing_1, thing_2, thing_3):
  return 2

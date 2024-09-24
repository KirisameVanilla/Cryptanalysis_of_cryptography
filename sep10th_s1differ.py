import numpy as np
def S1_change(text):
    S1_table = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]
    i = int(text[0] + text[-1], 2)
    j = int(text[1:-1], 2)
    S1_text = S1_table[i][j]
    return S1_text

def xor(text1, text2) -> str:
  if len(text1) != len(text2):
    raise Exception
  length = len(text1)
  res = ''
  for i in range(length):
    if text1[i] != text2[i]:
      res = res + '1'
    else:
      res = res + '0'
  return res


def S1_differ(text1,text2):
  s1_res_1 = S1_change(text1)
  s1_res_2 = S1_change(text2)
  dif_res = s1_res_1^s1_res_2
  return dif_res

def main():
  dif_table = np.zeros((64,16),dtype=int)
  for i in range(64):
    input_1 = bin(i)[2:].rjust(6, '0')
    if len(input_1)!=6:
      pass
    for j in range(64):
      input_2 = bin(j)[2:].rjust(6, '0')
      dif_input = i ^ j
      dif_res = S1_differ(input_1, input_2)
      dif_table[dif_input][dif_res] += 1

  print('\\',end='\t')
  for i in range(16):
    print(hex(i)[2:],end='\t')
  print('')
  for i in range(64):
    print(hex(i)[2:], end='\t')
    for j in range(16):
      print(dif_table[i][j], end='\t')
    print('')
if __name__ == "__main__":
  main()
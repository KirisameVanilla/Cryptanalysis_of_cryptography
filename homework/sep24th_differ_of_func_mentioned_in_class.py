import numpy as np
def s_change(text):
  # a simple permutation
  s_table = [6,4,0xc,5,0,7,2,0xe,1,0xf,3,0xd,8,0xa,9,0xb]
  s_text = s_table[text]
  return s_text


def s_differ(text1,text2):
  s_res_1 = s_change(text1)
  s_res_2 = s_change(text2)
  dif_res = s_res_1^s_res_2
  return dif_res

def main():
  dif_table = np.zeros((16,16),dtype=int)
  for i in range(16):
    for j in range(16):
      dif_input = i ^ j
      dif_res = s_differ(i, j)
      dif_table[dif_input][dif_res] += 1

  print('\\',end='\t')
  for i in range(16):
    print(hex(i)[2:],end='\t')
  print('')
  for i in range(16):
    print(hex(i)[2:], end='\t')
    for j in range(16):
      print(dif_table[i][j], end='\t')
    print('')
if __name__ == "__main__":
  main()
import numpy as np
import random
def s_change(int)->int:
  s_table = [6,4,0xc,5,0,7,2,0xe,1,0xf,3,0xd,8,0xa,9,0xb]
  s_text = s_table[int]
  return s_text

def p_change(int)->int:
  p_table = [0,4,8,0xc,1,5,9,0xd,2,6,0xa,0xe,3,7,0xb,0xf]
  p_text = p_table[int]
  return p_text

def s_differ(int1,int2)->int:
  s_res_1 = s_change(int1)
  s_res_2 = s_change(int2)
  dif_res = s_res_1^s_res_2
  return dif_res

def getBinaryString(_string,align):
  return bin(_string)[2:].rjust(align,'0')

def cipherfour_round(m,k,round_index)->int:
  m = m^k[round_index]
  m = getBinaryString(m,16)
  m_t = [m[0:4],m[4:8],m[8:12],m[12:16]]
  m_s = [0,0,0,0]
  for i in range(4):
    m_s[i] = s_change(int(m_t[i],2))
  m_s_string=getBinaryString(m_s[0],4)+getBinaryString(m_s[1],4)+getBinaryString(m_s[2],4)+getBinaryString(m_s[3],4)
  if round_index!=3:
    m_p_plain=int(m_s_string,2)
    mslist =[m_s_string[0:4], m_s_string[4:8], m_s_string[8:12], m_s_string[12:16]]
    p_r=''
    for i in range(4):
      a = int(mslist[i],2)
      b = getBinaryString(p_change(a),4)
      p_r = p_r+b
    return int(p_r,2)
  else:
    m_p_plain=int(m_s_string,2)
    m_p_plain = m_p_plain^k[round_index+1]
    return m_p_plain

def cipherfour(m,k_list):
  result=[0,0,0,0,0,0]
  result[0]=m
  for i in range(4):
    result[i+1]= cipherfour_round(result[i],k_list,i)
  return result[4]

import random
def generate_keys():
  key_list = [0,0,0,0,0]
  for i in range(5):
    a = random.randint(0,pow(2,16)-1)
    key_list[i]=a
  return key_list
    
dif_tab = np.zeros((pow(2,16)),dtype=int)

def main():
  for i in range(20):
    key_list = generate_keys()
    for i in range(pow(2,16)-1):
      int1 = i
      int2 = i^0x0020
      res1 = cipherfour(int1,key_list)
      res2 = cipherfour(int2,key_list)
      dif = res1^res2
      dif_tab[dif]+=1
  max = np.max(dif_tab)
  index = np.where(dif_tab==max)[0]
  print("差分为",end='')
  print(index)
  print("概率为",end='')
  print(max/(20*pow(2,16)))

if __name__ == "__main__":
  main()
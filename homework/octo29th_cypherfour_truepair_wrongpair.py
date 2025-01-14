import numpy as np
import random
def s_change(int)->int:
  s_table = [6,4,0xc,5,0,7,2,0xe,1,0xf,3,0xd,8,0xa,9,0xb]
  s_text = s_table[int]
  return s_text

def p_change(mslist)->int:
  p_r='0000000000000000'
  for i in range(4):
    ms = mslist[i]
    p_r = p_r[0:4*0+i] + ms[0] + p_r[4*0+i+1:]
    p_r = p_r[0:4*1+i] + ms[1] + p_r[4*1+i+1:]
    p_r = p_r[0:4*2+i] + ms[2] + p_r[4*2+i+1:]
    p_r = p_r[0:4*3+i] + ms[3] + p_r[4*3+i+1:]
  return int(p_r,2)

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
  if round_index!=4:# round_num-1
    m_p_plain=int(m_s_string,2)
    mslist =[m_s_string[0:4], m_s_string[4:8], m_s_string[8:12], m_s_string[12:16]]
    p_r = p_change(mslist)
    return p_r
  else:
    m_p_plain=int(m_s_string,2)
    m_p_plain = m_p_plain^k[round_index+1]
    return m_p_plain

def cipherfour(m,k_list,round_num):
  result=[0,0,0,0,0,0,0] #round_num+2
  result[0]=m
  for i in range(round_num):
    result[i+1]= cipherfour_round(result[i],k_list,i)
  return result[round_num]

import random

def generate_keys():
  key_list = [0,0,0,0,0,0] # round_num+1
  used_key = []
  for i in range(6): # round_nunm+1
    a = random.randint(0,pow(2,16)-1)
    while(a in used_key):
      a = random.randint(0,pow(2,16)-1)
    key_list[i]=a
    used_key=[used_key,a]
  return key_list
    

def main():
  key_set_nums = 5
  total = 0
  for j in range(key_set_nums):
    count = 0
    key_list = generate_keys()
    for i in range(pow(2,16)-1):
      int1 = i
      int2 = i^0x0020
      res1 = cipherfour(int1,key_list,5)
      res2 = cipherfour(int2,key_list,5)
      dif = res1^res2
      if(dif == 0x0010 
      or dif == 0x0020 
      or dif == 0x0090 
      or dif == 0x00a0):
        count = count+ 1
    print(count, end=' ')
    total+=count

  print((pow(2,16)*8)*5/total,end='%\n')

if __name__ == "__main__":
  main()
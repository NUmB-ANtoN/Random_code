import random
import csv

def randd():
  with open("list.csv",'r') as F: #to read file
    f = list(csv.reader(F))

  if len(f) != 0:  
    ran = random.choice(f)
    print(ran,f.index(ran))
    f.remove(ran)

    with open("list.csv",'w') as W: # to write file
      w = csv.writer(W)
      w.writerows(f)

    with open("rem.csv",'r') as RR:
      rr = list(csv.reader(RR))
      rr.append(ran)
    
    with open("rem.csv",'w') as R:
      r = csv.writer(R)
      r.writerows(rr)
  if len(f) == 0:
    print("--------List is empty--------")

def read():
  with open("list.csv",'r') as F: 
    f = list(csv.reader(F))
    if len(f) == 0:
      print("--------List is empty--------")
    else:
      for i in f:
        print(i)

def remove():
  with open("rem.csv",'r') as RR:
    rr = list(csv.reader(RR))
    if len(rr) == 0:
      print("--------List is empty--------")
    else:
      for i in rr:
        print(i)

def add():
  num = int(input("Number of elements :"))
  temp = []
  temp2 = []
  for i in range(0,num):
    val = input(" \n Enter the value to add: ")
    temp.append(val)
    temp2.append(temp)
    temp = []
  print(temp2)
  with open("list.csv",'r') as RR:
    rr = list(csv.reader(RR))
    for i in range(0,num):
      rr.append(temp2[i])   
    
  with open("list.csv",'w') as R:
    r = csv.writer(R)
    r.writerows(rr)
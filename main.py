import rancsv
print('''0 : To exit
1 : To read list
2 : TO read remove list
3 : To add file in list
4 : To select the random value
      ''')
f = int(input("Enter the number: "))
while True:
  if f == 0:
    print("End...!")
    break
    
  elif f ==1:
    rancsv.read()
    f = int(input("\nEnter the number: "))
    
  elif f == 2:
    rancsv.remove()
    f = int(input("\nEnter the number: "))
    
  elif f == 3:
    rancsv.add()
    f = int(input("\nEnter the number: "))
    
  elif f == 4:
    rancsv.randd()
    f = int(input("\nEnter the number: "))
    
  else:
    print ("Unknown command")
    f = int(input("\nEnter the number: "))
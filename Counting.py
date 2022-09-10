#COUNTING USING FOR LOOP

for i in  range(10): 
  print(f"Counting by {i+1}") #using f-string to automatically convert int to str.
  for j in range(10):         
    print((j+1)*(i+1), end=" ")  #nilagyan ng +1 sa j at i para hindi sa zero magsimula
  print()
print()                       #para space between sa for loop at while loop

#COUNTING USING WHILE LOOP

i = 0
while i < 10:
  print(f"Counting by {i+1}") #lagyan ng +1 kasi magiistart siya sa zero
  i += 1
  j = 1                       #1 ang start para hindi magsimula sa zero
  while j < 10:
    print(j*i, end=" ")
    j += 1
  print()

#dapat nasa loob yung j kasi hindi siya gagana pagnasa labas siya ng loop

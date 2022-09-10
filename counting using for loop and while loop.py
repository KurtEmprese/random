#counting using for loop

for i in  range(10): 
  print(f"Counting by {i+1}") #using f-string to automatically convert int to str.
  for j in range(10):         
    print((j+1)*(i+1), end=" ")  
  print()
print()
#counting using while loop 
i = 0

while i < 10:
  print(f"Counting by {i+1}")
  i += 1
  j = 1                
  while j < 10:
    print(j*i, end=" ")
    j += 1
  print()

#dapat nasa loob yung j kasi hindi siya gagana pagnasa labas siya ng loop

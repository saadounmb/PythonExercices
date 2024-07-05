# Program to calculate the average of even numbers from 1 to 50
total = 0
count = 0

for i in range(13,51):
  if i % 2== 0:
      total +=i
      count +=1
      
average = total/ count
print("the average of even numbers from 1 to 50 is:",average)
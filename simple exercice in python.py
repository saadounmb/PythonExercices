def calculate_even_numbers_average(numbers):
  even_numbers = [num for  num in numbers if num % 2==0]
  if len(even_numbers)==0:
      return "there are no even numbers in the list"
  average = sum(even_numbers)/len(even_numbers)
  return average


numbers= [11,20,6,14,9,8] 
  
avg_even = calculate_even_numbers_average(numbers)
print("the average of the even numbers is:",avg_even)
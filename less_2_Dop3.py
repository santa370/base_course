
number = int(input("Введите число: "))  
  
reversed_number = 0  
  
while number > 0:  
    last_digit = number % 10  
    reversed_number = reversed_number * 10 + last_digit  
    number = number // 10  
  

print("Обратное число:", reversed_number)  
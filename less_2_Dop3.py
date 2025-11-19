n = int(input("Введите число: "))  
  
reversed_n = 0  
  
while n > 0:  
    last_digit = n % 10  
    reversed_n = reversed_n * 10 + last_digit  
    n = n // 10  
  

print("Обратное число:", reversed_n)  
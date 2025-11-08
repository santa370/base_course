a =float(input("Введите первый член прогресии: "))
x =float(input("Введите знаминеатель прогресии: "))
c =float(input("Введите количество членов прогресии: "))

for i in range (c):
    prog= a * (x**i)
    print(a, end=" ")
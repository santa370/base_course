def calculate(*args):
    if not args:
        return 0

    
    total = sum(args)
    arguments = len(args)
    srednee = total / arguments
    return srednee

aref = calculate(10, 20, 30, 40, 50)
print(f"Среднее арифметическое (10, 20, 30, 40, 50): {aref}")
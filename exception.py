i=0
while i<10:
    try:
        k=int(input("Enter a number: "))
        n=100/k
        print(f'the result is {n:0.2f}')

    except ZeroDivisionError:
        print("Division by zero is not allowed")
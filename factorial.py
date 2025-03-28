def fact(n):
    if (n==0) or n==1 :
        return 1
    else:
        return(n*fact(n-1))
    

n=int(input('Enter the no. to find its factorial :'))
print(fact(n))
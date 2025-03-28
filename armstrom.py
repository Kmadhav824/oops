a=input('Enter the number to check if it is an armstrong number or not: ')
b=len(a)
c=(a[0:b])
sum=0
for i in range(0,b):
    sum +=int(c[i])**b

if(sum==int(a)):
    print('It is an armstrong number')
else:
    print('It is not an armstrong number')
    
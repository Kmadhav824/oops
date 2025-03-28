def bmi(w,h):
    return(w/(h*h))
wt=float(input('Enter your weight : '))
ht=float(input('Enter your height : '))

b=bmi(wt,ht)
if(b<18.5):
    print('Under weight ! ')
elif(b<22.5 and  b>18.5):
    print('Normal Weight ')
elif(b>22.5) and (b<28.5):
    print('Over Weight ! ')
else:
    print("# obese # ")
def sort(b):
    for i in range(len(b)):
        for j in range(i+1,len(b)-1):
            if b[i]>b[j]:
                temp=b[j]
                b[j]=b[i]
                b[i]=temp
    return b

from sys import argv

def main():
    if(len(argv)<2):
        print('Improper usage')

    else:
        a=[int(argv[i]) for i in range(1,len(argv))]
        print(f'given array is : {a}')
        a1=sort(a)
        print('sorted array is : ',a1)

if __name__=='__main__':
    main()

def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                t = a[i]
                a[i] = a[j]
                a[j] = t

a = list(map(int, input('Enter the list of numbers you want to sort (comma separated): ').split(',')))
print('Original list:', a)
a = list(map(int, b.split(',')))
print('Original list:', a)
print('Sorted list:', a)
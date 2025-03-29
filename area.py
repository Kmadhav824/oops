from sys import argv

def area(l: int, b: int) -> int:
    return l*b

def main():
    # Check if the number of arguments is less than 3 (script name, length, and breadth)
    if len(argv) < 3:
        print('Usage: python area.py <length> <breadth>')
        print('improper usage')
    else:
        try:
            l1 = int(argv[1])
            b1 = int(argv[2])
            print(f'The area of the rectangle is : {area(l1, b1)}')
        except ValueError:
            print('Please enter valid integers for length and breadth')

if __name__ == '__main__':
    main()

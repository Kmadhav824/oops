class date:
    def __init__(self,d,m,y):
        self.dd=d
        self.mm=m
        self.yy=y

    def getdata(self):
            self.dd=int(input("Enter the date: "))
            self.mm=int(input("Enter the month:"))
            self.yy=int(input("Enter the year:"))

    def __str__(self):
            return f'{self.dd}/{self.mm}/{self.yy}'
        
    def checkleap(self):
            if(self.yy%4==0 and self.yy%100!=0) or (self.yy%400==0):
                return True
            else:
                return False
            
    def checkdate(self,other):
            if(self.dd==other.dd and self.mm==other.mm and self.yy==other.yy):
                return True
            else:
                return False
            
    # operator overloading inbuilt in python
def __eq__(self,other):
        if(self.dd==other.dd and self.mm==other.mm and self.yy==other.yy):
            return True
        else:
            return False
        
def __iadd__(self,n):
            self.dd+=n
            if(self.dd>31):
                self.dd-=31
                self.mm+=1
                if(self.mm>12):
                    self.mm-=12
                    self.yy+=1
            return self
        
def main():
    d1=date(10,11,2024)
    d2=date()
    d2.getdata()
    d1.printdata()
    d2.printdata()
    print(d1)
    print(str(d1))
    if(d1.checkleap()):
        print("Leap year")
    else:
        print("Not a leap year")
'''def bargraph(n):
    for i in reversed(n):
        print('*'*i)

n=[3,3,3]
bargraph(n)'''

'''def bargraph(n):
    r=max(n)
    c=len(n)
    for i in range(1,r+1):
        for j in range(1,c+1):

            if r-n[j-1]>=i:
                print('  ',end='')
            else:
                print('*   ',end='')
        print()

n=[2,4,6,0,5]
bargraph(n)'''

class bike:
    def __init__(self,m,y,c):
        self.model=m
        self.year=y
        self.color=c
    def speed(self):
        return"this is moving 20 mph"
    
    def display(self):
        return f"this is {self.year} {self.color} {self.model}  bike"
   
    
bullet=bike("bullet",2020,"black")
print(bullet.speed())
print(bullet.display())

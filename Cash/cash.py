from cs50 import get_float

while True:
    f=get_float("Change owed: ")
    if f>=0:
        break
f=f*100
n= int(f/25)
x=int((f%25)/10)
y=int((f%25%10)/5)
z=int((f%25%10%5))

print(n+x+y+z)
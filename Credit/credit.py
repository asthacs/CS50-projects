from cs50 import get_int, get_string

n= get_int("Number: ")

sum1=0
sum2=0
x=str(n)
for i in range(len(x)-2, -1, -2):

    for j in range(len(str(int(x[i])*2))):
        m=str(int(x[i])*2)
        sum1=sum1+int(m[j])



for i in range(len(x)-1, -1, -2):

    sum2=sum2+int(x[i])
sum3=sum1+sum2


if sum3%10==0:

    if len(x)==15 and ((x[0]=='3' and x[1]=='4') or (x[0]=='3' and x[1]=='7')):
        print("AMEX")
    elif len(x)==16 and ((x[0]=='5' and x[1]=='1') or (x[0]=='5' and x[1]=='2') or (x[0]=='5' and x[1]=='3') or (x[0]=='5' and x[1]=='4') or (x[0]=='5' and x[1]=='5')):
        print("MASTERCARD")
    elif (len(x)==13 or len(x)==16) and x[0]=='4':
        print("VISA")
else:
    print("INVALID")
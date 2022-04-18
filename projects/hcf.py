x = int(input())
y = int(input())

if x < y:
    x,y=y,x

for i in range(1,y+1):
    if((x%i)==0 and (y%i)==0):
        hcf=i
print(hcf)
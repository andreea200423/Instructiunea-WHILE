x=0
s=0
while not((x%2!=0) and (x%3==0)):
    x=eval(input("Introduceti un nr: "))
    if x%2==0:
        s+=x
print("Suma tuturor nr pare introduse este",s)
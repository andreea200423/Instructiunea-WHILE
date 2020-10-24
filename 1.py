n=eval(input("n ="))
i=1
s=0
p=1
while i<=n:
    s+=i
    p*=i
    i+=1
print("suma este {p}, iar media aritmetica e {s/n}")
#Credits to my friend
n=int(input()) 
l=['3','7']
for i in range(2,90000):
    l.append(l[i-2]+'3')
    l.append(l[i-2]+'7')
l=[i for i in l if i==i[-1::-1]]
print(l[n-1])

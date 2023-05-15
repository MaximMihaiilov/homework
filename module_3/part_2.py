l = [1,4,1,6,"hello","a",5,"hello"]
l2 = []

for i in range(len(l)): 
    n=0
    for j in l: 
        if j == l[i-1]:
            n+=1
            if n >= 2: 
                l2.append(j)
print(l2)
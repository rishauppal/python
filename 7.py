n=7  
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]"  
index=0  
for i in range(1, n+1):
    print(" "*(n-i), end=" ")
    for j in range(i):
        print(alphabet[index], end=" ")
        index+=1      
    print()

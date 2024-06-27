array=[]
n=int(input("enter number of elements : "))
for i in range(n):
    l=int(input())
    array.append(l)  
print(array)
even_array=[x*2 for x in array if x%2==0]
print(even_array) 


   

   #Arithmetic

x=lambda a, b, c: a +(c-1)*b
arr=[]
sqrarr=[]
sum=0
def func1(a,b,c):
    for i in range(1,c+1):
        arr.append(x(a,b,i))
    for i in arr:
        sqrarr.append(i*i)
    for i in sqrarr:
        global sum
        sum=sum+i
    n=len(arr)    
    for i in range(n):
        print(arr[i],end=" ")
    print("\n")

    n1=len(sqrarr)    
    for i in range(n1):
        print(sqrarr[i],end=" ")
    print("\n")
    print(arr)
    print(sqrarr)
    print(sum)
func1(2,5,7)
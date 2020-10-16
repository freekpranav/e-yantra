
if __name__== '__main__':

    test_cases=int(input())
    n=int(input())
    for i in range(0,n):
        if(i==0):
            i+=3
            print("\n")
            print(i,end=" ")
        elif(i%2):
            i*=i
            print(i,end=" ")
        else:
            i*=2
            print(i,end=" ")


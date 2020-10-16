def third(m):
    return[m[i] for i in range(0+3,len(m),3)]
def fourth(m):
    return[m[i] for i in range(0+5,len(m),3)]

if __name__ == '__main__':
    lst=[]
    n=int(input())
    for i in range (0,n):
        ele=int(input())
        lst.append(ele)
    l=lst[::-1]
    n=len(lst)
    for i in range(n):
        print(l[i],end=" ")
    print("\n")
    third(lst)
    r=len(third(lst))
    for i in range(r):
        b=third(lst)[i]
        b+=3
        print(b,end=" ")
    print("\n")
    fourth(lst)
    r=len(fourth(lst))
    for i in range(r):
        b=fourth(lst)[i]
        b-=7
        print(b,end=" ")
    print("\n")
    y=lst[3:8]
    a=sum(y)
    print(a)
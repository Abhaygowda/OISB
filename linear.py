def l_search(a,x,l,n):
    if l<n:
        if a[1]==x:
            print("element found at location",l,"position")
        else:
            l_search(a,x,l+1,n)

    else:
        print("element not found")
print("enter list:")
a=[int(b) for b in input().split()]
x=eval(input("enter search element"))
n=len(a)
l=(a,x,0,n)

n1,n2,n3,n4,n5=list(map(int,input("Enter the numbers:").split()))
if (n1>=0) and (n2>=0) and (n3>=0) and (n4>=0) and (n5 >= 0):
    sum= (n1+n2+n3+n4+n5)
    print("the total sum is:",sum)
else:
    print("error,there is negative number")
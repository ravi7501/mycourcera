myl=[]#adding element to empty list
n=int(input("enter the no of digit you want to enter"))
add=0
for i in range(n):
    print("enter the digit")
    m=int(input())
    myl.append(m)
print(myl)

#ading each element of list
for i in range(len(myl)):
    add+=myl[i]
print('sum: ',add)


#reversing order of list
for i in range(len(myl)//2):
    myl[i], myl[n- i - 1] = myl[n- i - 1], myl[i]
print(myl)
#or we can directly use list.reverse()

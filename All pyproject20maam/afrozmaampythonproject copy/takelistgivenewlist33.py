# write Python function that takes a list and returns a new list with distinct elements from the first list.
def distlist(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
a=[]
while True:
    c=int(input("Enter a number(0 to exit): "))
    if c == 0:
        break
    else:
        a.append(c)
print(a)
print("Distinct list:")
distlist(a)

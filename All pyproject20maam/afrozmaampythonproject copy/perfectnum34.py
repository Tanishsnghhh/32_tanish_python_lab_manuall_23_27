#3.4 Write a program to Check whether a number is perfect or not.
def perfect(a):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i
    if sum == a:
        print(a, " is perfect number")
    else:
        print(a, "is not a perfect number")
a = int(input("Enter a number: "))
perfect(a)
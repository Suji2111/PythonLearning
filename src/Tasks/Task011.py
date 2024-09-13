# Fibonacci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

f = int(input("Enter the number to find fibonacci of: "))
a = 0
b= 1
fib = 0
if f==0:
    print(0)
elif f==1:
    print(0)
else:
    for i in range(2,f+1):
        fib=a+b
        a=b
        b=fib
    print(fib)
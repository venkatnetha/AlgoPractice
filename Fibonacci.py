# fibonacci series is 0,1,1,2,3,5,8,13,....
# alogo using the naive recusrive method.

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else:        
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(9))

# print the first n fibonacci numbers

def printfib(n):
    f1=0
    f2=1

    if(n<1):
        return
    
    for x in range(0,n):
        print(f1, end ="")
        next = f1+f2
        f1 = f2
        f2 = next
    

printfib(5)
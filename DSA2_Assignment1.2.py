#Modify your code in no.1 to write a code for Fibonacci (iterative DP) 

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    temp = [0, 1]
    
    for i in range(2, n + 1):
        temp.append(temp[i - 1] + temp[i -2])
        
    return temp[n]
            

n = int(input("Enter a number:"))

print(f"Fibonacci numbers: {fib(n)}")
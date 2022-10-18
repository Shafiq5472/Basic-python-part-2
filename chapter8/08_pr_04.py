#write a recursive function to calculate the sum of first n natural numbers

def summ(n):
    if n == 0 or n ==1:
        return 1
    return n+summ(n-1)

print(summ(5))

#n! = 1*2*3*4*....*n
#n! = n*(n-1)!
# n=4
# product = 1

# for i in range(n):
#     product = product*(i+1)
# print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product *= (i+1)
    return product
print(factorial_iter(4))

#%%
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n*factorial_recursive(n-1)
print(factorial_recursive(4))
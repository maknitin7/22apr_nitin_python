a=[-4,-2,0,3,10]
square=[]
for x in a:
    square.append(x*x)
print(square)

"""square=[i*i for i in a]
print(square)"""

"""for i in range(len(a)):
    a[i] = a[i] * a[i]

print("Squared array (in-place):", a)
"""

square.sort()
print("Squared array (sorted):", square)
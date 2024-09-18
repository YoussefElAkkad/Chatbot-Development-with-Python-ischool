a=[]
for x in range(1,11):
    a.append(x*x)
print("List a: %s"%a)

b=[x**2 for x in range(1,11)] #list comprehension
print("List b: %s"%b)

#normal division
result=5/3
print(result)
#integer division(floor division)
result=5//3
print(result)

#f-strings(formatted StringLiterals )
name="Alice"
print(f"Hello, {name}!")
print(f"List a: {a}")

def double(x):
    return x*2

number=7
print(f"Double of {number} is {double(number)}.")

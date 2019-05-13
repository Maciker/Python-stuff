# Caesar's cipher simply shifts the text to be encrypted
# to the left or the right in the alphabet.
def decrypt(s):
    l = [chr(ord(c)-2) for c in s]
    return ''.join(l)

print(decrypt("Ecguct"))

# Fibonacci series
a, b = 0,1
while b < 5:
    print(b)
    a, b = b, a+b

# Basic recursion. Solve problems with easy sub-problems
# "to understand recursion, one must first understand recursion." -- Stephen Hawking
def ping(i):
    if i>0:
        return pong(i-1)
    return "0"
def pong(i):
    if i>0:
        return ping(i-1)
    return "1"
print(ping(29))

# factorial
def factorial(x):
    y = 1
    for i in range(1, x+1):
        y *= i
    return y

print(factorial(6))
print(factorial(4))
print(factorial(6) // factorial(4))

# recursive function
def recursive_function(x,y):
    if (x%2==0):
        return x
    else:
        y = y + 3
        return recursive_function(x-y,y)

print(recursive_function(10,3))

# Profit of a single
# buying low and selling high
def maximumProfit(A):
    m = 0
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            m = max(m, A[j] - A[i])
    return m
# Ethereum prices Dic 2017
prices = [455,460,465,451,414,415,441]
print(maximumProfit(prices))

# https://en.wikipedia.org/wiki/Levenshtein_distance
def levenshtein(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(levenshtein(a[1:], b[1:])+(a[0] != b[0]),
               levenshtein(a[1:], b)+1, levenshtein(a, b[1:])+1)

print(levenshtein("xkcd","cool"))
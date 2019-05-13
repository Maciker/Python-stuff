# function arguments
def f(val1=3, val2=4, val3=6):
    return val1 + val2 + val3

values = {"val1":9, "val3":-1}
print(f(**values))

# decrpyt strings
def encrypt(s):
    return ''.join(reversed(s))

def decrypt(s):
    return s[::-1]

cleartext = """Nothing travels \
faster than the speed of light \
with the exception of bad news"""

print(decrypt(encrypt(cleartext)))
print(cleartext == decrypt(encrypt(cleartext)))

# Control flow
i = 5
def f(arg=i):
    print(arg)
i=6
f()

# lambda function
print(list(map(lambda x: 2 + (0 if x==1 else 8),range(4))))
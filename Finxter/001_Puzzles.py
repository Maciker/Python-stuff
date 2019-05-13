# Finxter Puzzles

a,b = zip(*[('g','d'),
            ('r', 'a'),
            ('e', 'y'),
            ('a', '!'),
            ('t', '')])
print (''.join(a)+ " "+''.join(b))

x = 50*2 + (60-20)/4
print(x)

squares = [1,4]
print(squares[:] + [9, 16])

print(list(range(3)))

# lambda function
def make_incrementator(n):
    return lambda x: x+n

f = make_incrementator(42)
print(f(0))
print(f(1))

# Funcion para ordenar lista de menor a mayor
def bubblesortt(lst):
    for passesLeft in range(len(lst)-1,0,-1):
        for index in range(passesLeft):
            if lst[index] > lst[index+1]:
                lst[index], lst[index+1] = lst[index+1], lst[index]

    return lst

l = [27,0,71,70,27,63,90]
print (bubblesortt(l))

# range
word = "galaxy"
print(word[-4:])
print(len(word[1:]))

print(range(5,10)[-1])
print(range(0,10,3)[-2])
print(range(-10,-100,-30)[1])

l=[1,2,3,4]
print(l[::-2])

letters= ['a','b','c','d','e','f','g']
letters[1:]= []
print(letters)

letters= ['a','b','c','d']
print(len(letters[1:-1]))

customers = ['Marie', 'Anne', 'Donald']
customers[2:4]=['Barack', 'Olivia', 'Sophia']
print(customers)
print(customers[2:-1])
def cons(a, b):
    def pair(f):
        return f(a, b)   
    return pair

# val = cons(3,4)
# print(val(print))

def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)

print(car(cons(3,4)))
print(cdr(cons(3,4)))
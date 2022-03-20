# Power Program  example
#  p(2,3) = 2*2*2 =8

def power(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return (base * power(base, exp - 1))


base = 2
exp = 3
print("Value is:", power(base, exp))

# Forward
def recursion1(n):
    if(n>0):
        print("woo-", n)
        recursion1(n-1)

recursion1(3)

# o/p -
# woo- 3
# woo- 2
# woo- 1


# Backward
def recursion2(n):
    if(n>0):
        recursion2(n-1)
        print("woo-", n)

recursion2(3)

#
# o/p -
#
# woo- 1
# woo- 2
# woo- 3

def recursion3(n):
    if(n>0):
        print("woo-", n)
        recursion3(n-1)
        recursion3(n - 1)

recursion3(3)

# o/p -
# woo- 3
# woo- 2
# woo- 1
# woo- 1
# woo- 2
# woo- 1
# woo- 1
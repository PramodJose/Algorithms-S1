def multiply(a, b, n):  # n is the number of bits; and not the number of digits
    if n == 1:
        return a & b    # multiplication of two bits is basically bitwise AND. Hence, we can write (a * b) as (a & b).

    nR = (n//2)                 # number of bits on the right..
    nL = n - nR                 # and number of bits on the left...

    aL = a >> (n//2)            # extract the left parts of..
    bL = b >> (n//2)            # ..both a and b

    aR = a & ((1 << nR) - 1)    # extract the right parts of
    bR = b & ((1 << nR) - 1)    # both a and b

    x1 = multiply(aL, bL, nL)
    x2 = multiply(aR, bR, nR)

    sumA = aL + aR
    sumB = bL + bR
    newN = max(nL, nR)          # the new number of bits would be the max of the number of bits on the left and right

    if (sumA & (1 << newN) != 0) or (sumB & (1 << newN) != 0):  # if there was an overflow, then increment newN..
        newN += 1                                               # i.e., the new number of bits.

    x3 = multiply(sumA, sumB, newN)

    if n & 1 != 0:              # if n is odd, then we need to shift x1 by one place less.
        n ^= 1                  # same as n -= 1; but slightly faster

    retVal = (x1 << n) + ((x3 - x1 - x2) << nR) + x2
    return retVal


print("result = " + str(multiply(211, 89, 8)))

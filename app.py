import random
import time

#1
def mergeSort(l):
    if(len(l) == 1):
        return l
    a = mergeSort(l[ : int(len(l)/2) ] )
    b = mergeSort(l[ int(len(l)/2) : ] )
    return merge(a, b)

def merge(a, b):
    ia = 0
    ib = 0

    result = []
    while(ia < len(a) and ib < len(b)):
        if(a[ia] < b[ib]):
            result.append(a[ia])
            ia += 1
        else:
            result.append(b[ib])
            ib += 1        
    result+=a[ia:]
    result+=b[ib:]

    return result


# teste da 1
"""x = 2048
l = random.sample(range(x), x)
start = time.time()
mergeSort(l)
end = time.time()
print("time to 1048576: " + str(end - start))
# time to 32: 0.0
# time to 2048: 0.018056631088256836
# time to 1048576: 19.85791015625"""

#2
def maxVal1(a):
    max = a[0]
    for i in a[1:]:
        if i > max:
            max = i
    return max

# teste da 2
"""size = 1048576
sample = random.sample(range(size), size)
start = time.time()
maxVal1(sample)
end = time.time()
print("time to 1048576: " + str(end - start))
# time to 32: 0.0
# time to 2048: 0.0
# time to 1048576: 0.24918556213378906"""

#3
def maxVal2(a):
    if (len(a) <= 1):
        return max(a[0], a[-1])
    size = int(len(a)/2)
    v1 = maxVal2(a[:size])
    v2 = maxVal2(a[size:])
    return max(v1, v2)

# teste da 3
"""size = 1048576
sample = random.sample(range(size), size)
start = time.time()
maxVal2(sample)
end = time.time()
print("time to 1048576: " + str(end - start))
# time to 32: 0.0
# time to 2048: 0.0069997310638427734
# time to 1048576: 3.7231509685516357"""

#4
import math
cont = 0

def multiply(x, y, n):
    global cont
    cont += 1

    if(n == 1):
        return x * y
    else:
        m = n // 2
        p = int(math.pow(2, m))
        a = x // p
        b = x % p
        c = y // p
        d = y % p
        e = multiply(a,c,m)
        f = multiply(b,d,m)
        g = multiply(b,c,m)
        h = multiply(a,d,m)
        return int(math.pow(2, 2 *m )) * e + int(math.pow(2, m)) *(g+h) + f

start = time.time()
multiply(15,15,4)
end = time.time()
print("time to 4 bits: " + str(end - start) + "\tIterations: " + str(cont))

start = time.time()
multiply(15,15,16)
end = time.time()
print("time to 16 bits: " + str(end - start) + "\tIterations: " + str(cont))

start = time.time()
multiply(15,15,64)
end = time.time()
print("time to 64 bits: " + str(end - start) + "\tIterations: " + str(cont))

start = time.time()
multiply(9223372036854775807,9223372036854775807,64)
end = time.time()
print("time to 64 bits: " + str(end - start) + "\tIterations: " + str(cont))


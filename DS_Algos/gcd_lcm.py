def gcd(a, b):
    while b:
        a, b = b, a % b
    
    return a

def lcm(a, b):
    return (a*b) // gcd(a, b)

def gcd_arr(arr):
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        return arr[0]
    
    res = gcd(arr[0], arr[1])

    for i in range(2, len(arr)):
        res = gcd(res, arr[i])
    
    return res

assert gcd(4, 18) == 2
assert lcm(4, 18) == 36
assert gcd_arr([2,3,4,5,6]) == 1
assert gcd_arr([2,4,6,8,10]) == 2

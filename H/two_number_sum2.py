def f(a,s): # T:O(n)|S:O(n)
    d = {}
    for n in a:
        m = s - n
        if m not in d:
            d[n] = True
        else:
            return [m , n]
    return []

a=[1,3,5,-7,-2,-1]
s=8
print(f(a,s))

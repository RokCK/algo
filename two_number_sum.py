def f(a, s): # T:O(nLog(n))|S:O(1)
    a.sort()
    l=0
    r=len(a)-1
    while l < r:
        c = a[l] + a[r]
        if c == s:
            return [a[l], a[r]]
        elif c < s:
            l += 1
        elif c > s:
            r -= 1
    return []

a=[9,1,3,-5,2,-11,-1]
s=4
print(f(a,s))

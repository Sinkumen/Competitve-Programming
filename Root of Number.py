def root(x, n):
    i = 0
    j = x
    if x < 1:
        j = 1
    while (j-i >= 0.001):
        mid = (i+j)/2
        curr = mid ** n
        if curr > x:
            j = mid
        else:
            i = mid
    return mid


print(root(7, 3))

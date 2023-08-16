# Recursive Arithematic Series

def recursiveAP(a, d, n):
    if n == 1:
        return a
    else:
        return recursiveAP(a, d, n-1)+d


print(recursiveAP(6, 7, 7))


def recursiveGP(a, r, n):
    if n == 1:
        return a
    else:
        return recursiveGP(a, r, n-1)*r


print(recursiveGP(3, 4, 4))

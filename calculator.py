
def prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# Check if [a, b, c] = [x, y, z] in
# the projective space mod n
def equiv(a, b, c, x, y, z, n):
    p1 = [a, b, c]
    p2 = [x, y, z]
    for i in range(3):
        if (p1[i] * p2[0] - p1[0] * p2[i]) % n != 0:
            return False
    return True


# all group elements of
# y^2 = x^3 + ax + b
# in mod p
def calc(a, b, p):
    ans = [(0, 0, 1)]
    for x in range(p):
        for y in range(p):
            res = y * y - (x * x * x + a * x + b)
            res %= p
            if res == 0:
                exists = False
                for point in ans:
                    if equiv(point[0], point[1], point[2], x, y, 0, p):
                        exists = True
                        break
                if not exists:
                    ans.append((x, y, 0))
    return ans


a = 2
b = 4
p = 35
print("calculating y^2 = x^3 + {}x + {} (mod {})".format(a, b, p))
ls = calc(a, b, p)

for x in ls:
    print(x)



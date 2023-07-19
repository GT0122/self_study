# 유클리드 호제법
def gcd(a, b) :
    while b != 0 :
        a, b = b, a % b

    return a

print(gcd(1274, 975))
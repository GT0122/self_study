import math, time

def is_prime(n) :
    if n <= 1 :
        return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False
    return True

def is_prime_time(n) :
    for i in range(n) :
        if is_prime(i) :
            print(i, end=' ')

# 에라토스테네스의 체
def get_prime(n) :
    if n <= 1 :
        return []
    prime = [2]
    limit = int(math.sqrt(n))

    data = [i + 1 for i in range(2, n, 2)]

    while limit >= data[0] :
        prime.append(data[0])
        data = [j for j in data if j % data[0] != 0] # 배수를 제외

    return prime + data

start = time.time()
is_prime_time(100000)
end = time.time()

print('\n')
print(f'{end - start:.5f} sec')

start = time.time()
get_prime(100000)
end = time.time()

print('\n')
print(f'{end - start:.5f} sec')
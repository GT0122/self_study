# 선형 검색
def linear_search(data, value) :
    for i in range(len(data)) :
        if data[i] == value :
            return i
    return -1

# 이진 검색
def binary_search(data, value) :
    left = 0
    right = len(data) - 1
    while left <= right :
        mid = (left + right) // 2
        if data[mid] == value :
            return mid
        elif data[mid] < value :
            left = mid + 1
        else :
            right = mid - 1
    return -1

data = [50, 30, 90, 10, 20, 70, 60, 40, 80]

print(linear_search(data, 40))
print(binary_search(sorted(data), 40))

tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]

# 전위 순회
def pre_order(pos) :
    print(pos, end=' ')
    for i in tree[pos] :
        pre_order(i)

# 후위 순회
def post_order(pos) :
    for i in tree[pos] :
        post_order(i)
    print(pos, end=' ')

# 중위 순회
def in_order(pos) :
    if len(tree[pos]) == 2 :
        in_order(tree[pos][0])
        print(pos, end=' ')
        in_order(tree[pos][1])
    elif len(tree[pos]) == 1 :
        in_order(tree[pos][0])
        print(pos, end=' ')
    else :
        print(pos, end=' ')

print('pre_order')
pre_order(0)
print()
print('post_order')
post_order(0)
print()
print('in_order')
in_order(0)
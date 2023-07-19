origin = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 선택 정렬
def selection(origin) :
    data = origin.copy()
    for i in range(len(data)) :
        min = i
        for j in range(i + 1, len(data)) :
            if data[min] > data[j] :
                min = j

        data[i], data[min] = data[min], data[i] # 가장 작은 수를 앞으로 이동

    print(data)

# 삽입 정렬
def insertion(origin) :
    data = origin.copy()
    for i in range(1, len(data)) :
        temp = data[i]
        j = i - 1
        while (j >= 0) and (data[j] > temp) : # 큰 경우까지 찾음
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp # 그 뒤에 삽입

    print(data)

# 버블 정렬
def bubble(origin) :
    data = origin.copy()
    for i in range(len(data)) :
        for j in range(len(data) - i - 1) :
            if data[j] > data[j + 1] : # 자신 앞자리와 비교하여 크면 이동
                data[j], data[j + 1] = data[j + 1], data[j]

    print(data)

# 힙 정렬
def heap(origin) :
    data = origin.copy()
    # 힙 구성
    for i in range(len(data)) :
        j = i
        while (j > 0) and (data[(j - 1) // 2] < data[j]) :
            data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2]
            j = (i - 1) // 2

    # 정렬
    for i in range(len(data), 0, -1) :
        data[i - 1], data[0] = data[0], data[i - 1]
        j = 0
        while ((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1])) \
        or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])) :
            if (2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2]) :
                data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
                j = 2 * j + 1
            else :
                data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
                j = 2 * j + 2

    print(data)

# 병합 정렬
def merge_sort(data) :
    if len(data) <= 1 :
        return data
    mid = len(data) // 2
    # 분할
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    # 병합
    return merge(left, right)

def merge(left, right) :
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)) :
        if left[i] <= right[j] :
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1

    if i < len(left) :
        result.extend(left[i:])
    if j < len(right) :
        result.extend(right[j:])
    return result

# 퀵 정렬
def quick(data) :
    if len(data) <= 1 :
        return data
    
    pivot = data[0]
    left, right, same = [], [], 0

    for i in data :
        if i < pivot : # 작다면 왼쪽
            left.append(i)
        elif i > pivot : # 크다면 오른쪽
            right.append(i)
        else :
            same += 1
    # 왼쪽, 오른쪽에서 다시 정렬
    left = quick(left)
    right = quick(right)
    # 병합
    return left + [pivot] * same + right

selection(origin)
insertion(origin)
bubble(origin)
heap(origin)
print(merge_sort(origin))
print(quick(origin))
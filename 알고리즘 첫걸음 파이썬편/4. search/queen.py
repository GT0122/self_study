N = 8

def check(x, col) :
    for i, row in enumerate(reversed(col)) :
        if (x  + i + 1 == row) or (x - i - 1 == row) : # 왼쪽 대각선 위치에 있는지
            return False
        
    return True

def search(col) :
    if len(col) == N : # 끝까지 찾으면 출력
        print(col)
        return
    
    for i in range(N) :
        if i not in col : # 동일한 행은 출력하지 않음
            if check(i, col) :
                col.append(i)
                search(col)
                col.pop()

search([])
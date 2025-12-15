def knapSack_travel(W, items):
    n = len(items)

    # 물건 정보 분리
    wt = [item[1] for item in items]      # 무게
    val = [item[2] for item in items]     # 만족도
    name = [item[0] for item in items]    # 물건 이름

    #초기화
    A = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:                 # 물건을 넣을 수 없는 경우
                A[i][w] = A[i - 1][w]
                
            else:                              # 물건을 넣을 수 있는 경우
                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]]
                valWithout = A[i - 1][w]
                A[i][w] = max(valWith, valWithout)

    max_value = A[n][W]

    # 3. 선택된 물건 역추적
    selected = []
    w = W
    for i in range(n, 0, -1):
        if A[i][w] != A[i - 1][w]:            # i번째 물건이 선택된 경우
            selected.append(name[i - 1])
            w -= wt[i - 1]                    # 남은 용량 갱신

    selected.reverse()
    return max_value, A, selected


# 물건 목록 (이름, 무게, 만족도)
items = [
    ("노트북", 3, 12),
    ("카메라", 1, 10),
    ("책", 2, 6),
    ("옷", 2, 7),
    ("휴대용 충전기", 1, 4),
]

# 사용자 입력
W = int(input("배낭 용량을 입력 하세요 : "))

max_value, A, selected_items = knapSack_travel(W, items)

# 결과 출력
print("최대 만족도:", max_value)
print("선택된 물건:", selected_items)


def solution(x, y):
    m, f, cnt = int(x), int(y), 0
    while f > 0:
        if f > m: m, f = f, m
        m, f, c = f, m % f, m // f
        cnt += c
    return str(cnt - 1) if m == 1 else "impossible" 
    
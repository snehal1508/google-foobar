def solution(n):
    cnt = 0
    n = int(n)
  
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n - 1) if (n == 3 or n % 4 == 1) else (n + 1)

        cnt += 1
    return cnt
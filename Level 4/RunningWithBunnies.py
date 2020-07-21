from itertools import permutations


def floyd_warshall(t):
    dp = t
    for k in range(len(t)):
        for i in range(len(t)):
            for j in range(len(t)):
                if(dp[i][j] > dp[i][k]+dp[k][j]):
                    dp[i][j] = dp[i][k]+dp[k][j]
    for i in range(len(t)): 
        if dp[i][i] < 0:
            return False

    return dp


def solution(t, t_limit):

    dp = floyd_warshall(t)

    ans = []
    if dp == False:
        return [i for i in range(0, len(t)-2)]

    order_of_bunny = list(permutations(range(1, len(t)-1)))

    power_set_size = 2**(len(t)-2)

    for l in order_of_bunny:

        for i in range(power_set_size): 

            bunny_picked = []
            current = 0
            cost = 0
            for j in l:  

                if i & (1 << (j-1)):
                    cost += dp[current][j]
                    bunny_picked.append(j-1)
                    current = j

            cost += dp[current][len(t)-1]

            if cost <= t_limit:  # pciking lexographicaly large order
                if len(bunny_picked) > len(ans):
                    ans = bunny_picked
                elif len(bunny_picked) == len(ans):
                    for k in range(len(ans)):
                        if bunny_picked[k] < ans[k]:
                            ans = bunny_picked
                            break
                        elif bunny_picked[k] > ans[k]:
                            break

    ans.sort()
    return ans

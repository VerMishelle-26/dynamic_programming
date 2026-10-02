# === К1: Задача о рюкзаке (0/1 Knapsack) ===
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


# === К2: LCS ===
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


# === К3: Количество разбиений ===
def count_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]


# === К4: Флойд-Уоршелл ===
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


# === Проверка ===
if __name__ == "__main__":
    print("=== К1: Рюкзак ===")
    print(f"Максимум: {knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7)}")

    print("\n=== К2: LCS ===")
    print(f"LCS('AGGTAB', 'GXTXAYB') = {lcs('AGGTAB', 'GXTXAYB')}")

    print("\n=== К3: Разбиения ===")
    for n in [1, 2, 3, 4, 5, 10]:
        print(f"count_partitions({n}) = {count_partitions(n)}")

    print("\n=== К4: Флойд-Уоршелл ===")
    INF = float("inf")
    graph = [
        [0,   5,   INF, 10],
        [INF, 0,   3,   INF],
        [INF, INF, 0,   1],
        [INF, INF, INF, 0],
    ]
    result = floyd_warshall(graph)
    for row in result:
        print("  " + " ".join(f"{x:>4}" for x in row))
from typing import List

def sat304(strategies: List[List[float]], A=[[0.0, -0.5, 1.0], [0.75, 0.0, -1.0], [-1.0, 0.4, 0.0]], eps=0.01):
    m, n = len(A), len(A[0])
    p, q = strategies
    assert all(len(row) == n for row in A), "inputs are a matrix"
    assert len(p) == m and len(q) == n, "solution is a pair of strategies"
    assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
    v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
    return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
            all(sum(A[i][j] * p[i] for i in range(m)) >= v - eps for j in range(n)))
def sol304(A=[[0.0, -0.5, 1.0], [0.75, 0.0, -1.0], [-1.0, 0.4, 0.0]], eps=0.01):
    """
    Compute minimax optimal strategies for a given zero-sum game up to error tolerance eps.
    For example, rock paper scissors has
    A = [[0., -1., 1.], [1., 0., -1.], [-1., 1., 0.]] and strategies = [[0.33, 0.33, 0.34]] * 2
    """
    MAX_ITER = 10 ** 4
    m, n = len(A), len(A[0])
    a = [0 for _i in range(m)]
    b = [0 for _j in range(n)]

    for count in range(1, MAX_ITER):
        i_star = max(range(m), key=lambda i: sum(A[i][j] * b[j] for j in range(n)))
        j_star = min(range(n), key=lambda j: sum(A[i][j] * a[i] for i in range(m)))
        a[i_star] += 1
        b[j_star] += 1
        p = [x / (count + 1e-6) for x in a]
        p[-1] = 1 - sum(p[:-1])  # rounding issues
        q = [x / (count + 1e-6) for x in b]
        q[-1] = 1 - sum(q[:-1])  # rounding issues

        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        if (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(A[i][j] * p[i] for i in range(m)) >= v - eps for j in range(n))):
            return [p, q]
# assert sat304(sol304())

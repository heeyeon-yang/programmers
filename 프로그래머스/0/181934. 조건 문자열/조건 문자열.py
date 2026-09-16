def solution(ineq, eq, n, m):
    if ineq == '>':
        return int(n >= m if eq == '=' else n > m)
    else:
        return int(n <= m if eq == '=' else n < m)
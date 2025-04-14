


def main():
    N, m, M, T, R = map(int, input().split())

    t = 0
    r = 0
    p = m
    while t < N :
        r += 1
        if p + T <= M:
            t += 1
            p += T
            continue
        np = max(m, p - R)
        if np == p : return -1
        p = np
    return r

print(main())
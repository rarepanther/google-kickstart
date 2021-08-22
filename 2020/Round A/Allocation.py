T = int(input())
for t in range(1, T+1):
    B = int(input().split()[1])
    H = list(map(lambda g: int(g), input().split()))
    H.sort()
    count = 0
    for h in H:
        if B >= h:
            B = B-h
            count += 1
    print(f"Case #{t}: {count}")

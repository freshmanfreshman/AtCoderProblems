A, B, C = map(int, input().split())

ans = ((A-1)//C+1) * C
if ans >B:
    print(-1)
else:
    print(ans)
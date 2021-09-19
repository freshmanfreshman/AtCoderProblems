N = int(input())
X, Y = map(int, input().split())
A = [0]*N
B = [0]*N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b
    
if sum(A)<X or sum(B)<Y:
    print(-1)
    exit()
    
    

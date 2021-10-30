N = int(input())

AB = []

for i in range(N-1):
    AB.append(list(map(int, input().split())))
    
cent = 0
if AB[0][0] == AB [1][0]:
    cent = AB[0][0]
if AB[0][0] == AB [1][1]:
    cent = AB[0][0]
if AB[0][1] == AB [1][0]:
    cent = AB[0][1]
if AB[0][1] == AB [1][1]:
    cent = AB[0][1]
    
for ab in AB:
    if not cent in ab:
        print("No")
        exit()
        
print("Yes")
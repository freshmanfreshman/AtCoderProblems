S = input()
T = input()

if S == T:
    print("Yes")
    exit()

for i in range(len(S)-1):
    s = ""
    s += S[0:i]
    s += S[i+1]
    s += S[i]
    s += S[i+2:len(S)]
    if s == T:
        print("Yes")
        exit()
        
print("No")
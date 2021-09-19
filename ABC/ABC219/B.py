S_list = [""] * 3
for i in range(3):
    S_list[i] = input()
    
T = input()

str = ""
for t in T:
    str += S_list[int(t)-1]
    
print(str)
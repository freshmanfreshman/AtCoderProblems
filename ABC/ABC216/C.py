N=int(input())

bin_str = bin(N)
bin_str = bin_str[2:len(bin_str)]

ans = ""
for s in bin_str:
    if s == "0":
        ans += "B"
    if s == "1":
        ans += "BA"
        
print(ans)
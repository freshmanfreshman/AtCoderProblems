def translateX(X, S):
    X_pre = "abcdefghijklmnopqrstuvwxyz"
    s = S.translate(str.maketrans({X_pre[0]:X[0]
                                   , X_pre[1]: X[1]
                                   , X_pre[2]: X[2]
                                   , X_pre[3]: X[3]
                                   , X_pre[4]: X[4]
                                   , X_pre[5]: X[5]
                                   , X_pre[6]: X[6]
                                   , X_pre[7]: X[7]
                                   , X_pre[8]: X[8]
                                   , X_pre[9]: X[9]
                                   , X_pre[10]: X[10]
                                   , X_pre[11]: X[11]
                                   , X_pre[12]: X[12]
                                   , X_pre[13]: X[13]
                                   , X_pre[14]: X[14]
                                   , X_pre[15]: X[15]
                                   , X_pre[16]: X[16]
                                   , X_pre[17]: X[17]
                                   , X_pre[18]: X[18]
                                   , X_pre[19]: X[19]
                                   , X_pre[20]: X[20]
                                   , X_pre[21]: X[21]
                                   , X_pre[22]: X[22]
                                   , X_pre[23]: X[23]
                                   , X_pre[24]: X[24]
                                   , X_pre[25]: X[25]
                                   }))
    return s

def detranslateX(X, S):
    X_pre = "abcdefghijklmnopqrstuvwxyz"
    s = S.translate(str.maketrans({X[0]:X_pre[0]
                                   , X[1]: X_pre[1]
                                   , X[2]: X_pre[2]
                                   , X[3]: X_pre[3]
                                   , X[4]: X_pre[4]
                                   , X[5]: X_pre[5]
                                   , X[6]: X_pre[6]
                                   , X[7]: X_pre[7]
                                   , X[8]: X_pre[8]
                                   , X[9]: X_pre[9]
                                   , X[10]: X_pre[10]
                                   , X[11]: X_pre[11]
                                   , X[12]: X_pre[12]
                                   , X[13]: X_pre[13]
                                   , X[14]: X_pre[14]
                                   , X[15]: X_pre[15]
                                   , X[16]: X_pre[16]
                                   , X[17]: X_pre[17]
                                   , X[18]: X_pre[18]
                                   , X[19]: X_pre[19]
                                   , X[20]: X_pre[20]
                                   , X[21]: X_pre[21]
                                   , X[22]: X_pre[22]
                                   , X[23]: X_pre[23]
                                   , X[24]: X_pre[24]
                                   , X[25]: X_pre[25]
                                   }))
    return s

X = input()
N = int(input())
S_list = [""]*N

for i in range(N):
    s = input()
    s = translateX(X, s)
    S_list[i] = s
    
S_list = sorted(S_list)

# print()
for s in S_list:
    print(detranslateX(X, s))
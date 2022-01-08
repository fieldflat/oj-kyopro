### abc230_c.py ###
N, A, B = [int(i) for i in input().split()]
P, Q, R, S = [int(i) for i in input().split()]

# 整形
for i in range(P, Q+1):
    for j in range(R, S+1):
        if abs(A-i) == abs(B-j):
            print('#', end="")
        else:
            print('.', end="")
    print('')
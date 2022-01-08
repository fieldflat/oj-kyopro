### abc230_d.py ###
N, D = [int(i) for i in input().split()]
LR_list = []
for _ in range(N):
    LR_list.append([int(i) for i in input().split()])

LR_list.sort(key=lambda x: x[1])
x, ans = - 10**9, 0
for t in LR_list:
  if t[0] >= x + D:
    x = t[1]
    ans += 1
print(ans)


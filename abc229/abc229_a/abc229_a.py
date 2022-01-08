### abc229_a.py ###
s1 = input()
s2 = input()
f = "Yes"
if s1[0] == "#" and s1[1] == "." and s2[1] == "#" and s2[0] == ".": f = "No"
if s1[1] == "#" and s1[0] == "." and s2[0] == "#" and s2[1] == ".": f = "No"
print(f)
import copy
inputs = '2 3 5 1000'
tmp = [int(e) for e in inputs.split()]

bases = tmp[:-1]
k = tmp[-1]


dic_values = {}
dic_used = {}
dic_cand = {}

initial_key = (0, 0, 0)
initial_value = 1

dic_cand[initial_key] = initial_value
dic_values[initial_key] = initial_value

idx = 1
while True:
    key, value = min(dic_cand.items(), key=lambda x: x[1])
    del dic_cand[key]
    if idx == k:
        break

    idx += 1

    for i, base in enumerate(bases):
        key_n = list(copy.copy(key))
        key_n[i] += 1
        if tuple(key_n) in dic_cand: continue

        dic_cand[tuple(key_n)] = value * base

print(value)
    

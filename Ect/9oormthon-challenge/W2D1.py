N = int(input())
S = input()

comb = []
comb_list = []
result = []

for i in range(N):
    for j in range(i+1,N): # N이 4고 i가 2,3 일때 j와 k에 해당하는 반복문은 조건에 의하여 돌지 않는다.
        for k in range(j+1,N):
            if (S[:i+1] + S[j:k] + S[k:]) != S :
                continue # 연속되지 않는 이상한 조합이 나오는 경우가 있어 (예를 들면 abcd를 입력했는데 {a,c,d} 같은 조합) 이 경우를 걸러주었다.
            comb_list.append(S[:i+1])
            comb_list.append(S[j:k])
            comb_list.append(S[k:])
            comb.append([S[:i+1],S[j:k], S[k:]])

P = sorted(set(comb_list))
P_map = {
    s:index+1 for index,s in enumerate(P)
}

for el in comb:
    sum_res = 0
    for i in range(3):
        sum_res += P_map[el[i]]
    result.append(sum_res)

print(max(result))
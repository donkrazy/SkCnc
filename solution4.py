def solution(truck, w):
    answer = []
    prev_w = 9999999999
    prev_idx = -1
    for k  in range(len(w)):
        flag = False
        weight = w[k]
        if weight >= prev_w:
            from_index = prev_idx
        else:
            from_index = 0

        for i in range(from_index, len(truck)):
            if weight > truck[i]:
                continue
            else:
                truck[i] -= weight
                answer.append(i+1)
                prev_idx = i
                flag = True
                break
        if not flag:
            prev_idx = -1
            answer.append(-1)
        prev_w = weight
    return answer

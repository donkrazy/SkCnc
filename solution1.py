def solution(N):
    even_list = {}
    odd_list = {}
    for i in range(10):
        count =  N.count(str(i))
        if count == 0:
            continue
        elif count % 2 == 0:
            even_list[str(i)] = count
        else:
            odd_list[str(i)] = count
    
    n = 0
    if len(odd_list) == 0:
        a =1
    elif len(even_list) == 1 and '0' in even_list:
        b = 1
    else:
        n += sum([ odd_list[i]-1 for i in odd_list.keys() ]) + 1
    n += sum([even_list[i] for i in even_list.keys()])
            
    return n

def solution(board, nums):
    length = len(board)
    check = [1] * length * 2
    diag_1 = 1
    diag_2 = 1
    
    for i in range(length):
        for j in range(length):
            item = board[i][j]
            if item in nums:
                continue 
            
            if i == j:
                diag_1 = 0
            if i + j == length-1:
                diag_2 = 0
                    
            check[i] = 0
            check[length+j] = 0
        
    return sum(check) + diag_1 + diag_2

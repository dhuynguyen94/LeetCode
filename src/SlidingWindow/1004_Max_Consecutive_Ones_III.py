def longestOnes(self, A: List[int], K: int) -> int:
    max_len = 0
    start = 0
        
    for end in range(len(A)):
        if A[end] == 0:
            K -= 1
        max_len= max(max_len, end-start)
        while K < 0:
            if A[start] == 0:
                K += 1
            start += 1
                
    return max(max_len, len(A) - start)

    #Time Complexity: O(n)
    # Space Complexity: O(1)
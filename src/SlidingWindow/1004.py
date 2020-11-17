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

#Second solution following template
def longestOnes2(self, a: List[int], K: int) -> int:
    i = 0
    counter = 0
    res = 0
    for j in range(0, len(a)):
        if a[j] == 0:
            counter += 1
        while ( counter > K ): #check invalid
            if ( a[i] == 0 ):
                counter -= 1
            i += 1
        #valid: update result
        res = max(res, (j-i+1))
    return res
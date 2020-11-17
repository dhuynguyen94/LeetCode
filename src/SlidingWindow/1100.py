class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        counter = Counter(S[:K]) # get 1st window
        ans = 0
        for i in range(K, len(S)):
            if len(counter) == K: # Satisfy requirement
                ans += 1
            counter[S[i-K]] -= 1  # Update freq
            counter[S[i]] += 1    # Slide to the right
            if counter[S[i-K]] == 0: # Delete entry if freq == 0
                del counter[S[i-K]]
        return ans + int(len(counter) == K)

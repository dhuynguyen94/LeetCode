class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        ans = 0
        for word in words:
            word_counter = Counter(word)
            if all(word_counter[c] <= chars_counter[c] for c in word):
                ans += len(word)
        return ans


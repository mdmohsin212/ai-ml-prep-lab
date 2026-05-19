class Solution:
    def find_al(self, word, rows):
        for row in rows:
            if all(char.lower() in row for char in word):
                return word

    def findWords(self, words: List[str]) -> List[str]:
        s = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []

        for word in words:
            result = self.find_al(word, s)
            if result:
                ans.append(result)

        return ans
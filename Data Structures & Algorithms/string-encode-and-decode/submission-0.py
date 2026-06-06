class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # 2. Find where the next '#' is located
            j = s.find('#', i)
            # 3. Read the number before the '#' to get the length
            length = int(s[i:j])
            # 4. Jump past the '#' and grab exactly that many characters
            res.append(s[j + 1 : j + 1 + length])
            # 5. Move our pointer to the start of the next encoded block
            i = j + 1 + length
        return res
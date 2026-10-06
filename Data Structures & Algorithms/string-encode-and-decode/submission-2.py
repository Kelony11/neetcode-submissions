class Solution:

    def encode(self, strs: List[str]) -> str:
        full_string = ''
        for i in strs:
            full_string += str(len(i)) + "#" + i
        return full_string

    def decode(self, s: str) -> List[str]:
        
        word_list = []
        
        left = 0
        while left < len(s):

            right = left
            while s[right] != "#":
                right += 1
            else:
                length = int(s[left:right])
                left = right + 1
                right = left + length
                word_list.append(s[left:right])
                left = right

        return word_list



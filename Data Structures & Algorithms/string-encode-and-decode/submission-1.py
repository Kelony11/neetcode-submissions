class Solution:
    def encode(self, strs: List[str]) -> str:

        word = ""
        for i in strs:
            word += str(len(i)) + "#" + i
        return word

    def decode(self, s: str) -> List[str]:

        l = 0
        word_list = []
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            word_list.append(s[l:r])
            l = r
        return word_list

             
            
            

        























# def encode(self, strs: List[str]) -> str:
#         full_string = ''
#         for i in strs:
#             full_string += str(len(i)) + '*' + i
#         return full_string

#     def decode(self, s: str) -> List[str]:

#         string_list = []

#         first_index = 0

#         while first_index < len(s):

#             second_index = first_index 
#             while s[second_index] != "*":
#                 second_index += 1
#             length_per_string = int(s[first_index:second_index])
#             first_index = second_index + 1
#             second_index = length_per_string + first_index
#             string_list.append(s[first_index:second_index])
#             first_index = second_index

#         return string_list






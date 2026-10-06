class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def_dict = defaultdict(list)

        for i in strs:
            group_word = "".join(sorted(i))
            def_dict[group_word].append(i)

        return def_dict.values()

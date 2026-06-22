class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mappings = {}
        sol = []

        for i in strs:
            tmp = str(sorted(i))
            if tmp in mappings:
                ####
                mappings[tmp].append(i)
            else:
                mappings[tmp] = []
                mappings[tmp].append(i)
        for x in mappings:
            sol.append(mappings[x])
        return(sol)



        
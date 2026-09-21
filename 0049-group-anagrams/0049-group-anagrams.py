from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        # hashh = defaultdict(int)
        # lst = []
        # # while ch in strs[i]
        # #     if strs[].count(ch) != strs[].count(ch)

        # for i  in range(len(strs)):
        #     for j in range(i+1,len(strs)):
        #         if len(strs[i]) == len(strs[j]):    
        #             for ch in strs[i]:
        #                 hashh[ch] +=1

        #             for hc in strs[j]:
        #                 if hc not in hashh or hc == 0:
        #                     continue
        #                 hashh[ch] -=1 

        #             lst.append([[strs[i]],strs[j]]) 
        #         else:
        #             lst.append([strs[i]])
        #             lst.append([strs[j]])

        # return lst       

        hashh = defaultdict(list)

        for ch in strs:
            key = "".join(sorted(ch))
            hashh[key].append(ch)

        return list(hashh.values())
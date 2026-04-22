class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}

        for s in strs:
            count= [0]*26

            for chars in s:
                count[ord(chars)- ord("a")] += 1

            key = tuple(count)

            if key not in dict1:
                dict1[key] =[]
            dict1[key].append(s)
            
        return list(dict1.values())


        
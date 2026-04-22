class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}

        for i in s:
            dict1[i]= dict1.get(i , 0)+1
        
        for i in t:
            if i not in dict1:
                return False
            else:
                dict1[i] -=1
            
        for i in dict1.values():
            if i!= 0:   
                return False
        return True

        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        newList = []

        for i in strs:
            countArr = {}
            for x in i:

                if x in countArr:
                    countArr[x] += 1
                else:
                    countArr.update({x: 1})
            
            newList.append(countArr)

        result = []

        for i in newList:
            newList.remove(i)
            group = [i]
            for c in newList:
                if i == c:
                    group.append(c)
            
            result.append(group)

        print(result)

  # in progress

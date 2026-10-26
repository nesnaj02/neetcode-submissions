class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in answer:
                answer[key].append(word)
            else:
                answer[key] = [word]
        return list(answer.values())
        
        
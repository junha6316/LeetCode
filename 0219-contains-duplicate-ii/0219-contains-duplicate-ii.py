class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if hash_map.get(num, None) is None:
                hash_map[num] = [i]
            else:
                hash_map[num].append(i)
        
        for key in hash_map.keys():
            if len(hash_map[key]) == 1:
                continue
            
            for i in range(len(hash_map[key])):
                for j in range(i+1, len(hash_map[key])):
                    idx_i = hash_map[key][i]
                    idx_j = hash_map[key][j]
                    if abs(idx_j - idx_i) <= k:
                        return True
        
        return False
                
        
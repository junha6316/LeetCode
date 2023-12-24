class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        N = len(nums)
        answer = set()
        for i in range(N):
            for a in self.twoSum(i):
                answer.add(a)
                
        return list(answer)
            
    
    def twoSum(self, x):
        tmp = self.nums[x:]
        
        l = x + 1
        r = len(self.nums) -1
        tmp_answer = []
        while l < r:
            summ = self.summ(x,l,r)
            if summ == 0:
                tmp_answer.append((self.nums[x], self.nums[l], self.nums[r],))
            if summ < 0:
                l +=1
            else:
                r -= 1
                
        return tmp_answer
                
                
            
            
    
    def summ(self, x,y,z):
        return self.nums[x] + self.nums[y] + self.nums[z]


 
                
            
        
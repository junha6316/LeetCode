import heapq as hq
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] +=1

    def pop(self) -> None:
        if self.min_stack[-1][0] == self.stack[-1]:
            if self.min_stack[-1][1] > 1:
                self.min_stack[-1][1] -= 1
            else:
                self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1][0]
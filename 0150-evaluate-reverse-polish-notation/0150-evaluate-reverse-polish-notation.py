class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        numbers= {str(i) for i in range(-200, 201)}
        while tokens:
            tkn = tokens.pop(0)
            
            
            if tkn not in numbers:
                num1 = stk.pop()
                num2 = stk.pop()
                if tkn == "+":
                    tmp = num1 + num2
                elif tkn == "-":
                    tmp = num2- num1 
                elif tkn == "*":
                    tmp = num1 * num2
                elif tkn == '/':
                    
                    tmp = int(float(num2) / float(num1))
                    
                    
                    
                    
                stk.append(tmp)
            else:
                stk.append(int(tkn))
            
                
        return stk[0]
                    
                    
            
                
                    
        
        
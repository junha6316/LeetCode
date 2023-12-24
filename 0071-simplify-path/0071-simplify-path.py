class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        for arg in path.split("/"):
            if not arg:
                continue
                
            if arg == ".." :
                # /home/..
                if len(answer) >0:
                    answer.pop()
            elif arg == ".":
                continue
                
            else:
                answer.append(arg)
            
            
                

        return "/" +"/".join(answer)
        
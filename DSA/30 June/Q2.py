class Solution(object):
    def isValid(self, s):
        l=[]
        for i in s:
            try:

                if i in "({[":
                    l.append(i)
                elif i in ")}]":
                    if i==')' and l[-1]=='(':
                        l.pop()
                    elif i=='}' and l[-1]=='{':
                        l.pop()
                    elif i==']' and l[-1]=='[':
                        l.pop()
                    else:
                        return False
            except:
                return False
            # if i=="(":
            #     l1.append('(')
            # elif i=='{':
            #     l2.append('{')
            # elif i=='[':
            #     l3.append('[')
            # elif i==')':
            #     try:
            #         l1.pop() 
            #     except:
            #         return False  
            # elif i=='}':
            #     try:
            #         l2.pop() 
            #     except:
            #         return False
            # elif i==']':
            #     try:
            #         l3.pop() 
            #     except:
            #         return False
                    
        if not l:
            return True
        else:
            return False
            
            
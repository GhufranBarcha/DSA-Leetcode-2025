class Solution:
    def reverse(self, x: int) -> int:
        if x >= (2**31 - 1) and x <= (-2**31):
            return 0
        signed = 1
        if x < 0:
            signed = -1

        x = abs(x)
        x = int(str(x)[::-1]) * signed
        if x >= (-2**31) and x <= (2**31  -1):
            return x
        else:
            return 0   
        
        

            
        
        
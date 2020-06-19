import math
def solution(k):
    # Your code here
    s = ""
   
    for num in range(2,100000):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            s = s+ str(num)
    
    new_id = ""
    for i in range(k, k+5):
        new_id += s[i]
    
    return new_id[:5]

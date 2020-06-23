def solution(l):
    # Your code here
    # l = list(l)
    # return sorted(l)
    return sorted(l, key=lambda x: map(int, x.split('.')))
    

#1356 유진수
def find(n): 
    for i in range(len(n)-1):
        left,right = 1,1
        for j in range(i+1):
            left *= int(n[j])
        for j in range(i+1,len(n)):
            right *= int(n[j])
        if left == right: 
            return True
    return False
n = input()
if find(n): print('YES')
else: print('NO')

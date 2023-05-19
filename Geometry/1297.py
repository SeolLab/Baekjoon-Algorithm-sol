## 1297 TV 크기
import math
d,h,w = map(int,input().split())
x = d / math.sqrt(h**2 + w**2)
print(int(x*h),int(x*w))

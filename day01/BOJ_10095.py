# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 
# 각 줄에 A와 B가 주어진다. A와 B는 콤마(,)로 구분되어 있다. (0 < A, B < 10)
while True:
    a,b = map(int,input().split())

    if (a,b) ==(0,0):
         break
    else:
         print(a,b)
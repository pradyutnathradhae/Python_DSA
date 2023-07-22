arrs = [int(x) for x in input().split(' ')]
reqd_sum = int(input())

arrs.sort()
flag = False
left = 0
right = len(arrs)-1
while left < right:
    temp = arrs[left]+arrs[right]
    if temp > reqd_sum:
        right = right -1
    elif temp < reqd_sum:
        left = left + 1
    else:
        flag = True
        break

if flag:
    print("Required Sum Present!")
else:
    print("Required Sum Not Present!")
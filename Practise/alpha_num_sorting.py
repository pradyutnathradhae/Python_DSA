n = int(input())
for i in range(n):
    line = input()
    arr = line.split(" ")
    nos = [int(arr[i]) for i in range(len(arr)) if i%2==1]
    strs = [arr[i].lower() for i in range(len(arr)) if i%2==0]
    nos.sort()
    strs.sort()
    for i in range(len(nos)-1):
        print(strs[i],nos[i],sep=' ',end=' ')
    print(strs[len(nos)-1],nos[len(nos)-1],sep=' ',end='\n')

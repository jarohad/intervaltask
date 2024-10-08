from collections import deque
interval = input().split(',')
# interval = '1-5,6,8-9,11'.split(',')
dq = deque()
for i in interval:
    dq.append(i)
new_str = ''
new_str1 = ''
for j in range(len(dq)):
    d = dq.popleft()
    if d.find('-') != -1:
        new_str = d[:d.find('-')]
        for elem in range(int(d[:d.find('-')]), int(d[d.find('-')+1:])):
            new_str += str(elem+1)
        new_str1 += new_str
    elif d.find('-') == -1:
        new_str1 += str(d)
print(new_str1)


a = int(input())
ans = ""
length = len(str(a))
first = str(a)[:length//2]
last  = str(a)[:(length//2)-1:-1]
sum_lst = list(map(lambda i, j: int(i)+int(j), first,last))
for i in sum_lst:
    ans +=str(i)

print(ans)

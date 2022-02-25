n1 = int(input())
n2 = int(input())
count = 0

if n1 < n2 :
    for i in range(n1, n2+1):
        n = len(str(i))
        b = True
        for j in range(1,n):
            if str(i)[j] == str(i)[0]:
                b = False
                break
            else:
                pass
        if b == True:
            count+=1
        else:
            pass


print(count)

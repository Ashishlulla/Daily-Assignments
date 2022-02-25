def is_prime(num):
    factors = [i for i in range(2,num) if num % i == 0]
    if len(factors) == 0:
        return True
    else:
        return False


num = int(input())
add = 0
for i in str(num):
    if is_prime(int(i)):
        add +=int(i)
    else:
        pass

print(add)

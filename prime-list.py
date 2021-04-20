import math

prime_list = []
def is_prime(n):
    if n <= 1:
        print('n <= 1:false')
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        hoge = int(math.sqrt(n))
        print('hoge:',hoge)
        # print(i)
        print('n:',n)
        if n % i == 0:
            print('false')
            return False
        print('true')
    return True
        
for x in range(1, 201):
    print(x)
    if is_prime(x) == True:
        prime_list.append(x)
print('素数：',prime_list)


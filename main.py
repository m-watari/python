import math

# prime_list = []
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
        
# for x in range(1, 201):
#     if is_prime(x) == True:
#         prime_list.append(x)
# print('素数：',prime_list)

# ノーマルパターン
def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False
        
    for i in range(2, num):
        if num % i == 0:
            return False
            
    return True

    
# 平方根パターン
def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False
    
    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True
    
# 平方根パターン微調整
def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False
        
    if num == 2:
        return True
        
    if num == 3:
        return True
        
    if num == 4:
        return False
        
    if num == 5:
        return True
    
    for i in range(2, math.floor(math.sqrt(num) + 2)):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    import time
    import random
    
    numbers = [random.randint(0, 1000) for _ in range(100000)]
    start = time.time()
    for num in numbers:
        is_prime_v1(num)
    print('v1', time.time() - start)
    
    numbers = [random.randint(0, 1000) for _ in range(100000)]
    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print('v2', time.time() - start)
    
    numbers = [random.randint(0, 1000) for _ in range(100000)]
    start = time.time()
    for num in numbers:
        is_prime_v3(num)
    print('v3', time.time() - start)
    


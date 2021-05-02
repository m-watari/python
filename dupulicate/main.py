#[1,3,3,5,5,7,7,10,12,12,15] => [1,3,5,7,10,12,15]

# l = [1,3,3,5,5,7,7,10,12,12,15]
# print(list(set(l)))
# print(list(dict.fromkeys((l))))
# for ll in l:
#     print(ll)
# print([n for i, n in enumerate(l) if n not in l[:i]])

from typing import List

def delete_duplicate_v1(numbers: List[int]) -> None:
    temp = []
    for num in numbers:
        if num not in temp:
            temp.append(num)
    numbers[:] = temp
    
def delete_duplicate_v2(numbers: List[int]) -> None:
    temp = [numbers[0]]
    # i, len_num = 0, len(numbers) - 1
    i = 0
    len_num = len(numbers) - 1
    print(len_num)
    while i < len_num:
        if numbers[i] != numbers[i+1]:
            temp.append(numbers[i+1])
        i += 1
    numbers[:] = temp    
    
if __name__ == '__main__':
    l = [1,3,3,5,5,7,7,10,12,12,15]
    delete_duplicate_v2(l)
    print(l)
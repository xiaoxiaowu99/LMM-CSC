import random

def distribute_numbers(lst):
    # 计算分配的数量
    total_numbers = len(lst)
    distribute_A_count = int(total_numbers * 0.5)
    distribute_B_count = int(total_numbers * 0.4)
    distribute_C_count = int(total_numbers * 0.1)

    # 随机分配数字
    list_A = random.sample(lst, distribute_A_count)
    lst = [num for num in lst if num not in list_A]
    list_B = random.sample(lst, distribute_B_count)
    lst = [num for num in lst if num not in list_B]
    list_C = random.sample(lst, distribute_C_count)

    return list_A, list_B, list_C

# 示例用法
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_A, list_B, list_C = distribute_numbers(numbers)
print("List A:", list_A)
print("List B:", list_B)
print("List C:", list_C)

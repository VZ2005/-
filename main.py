def find_unique_number(num_list):
    if not num_list:
        return None
    elif len(num_list) == 1:
        return num_list[0]
    else:
        num_count = {}  #使用字典 num_count 来统计每个数字在列表中出现的次数。
        for num in num_list:
            num_count[num] = num_count.get(num, 0) + 1
        for num, count in num_count.items():   #遍历字典 num_count，找到出现次数为 1 的数字并返回。
            if count == 1:   #如果遍历完字典没有找到出现次数为 1 的数字，则返回 None。
                return num
        return None

# 将输入的整数转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique_number(numbers))
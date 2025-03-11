def find_unique_number(num_list):
    if not num_list:
        return None
    elif len(num_list) == 1:
        return num_list[0]
    else:
        num_count = {}  #使用字典 num_count 来统计每个数字在列表中出现的次数。
        for num in num_list:
            num_count[num] = num_count.get(num, 0) + 1

        #get() 是字典的一个方法。它的作用是根据键（这里的键就是 num）来获取对应的值。
        '''它有两个参数,第一个参数是要查找的键（即 num）,第二个参数是当键不存在时返回的默认值（这里设置为 0）
        如果 num 已经作为键存在于字典 num_count 中，那么 num_count.get(num, 0) 会返回对应的值；
        如果 num 不存在于字典 num_count 中，那么 num_count.get(num, 0) 会返回 0。'''

        for num, count in num_count.items():   #遍历字典 num_count，找到出现次数为 1 的数字并返回。
            if count == 1:   #如果遍历完字典没有找到出现次数为 1 的数字，则返回 None。
                return num
        return None

# 将输入的整数转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique_number(numbers))

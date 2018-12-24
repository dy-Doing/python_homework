import random
from copy import *


def sort_data(input_data):
    data = deepcopy(input_data)
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key
    return data


origin_data = list(range(1, 10))
print("生成数:{name}".format(name=origin_data))
random.shuffle(origin_data)
print("洗牌后随机数:{name}".format(name=origin_data))
sorted_data = sort_data(origin_data)
print("排序后:{id}".format(id=sorted_data))



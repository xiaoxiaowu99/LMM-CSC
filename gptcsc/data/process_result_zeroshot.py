import os
import openai
import time

from tqdm import tqdm

#读取数据集
result_path = 'sighan_result_0.05_bench.txt'
label_path = 'sighan15_new_data.txt'
output_path = 'few_shot_t0.05.txt'
all_label_data = {}
all_results = {}

with open(label_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split('$')
        id = line[0][3:]
        label = line[2][4:]
        length = line[3][8:]
        length = length.replace('\n', '', 1)
        # one_data = label + str(length)
        data = {id: label}
        all_label_data.update(data)

with open(result_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    i = 1
    for line in lines:
        if i % 2 == 1:
            id = line
            id = id.replace('\n', '', 1)
        if i % 2 == 0:
            pre = line
            pre = pre.replace('\n', '', 1)
            length = len(pre)
            # pre = pre + str(length)
            data = {id: pre}
            all_results.update(data)
        i = i + 1

for item in all_results.items():
    id = item[0]
    predict = item[1]
    label = all_label_data[id]
    with open(output_path, 'a', encoding='utf-8') as writer:
        writer.write(id)
        writer.write('\n')
        writer.write(predict)
        writer.write('\n')
        writer.write(label)
        writer.write('\n')










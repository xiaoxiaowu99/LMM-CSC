import os
import openai
import time
from bench_function import get_api_key
from tqdm import tqdm

from gptcsc.openai1 import OpenaiAPI

openai.api_key = "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"

#读取数据集
path = 'output\data_by_ours_938.txt'#6.9日改动
output_path = 'output\data_by_ours_938_zeroshot.txt'
all_data = {}
all_results = {}
prompt = "请将下列句子的拼写错误改正，句子长度不变，改动最小：\n"
#example1 = '请你输人。->请你输入。\n'
#example2 = '我明天有事晴。->我明天有事情。\n'
#example3 = '我以前想要高诉你，可是我忘了，我真户秃。->我以前想要告诉你，可是我忘了，我真糊涂。\n'
#with open(path, 'r', encoding='utf-8') as f:
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    id = 1
    i=1
    csc_data = 2
    ori_data = 3
    for line in lines:
        if i==1:
            id = line
            id = id.replace('\n', '', 1)

        if i % 2 == 1:
            id = line
            id = id.replace('\n', '', 1)
        if i % 2 == 0:
            question = line
            question = question.replace('\n', '', 1)
            # content = prompt + example1 + example2 + example3 + question + '->'
            #content =prompt +  question   #6.9日改动代码
            content =prompt
            data = {id: content}
            all_data.update(data)
        i = i + 1

openai_api_key_file = "data\openai_api_list.txt"
openai_api_key_list = get_api_key(openai_api_key_file, start_num=0, end_num=1)
model_name = 'gpt-3.5-turbo'
model_api = OpenaiAPI(openai_api_key_list, model_name='gpt-3.5-turbo')

for item in tqdm(all_data.items()):
    id = item[0]
    content = item[1]
    # prompt = content[0:99]
    prompt = ''
    # question = content[100:]
    question = "请将下列句子的拼写错误改正，句子长度不变，改动最小：\n" + content
    model_output = model_api(prompt, question)
    # completion = openai.ChatCompletion.create(
    #               model="gpt-3.5-turbo",
    #               messages=[
    #                 {"role": "user", "content": content}
    #               ]
    #             )
    # reply = completion.choices[0].message['content']
    result = {id: model_output}
    all_results.update(result)
    with open(output_path, 'a',encoding='utf-8') as writer:
        writer.write(id)
        writer.write('\n')
        writer.write(model_output)
        writer.write('\n')
    time.sleep(18)  # 休眠2秒
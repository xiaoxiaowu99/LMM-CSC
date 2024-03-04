import os
import openai
import time
from bench_function import get_api_key
from tqdm import tqdm

from gptcsc.openai1 import OpenaiAPI

openai.api_key = "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"

#读取数据集
path = 'data\SST-2.txt'
output_path = 'output\SST-result.txt'
all_data = {}
all_results = {}
# prompt = '请指出下列句子中哪个字是错别字，可以改成什么字：\n句子1：请你输人。\n错别字：人\n正确字：入\n句子2：我明天有事晴。' \
#          '\n错别字：晴\n正确字：情\n句子3：我以前想要高诉你，可是我忘了。我真户秃。\n错别字：高、户、秃\n正确字：告、糊、涂'
# '句子1：一般的美缝施工大致报价如。\n' \
         # '句子1纠正结果：将“如”改为“如下”\n' \
         # '句子2：一般室内环境采用200系列材质即可，室外需环境使用304等材质，而在酸碱性地方或沿海地区一般要使用316以上材质。\n' \
         # '句子2纠正结果：将“需环境”改为“环境需”\n' \
         # '句子3：本着用户至上，信誉第一为原则，我们不断追求技术创新，竭诚为您服务。\n' \
         # '句子3纠正结果：将“为”改为“的”\n' \
# '句子6：据了解，在现场捞鱼的人大都都来自外地，其中有不少人竟然从河北远道而来。\n' \
# '句子6纠正结果：“都都”改为“都”\n' \
prompt = 'Please judge whether the following sentences are positive or negative:'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    id = 1
    for line in lines:
        content = line.split('\t')
        question = content[0]
        label = content[1]
        data = {id: content}
        all_data.update(data)
        id = id + 1

openai_api_key_file = "data\openai_api_list.txt"
openai_api_key_list = get_api_key(openai_api_key_file, start_num=2, end_num=3)
model_name = 'gpt-3.5-turbo'
model_api = OpenaiAPI(openai_api_key_list, model_name='gpt-3.5-turbo')

for item in tqdm(all_data.items()):
    id = item[0]
    content = item[1][0]
    # prompt = content[0:99]
    # question = content[100:]
    model_output = model_api(prompt, content)
    result = {id: model_output}
    all_results.update(result)
    with open(output_path, 'a',encoding='utf-8') as writer:
        writer.write(str(id))
        writer.write('\n')
        writer.write(model_output)
        writer.write('\n')
    time.sleep(20)  # 休眠2秒
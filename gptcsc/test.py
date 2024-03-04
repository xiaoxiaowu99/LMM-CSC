import os
import openai
import time

from gptcsc.bench_function import get_api_key
from gptcsc.openai1 import OpenaiAPI

openai.api_key = "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"

#读取数据集
path = 'data\sighan_data.txt'
output_path = 'output\sighan_result.txt'
all_data = {}
all_results = {}
openai_api_key_file = "data\openai_api_list.txt"
openai_api_key_list = get_api_key(openai_api_key_file, start_num=0, end_num=1)
model_name = 'gpt-3.5-turbo'
model_api = OpenaiAPI(openai_api_key_list, model_name='gpt-3.5-turbo')
# prompt1 = "请替换下列句子的错别字,改动最小\n"
# prompt2 = "不可以改变句子长度\n"
# example1 = '请你输人。->请你输入。\n'
# example2 = '我明天有事晴。->我明天有事情。\n'
# example3 = '我以前想要高诉你，可是我忘了，我真户秃。->我以前想要告诉你，可是我忘了，我真糊涂。\n'
# example4 = '他们看了一个很可爱的电影，一个小机一个人去火星。->他们看了一个很可爱的电影，一个小鸡一个人去火星。\n'
# question = '他正要喝点水，老师就进教师来来了。->'
prompt = '请指出下列句子中哪个字是错别字，可以改成什么字：\n句子1：请你输人。\n错别字：人\n正确字：入\n句子2：我明天有事晴。' \
         '\n错别字：晴\n正确字：情\n句子3：我以前想要高诉你，可是我忘了。我真户秃。\n错别字：高、户、秃\n正确字：告、糊、涂'
fewshot_all = 31.1+14.8+43.5+46.2+25.7+59.2+67.7+40.9+81.1+53.9+41.5+86.3+63.8+57.6+52.4+44+33.5+31.3+5.9
fewshot_avg = fewshot_all/19
print('fewshot_avg: ')
print(fewshot_avg)
zeroshot_all = 31.9+26.4+35.0+41.0+24.4+52.6+65.4+42.7+81.1+44.2+39.0+84.9+59.8+59.7+52.9+38.7+33.0+36.5+7.6
zeroshot_all_avg = zeroshot_all/19
print('zeroshot_all_avg: ')
print(zeroshot_all_avg)
fewshot_COT_all = 60.6+30.1+38.9+38.6+25.2+52.2+57.6+65+78.2+51.5+37.8+84.6+61.8+58.4+50+33.8+36.5+31.6+8.5
fewshot_COT_all_avg = fewshot_COT_all/19
print('fewshot_COT_all_avg: ')
print(fewshot_COT_all_avg)
zeroshot_COT_all = 55.9+31.9+39.9+38.9+22.6+52.6+62.1+70.9+77.7+45.6+33.7+84.3+55.8+50.2+42.4+33.8+29.5+33.3+5.1
zeroshot_COT_all_avg = zeroshot_COT_all/19
print('zeroshot_COT_all_avg: ')
print(zeroshot_COT_all_avg)



question = '请指出下列句子中哪个字是错别字，可以改成什么字：\n句子4:可是你现在不在宿舍，所以我留了一枝条。'
content = prompt + question
model_output = model_api(prompt, question)
# content = prompt1 + prompt2 + example1 + example2 + example3 + question + '->'
# completion = openai.ChatCompletion.create(
#                   model="gpt-3.5-turbo",
#                   messages=[
#                     {"role": "user", "content": content}
#                   ]
#                 )
# reply = completion.choices[0].message['content']
# print(reply)

print(model_output)


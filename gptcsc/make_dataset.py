import pickle

from tqdm import tqdm

from gptcsc.bench_function import get_api_key
from gptcsc.openai1 import OpenaiAPI

input_path = 'data/train.pkl'
output_path = 'data/all_train_gpt_check.txt'

openai_api_key_file = "data\openai_api_list.txt"
openai_api_key_list = get_api_key(openai_api_key_file, start_num=0, end_num=1)
model_name = 'gpt-3.5-turbo'
model_api = OpenaiAPI(openai_api_key_list, model_name='gpt-3.5-turbo')
prompt = "下列句子是否存在语法错误：\n句子1：日产汽车的总裁高森说，由于钢铁短缺，这家全日本第二大的汽车厂也许将被迫在明年三月减少国内厂产量一万五千台。回答：无错误" \
         "\n句子2：对不起，最近我很忙，所以我不会去你的。回答：有错误。\n句子3：中东在过去十七个月间一直陷于暴力冲突之中。回答：无错误。"
all_data = {}
with open(input_path, 'rb') as f:
    data = pickle.load(f)
    for i in tqdm(range(len(data))):
        id = data[i]['id']
        src = data[i]['src']
        tgt = data[i]['tgt']
        question = "下列句子是否存在语法错误：\n" + tgt
        model_output = model_api(prompt, question)
        with open(output_path, 'a', encoding='utf-8') as writer:
            writer.write('id:' + id)
            writer.write('\n')
            writer.write('是否有错：' + model_output)
            writer.write('\n')
            writer.write('src:' + src)
            writer.write('\n')
            writer.write('tgt:' + tgt)
            writer.write('\n')



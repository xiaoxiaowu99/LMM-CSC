import json
import os
import random

def count_words(sentence):
    # 使用split()方法将句子按空格分割成单词列表
    words = sentence.split()
    # 返回单词列表的长度
    return len(words)


def count_chinese_characters(text):
    count = 0
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            count += 1
    return count

# 字符15%一定被替换
def replace_english_characters(text, replacement_rate):
    words = text.split()
    num_words = len(words)
    need_num_replacements = int(num_words * replacement_rate)

    replaced_indices = random.sample(range(num_words), need_num_replacements)
    for idx in replaced_indices:
        word = words[idx]
        position = random.randint(0, len(word))
        letter = chr(random.randint(97, 122))  # 生成随机小写字母
        new_word = word[:position] + letter + word[position:]
        words[idx] = new_word
    new_sentence = " ".join(words)

    return new_sentence, need_num_replacements

def get_all_filenames(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


replacement_rate = 0.05

ori_filename = 'aqua-rat.few-shot.jsonl'
noise_filename_json = 'aqua-rat.few-shot.jsonl'
# noise_filename_txt = '2012-2022_English_Cloze_Test.txt'
ori_data_dir = './data/v1/'
noise_data_dir = './data/v1_noise/'

file_list = get_all_filenames(ori_data_dir)

def make_json_data(one_file_path):
    all_content = []
    with open(one_file_path, 'rb', ) as file:
        # if 'few-shot' in one_file_path:
        #     for line in file.readlines():
        #         dic = json.loads(line)
        #         for i in range(len(dic['context'])):
        #             if dic['context'][i]['role']=='user':
        #                 content = dic['context'][i]['content']
        #                 new_content, num_replacements = replace_english_characters(content, replacement_rate)
        #                 dic['context'][i]['content'] = new_content
        #         all_content.append(dic)
        # if 'zero-shot' in one_file_path:
        #     for line in file.readlines():
        #         dic = json.loads(line)
        #         new_content, num_replacements = replace_english_characters(dic['context'], replacement_rate)
        #         dic['context'] = new_content
        #         all_content.append(dic)
        for line in file.readlines():
            dic = json.loads(line)
            if dic['passage'] != None:
                passage = dic['passage']
                noise_data_path = one_file_path.replace('jsonl', 'txt')
                with open(noise_data_path, 'a', encoding='utf-8') as writer:
                    writer.write(passage)
                    writer.write('\n')
            if dic['question'] != None:
                question = dic['question']
                noise_data_path = one_file_path.replace('jsonl', 'txt')
                with open(noise_data_path, 'a', encoding='utf-8') as writer:
                    writer.write(question)
                    writer.write('\n')



# 写入json文件# 使用写模式，名称定义为r
def write_json_data(datas, noise_path):
    with open(noise_path, 'w', encoding='utf-8') as r:
        for item in datas:
            json.dump(item, r, ensure_ascii=False)
            r.write('\n')


# 调用两个函数，更新内容
for one_file_path in file_list:
    make_json_data(one_file_path)

# with open(os.path.join(ori_data_dir, ori_filename), 'rb', ) as f:
#     mcq_data = json.load(f, encoding='utf-8')  # 加载json文件中的内容
# with open(os.path.join(noise_data_dir, noise_filename_json), 'rb', ) as f:
#     noise_data = json.load(f, encoding='utf-8')  # 加载json文件中的内容

print(0)

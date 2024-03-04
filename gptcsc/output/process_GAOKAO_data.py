import json
import os
import random


def is_chinese_character(char):
    # 使用unicode编码范围判断是否是汉字
    if '\u4e00' <= char <= '\u9fff':
        return True
    else:
        return False


def count_chinese_characters(text):
    count = 0
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            count += 1
    return count

# 字符15%一定被替换
def replace_chinese_characters(text, replacement_rate, pinyin_ConfusionSet_data, stroke_ConfusionSet_data, random_ConfusionSet_data):
    chinese_chars = []
    pinyin_num_replacements = 0
    stroke_num_replacements = 0
    random_num_replacements = 0
    global confusion_char
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            chinese_chars.append(char)
    need_num_replacements = int(len(chinese_chars) * replacement_rate)
    pinyin_replacement_num = int(need_num_replacements * pinyin_rate)
    stroke_replacement_num = int(need_num_replacements * stroke_rate)
    random_replacement_num = int(need_num_replacements * random_rate)

    replaced_indices = random.sample(range(len(chinese_chars)), need_num_replacements)
    pinyin_replaced_indices = random.sample(replaced_indices, pinyin_replacement_num)
    replaced_indices = [num for num in replaced_indices if num not in pinyin_replaced_indices]
    stroke_replaced_indices = random.sample(replaced_indices, stroke_replacement_num)
    replaced_indices = [num for num in replaced_indices if num not in stroke_replaced_indices]
    random_replaced_indices = random.sample(replaced_indices, random_replacement_num)


    # replace pinyin confusion
    pinyin_replaced_char_list = []
    for index in pinyin_replaced_indices:
        pinyin_replaced_char_list.append(chinese_chars[index])
    for pinyin_replaced_char in pinyin_replaced_char_list:
        if pinyin_replaced_char in pinyin_ConfusionSet_data.keys():
            # if ConfusionSet_data[replaced_char]:
            index = random.randint(0, len(pinyin_ConfusionSet_data[pinyin_replaced_char]) - 1)
            confusion_char = pinyin_ConfusionSet_data[pinyin_replaced_char][index]
            pinyin_num_replacements = pinyin_num_replacements + 1
        text = text.replace(pinyin_replaced_char, confusion_char, 1)

    # replace stroke confusion
    stroke_replaced_char_list = []
    for index in stroke_replaced_indices:
        stroke_replaced_char_list.append(chinese_chars[index])
    for stroke_replaced_char in stroke_replaced_char_list:
        if stroke_replaced_char in stroke_ConfusionSet_data.keys():
            # if ConfusionSet_data[replaced_char]:
            index = random.randint(0, len(stroke_ConfusionSet_data[stroke_replaced_char]) - 1)
            confusion_char = stroke_ConfusionSet_data[stroke_replaced_char][index]
            stroke_num_replacements = stroke_num_replacements + 1
        text = text.replace(stroke_replaced_char, confusion_char, 1)

    # replace random confusion
    random_repalced_char_list = []
    for index in random_replaced_indices:
        random_repalced_char_list.append(chinese_chars[index])
    for random_replaced_char in random_repalced_char_list:
        if random_replaced_char in random_ConfusionSet_data.keys():
            # if ConfusionSet_data[replaced_char]:
            index = random.randint(0, len(random_ConfusionSet_data[random_replaced_char]) - 1)
            confusion_char = random_ConfusionSet_data[random_replaced_char][index]
            random_num_replacements = random_num_replacements + 1
        text = text.replace(random_replaced_char, confusion_char, 1)

    all_replace_num = pinyin_replacement_num + stroke_num_replacements + random_num_replacements
    return text, need_num_replacements, pinyin_num_replacements, stroke_num_replacements, random_num_replacements, all_replace_num


replacement_rate = 0.15
pinyin_rate = 0.6
stroke_rate = 0.3
random_rate = 0.1

ori_filename = 'gaokao-biology.json'
noise_filename_json = '2012-2022_English_Cloze_Test.json'
noise_filename_txt = '2012-2022_English_Cloze_Test.txt'
ori_data_dir = 'D:/LLM_CSC/GAOKAO-Bench-main/data/Multiple-choice_Questions'
noise_data_dir = 'D:/LLM_CSC/GAOKAO-Bench-main/data/Multiple-choice_Question_new_noise15%_631'
noise_data_information_dir = 'D:/LLM_CSC/GAOKAO-Bench-main/data/Multiple-choice_Question_new_noise15%_information_631/'
random_ConfusionSet_path = 'D:/LLM_CSC/gptcsc/data/cnew/same_all.txt'
pinyin_ConfusionSet_path = 'D:/LLM_CSC/gptcsc/data/cnew/same_pinyin.txt'
stroke_ConfusionSet_path = 'D:/LLM_CSC/gptcsc/data/cnew/same_stroke.txt'


# 加载pinyin混淆集
pinyin_ConfusionSet_data = {}
with open(pinyin_ConfusionSet_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        char = line[0]
        char_confusion = line[1:]
        char_confusion = char_confusion.replace('\n', '', 1)
        char_confusion = list(char_confusion)
        data = {char: char_confusion}
        pinyin_ConfusionSet_data.update(data)

# 加载stroke混淆集
stroke_ConfusionSet_data = {}
with open(stroke_ConfusionSet_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        char = line[0]
        char_confusion = line[1:]
        char_confusion = char_confusion.replace('\n', '', 1)
        char_confusion = list(char_confusion)
        data = {char: char_confusion}
        stroke_ConfusionSet_data.update(data)

# 加载random all混淆集
random_ConfusionSet_data = {}
with open(random_ConfusionSet_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        char = line[0]
        char_confusion = line[1:]
        char_confusion = char_confusion.replace('\n', '', 1)
        char_confusion = list(char_confusion)
        data = {char: char_confusion}
        random_ConfusionSet_data.update(data)


# data = json.load(open(os.path.join(model_output_dir, filename), encoding="utf-8"))['example']
# for i in range(len(data)):
#     question = data[i]['question']
#     noise_question = replace_chinese_characters(question, replacement_rate, ConfusionSet_data)
#
#     print(question)
#     print(noise_question)

# 获取json里面数据
def get_json_data():
    with open(os.path.join(ori_data_dir, ori_filename), 'rb', ) as f:
        data = json.load(f, encoding='utf-8')  # 加载json文件中的内容
        for i in range(len(data['example'])):
            ori_question = data['example'][i]['question']
            noise_question, need_num_replacements, pinyin_num_replacements, stroke_num_replacements, \
                        random_num_replacements, all_replace_num = replace_chinese_characters(ori_question,
                                                                                            replacement_rate,
                                                                                            pinyin_ConfusionSet_data,
                                                                                            stroke_ConfusionSet_data,
                                                                                            random_ConfusionSet_data)
            data['example'][i]['question'] = noise_question
            print('原题干：')
            print(ori_question)  # 打印原题干
            print('引入噪声题干：')
            print(data['example'][i]['question'])  # 打印引入noise题干
            print('题干中中文字符数：' + str(count_chinese_characters(ori_question)))  # 打印题干中中文字符数
            print('应修改字符数：' + str(need_num_replacements))
            print('实际修改字符数：' + str(all_replace_num) + '(' + '拼音相似:' + str(pinyin_num_replacements) +
                  '  字形相似：' + str(stroke_num_replacements) + '  随机替换：' + str(random_num_replacements) + ')')
            print('----------------------')
            with open(os.path.join(noise_data_information_dir, noise_filename_txt), 'a', encoding='utf-8') as writer:
                writer.write('原始题干：')
                writer.write(ori_question)
                writer.write('引入噪声的题干：')
                writer.write(data['example'][i]['question'])
                writer.write('题干中中文字符数：' + str(count_chinese_characters(ori_question)))
                writer.write('\n')  # 打印题干中中文字符数
                writer.write('应修改字符数：' + str(need_num_replacements))
                writer.write('\n')
                writer.write('实际修改字符数：' + str(all_replace_num) + '(' + '拼音相似:' + str(pinyin_num_replacements) +
                             '  字形相似：' + str(stroke_num_replacements) + '  随机替换：' + str(random_num_replacements) + ')')
                writer.write('\n')
                writer.write('\n')
    return data  # 返回修改后的内容


# 写入json文件# 使用写模式，名称定义为r
def write_json_data(datas):
    with open(os.path.join(noise_data_dir, noise_filename_json), 'w', encoding='utf-8') as r:
        json.dump(datas, r, ensure_ascii=False)


# 调用两个函数，更新内容
the_revised_dict = get_json_data()
write_json_data(the_revised_dict)

with open(os.path.join(ori_data_dir, ori_filename), 'rb', ) as f:
    mcq_data = json.load(f, encoding='utf-8')  # 加载json文件中的内容
with open(os.path.join(noise_data_dir, noise_filename_json), 'rb', ) as f:
    noise_data = json.load(f, encoding='utf-8')  # 加载json文件中的内容

print(0)

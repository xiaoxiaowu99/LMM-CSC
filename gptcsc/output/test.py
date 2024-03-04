import random


def count_chinese_characters(text):
    count = 0
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            count += 1
    return count


# def replace_chinese_characters(text, replacement_rate):
#     chinese_chars = []
#     replaced_text = ""
#     for char in text:
#         if '\u4e00' <= char <= '\u9fff':
#             chinese_chars.append(char)
#             if random.random() <= replacement_rate:
#                 replaced_text += "@"
#             else:
#                 replaced_text += char
#         else:
#             replaced_text += char
#
#     return replaced_text

def replace_chinese_characters(text, replacement_rate, ConfusionSet_data):
    chinese_chars = []
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            chinese_chars.append(char)
    num_replacements = int(len(chinese_chars) * replacement_rate)
    replaced_indices = random.sample(range(len(chinese_chars)), num_replacements)
    replaced_char_list = []
    for index in replaced_indices:
        replaced_char_list.append(chinese_chars[index])
    for replaced_char in replaced_char_list:
        if ConfusionSet_data[replaced_char]:
            index = random.randint(0, len(ConfusionSet_data[replaced_char]) - 1)
            confusion_char = ConfusionSet_data[replaced_char][index]
        text = text.replace(replaced_char, confusion_char, 1)

    return text


# 输入文章
input_text = "这是一段包含hhh中文哈哈哈哈哈啊哈哈猎杀对决艾斯欧达斯噢屌丝的示例文本。This is a sample text with Chinese characters."

# 统计汉字数量
chinese_count = count_chinese_characters(input_text)
print("汉字数量：", chinese_count)

# 加载混淆集
ConfusionSet_path = 'D:\LLM_CSC\gptcsc\data\confusion.txt'
ConfusionSet_data = {}
with open(ConfusionSet_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        char = line[0]
        char_confusion = line[2:]
        char_confusion = char_confusion.replace('\n', '', 1)
        char_confusion = list(char_confusion)
        data = {char: char_confusion}
        ConfusionSet_data.update(data)


# 替换15%的汉字为@
replacement_rate = 0.15
replaced_text = replace_chinese_characters(input_text, replacement_rate, ConfusionSet_data)
print("替换前的文本：", input_text)
print("替换后的文本：", replaced_text)

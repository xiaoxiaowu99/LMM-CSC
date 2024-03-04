

input_path = 'data/all_train_gpt_check.txt'
output_path = 'data/no_wrong_dataset.txt'
output_format_path = 'data/no_wrong_dataset_format.txt'

with open(output_path, 'r', encoding='utf-8') as f:
     lines = f.readlines()
     for line in lines:
         if line != '\n':
             with open(output_format_path, 'a', encoding='utf-8') as writer:
                     writer.write(line)



# with open(input_path, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     i = 1
#     datalist = {}
#     id = ''
#     content = []
#     for line in lines:
#         if line[0:2] == 'id':
#             data = {id: content}
#             id = line[3:]
#             id = id.replace('\n', '', 1)
#             content = []
#             datalist.update(data)
#         else:
#             content.append(line)
#
# right_data = {}
# for one_data in datalist:
#     if one_data != '':
#         if '无' in datalist[one_data][0][5:] or '没有' in datalist[one_data][0][5:] or '不' in datalist[one_data][0][5:]:
#             a_data = {one_data: datalist[one_data]}
#             right_data.update(a_data)
#
# for data_id in right_data:
#     one_dataset = right_data[data_id]
#     with open(output_path, 'a', encoding='utf-8') as writer:
#         writer.write('id:' + data_id)
#         writer.write('\n')
#     for i in range(len(one_dataset)):
#         with open(output_path, 'a', encoding='utf-8') as writer:
#             writer.write(one_dataset[i])
#             writer.write('\n')
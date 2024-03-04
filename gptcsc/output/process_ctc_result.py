label_path = 'qua_labels.txt'
predict_path = 'qua_input.txt'
output_path = 'ctc_zertshot_result2.txt'
label_list = {}
predict_list = {}
lost_data_list = {}
ctc_zeroshot_path = 'ctc_zeroshot_result.txt'
# with open(label_path, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         id = line[4:9]
#         label = line[10:]
#         data = {id: label}
#         label_list.update(data)
#
with open(ctc_zeroshot_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    i = 1
    for line in lines:
        if i % 2 == 1:
            id = line[4:]
            id = id.replace('\n', '', 1)
        if i % 2 == 0:
            predict = line
            predict = predict.replace('\n', '', 1)
            if predict[0:3]=='句子：':
                predict_data = {id: predict[3:]}
                predict_list.update(predict_data)
            else:
                predict_data = {id: predict}
                predict_list.update(predict_data)
        i = i + 1

#  human_eval
for id in predict_list:
    with open(output_path, 'a', encoding='utf-8') as writer:
        writer.write('id:' + str(id))
        writer.write('\n')
        writer.write(predict_list[id])
        writer.write('\n')
